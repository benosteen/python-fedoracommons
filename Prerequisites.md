# Introduction #

This package serves to bind together a number of libraries to try to make use of the Fedora-Commons software from python as straightforward as possible. It draws on a number of other projects such as the SOAP work from the ZSI package, rdflib for handling RDF triples, and so on.

# Install these first #

If you are on a debian-based OS, such as Ubuntu, you can install the requisite environment as follows. For other OSs, please ensure that the dev packages are installed for python, and that gcc or similar is available.
```
[root]# apt-get install build-essential python-dev python-mysqldb python-pysqlite2
```
Then get easy\_install to install these straight from the cheeseshop:
```
[root]# easy_install -U rdflib==2.4.0
[root]# easy_install ZSI
[root]# easy_install uuid
[root]# easy_install 4Suite-xml
[root]# easy_install pyxml
```
Then, pull down the source from above, or grab a release from the downloads [currently, there isn't a release, so use svn to grab the source.](NB.md)