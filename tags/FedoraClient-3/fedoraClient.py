import fedoraClient20, fedoraClient22, fedoraClient30

class ClientFactory(object):
    def __init__(self):
        self.supported_versions = ['2.0','2.2','3.0']
        
    def getClient(self,serverurl='http://localhost:8080/fedora', username='fedoraAdmin', password='fedoraAdmin', version="3.0"):
        if version=="2.2":
            return fedoraClient22.FedoraClient(serverurl=serverurl, username=username, password=password, version="2.2")
        elif version=="2.0":
            return fedoraClient20.FedoraClient(serverurl=serverurl, username=username, password=password, version="2.0")
        elif version=="3.0":
            return fedoraClient30.FedoraClient(server=serverurl, username=username, password=password, version="3.0")
        else:
            raise 'FedoraClient supports APIs for Fedora versions %s only' % (self.supported_versions)
