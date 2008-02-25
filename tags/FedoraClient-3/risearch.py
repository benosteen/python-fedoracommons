from xml.dom import minidom
from xml.dom import Node

from archive.lib.relsext_mapping import *

from Ft.Xml.Xslt import Transform

import urllib
import string
import re, csv

class Risearch(object):
    def __init__(self, server='http://localhost:8080/fedora'):
        self.baseurl = server
        self.server = server + '/risearch'
        self.fedoraClient = None
        
        # HACK:  (Not needed now - 10Aug2007 - due to trippi changes)
        # Calling findTriples with a full triple (i.e. no wildcards) returns nothing
        # if the triple doesn't exist, or returns the same triple if it does exist.
        
        # This will match a single triple response in N-Triple format
        # self.triple_pattern = re.compile('^<.*?> <.*?> <.*?> .\n')
        
        m = Predicates()
        self.rev_relsext = m.getReverseDictionary()

    def getSearchResultSet(self, query, desiredformat='Sparql', limit='10'):
        # Get Tuples from the risearch servlet running on the Fedora
        # server
        response = self.getTuples(query, format=desiredformat, limit=limit)
        
        # Instantiate items hash
        items = {}
        
        # Create a minidom reader
        if desiredformat == 'Sparql':
            # Create minidom. SAX parsing may be a good match here, but I
            # feel in a DOM kinda mood.
            doc = minidom.parseString(response).documentElement
            
            
            # Select all the <result> elements and subelements
            results = doc.getElementsByTagName('result')
            
            for resultset in results:
                # Select the child elements of the <result> element,
                # as the <result> element is there only to group them
                results = resultset.childNodes
                
                # Select out the first <object> element
                object = resultset.getElementsByTagName('object')[0]
                
                # Select out the first <dctitle> element
                dctitle = resultset.getElementsByTagName('dctitle')[0]

                # <object> is normally formatted in the following way
                # in Sparql:  <object uri="info:fedora/namespace:id"/>
                # Manipulate node to get the 'namespace:id' text, the
                # pid of the object in question
                fedora_uri = object.getAttribute('uri')
                parsed_fedora_uri = fedora_uri.split('/')

                # Check to see if it is a pid URI. Fail if not.
                if parsed_fedora_uri[0] == 'info:fedora':
                    pid = parsed_fedora_uri[1]
                else:
                    # Pass None to show failure
                    pid = None
                    
                items[pid] = self._getText(dctitle.childNodes)
        
        elif desiredformat == 'csv':
            # Much quicker to parse
            csv_reader = csv.reader(response.split("\n"))
            headers = None
            for row in csv_reader:
                if headers == None:
                    headers = row
                else:
                    # By convention, anticipate that the first item in the row is a pid:
                    if len(row)>0:
                        parsed_fedora_uri = row[0].split('/')
                        if parsed_fedora_uri[0] == 'info:fedora':
                            pid = parsed_fedora_uri[1]
                        else:
                            # Pass the text of the row:
                            pid = row[0]
                        if len(row) == 2:
                            # Set as a literal item
                            items[pid] = row[1]
                        else:
                            # Set as a list of the columns:
                            items[pid] = row[1:]

        return items
    
    def _getText(self, nodelist):
        text = ''
        for node in nodelist:
            if node.nodeType == Node.TEXT_NODE:
                text += node.nodeValue
        return text
    
    def getTrippi(self, query_type, query, lang='itql', format='Sparql',limit='100'):
        # Get Tuples from the risearch servlet running on the Fedora
        # server
        
        query_type = query_type.lower()
        
        if query != '' and (query_type == 'tuples' or query_type == 'triples'):
            queryparams = urllib.urlencode({'type' : query_type, 'lang' : lang, 'format' : format, 'query' : query, 'limit' : limit })
            response = urllib.urlopen( self.server, queryparams).read()
            return response

        # Test for a correct response, return blank if Trippi errors
        # out
        return None
    
    def getTriples(self, query, lang='spo', format='N-Triples', limit='100', offset='0'):
        return self.getTrippi('triples', query, lang, format, limit)
        
    def getTuples(self, query, lang='itql', format='sparql', limit='100', offset='0'):
        return self.getTrippi('tuples', query, lang, format, limit)
        
    def getCount(self, query, lang='spo', query_type='triples'):
        return self.getTrippi(query_type, query, lang=lang, format='count', limit="")

    def doesTripleExist(self, query):
        # Convienience method - lang is 'spo' and relies on my patches to Trippiserver
        count = self.getCount(query)
        
        if count != '0':
            return True
        else:
            return False
            
        """
        Old method:
        
        triple_pattern = re.compile('^<.*?> <.*?> <.*?> .')
        response = self.getTrippi('triples', query, lang="spo", format='N-Triples', limit="10")
        if triple_pattern.match(response):
            return True
        else:
            return False
        """

##  End of Basic RIsearch API functions
################################################################################################

################################################################################################
##  Beginning of convenience functions based on the above API

    def doesPIDExist(self, pid):
        """Test to see if the pid node is the subject of any triples in the triplestore
        # Very much faster than SOAP methods, but is accurate only so far as the 
        # triplestore is accurate"""
        return self.doesTripleExist(query='<info:fedora/'+pid+'> * *')
        
# For UUID <-> tinypid linking
    def resolveTinyPid(self, pid):
        query = "select $object from <#ri> where $object <info:fedora/fedora-system:def/model#label> '" + pid +"'"
        linelist = self.getTuples(query, format='csv').split("\n")
        if len(linelist) == 3:
            return linelist[1].split('/')[-1]
        else:
            return False
        
    def simplifyUUID(self, uuid_pid):
        query = "select $object from <#ri> where <info:fedora/"+uuid_pid+"> <info:fedora/fedora-system:def/model#label> $object"
        linelist = self.getTuples(query, format='csv').split("\n")
        if len(linelist) == 3:
            return linelist[1].split('/')[-1]
        else:
            return False
        
        
