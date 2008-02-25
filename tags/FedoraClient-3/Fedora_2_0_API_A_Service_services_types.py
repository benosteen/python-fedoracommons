################################################## 
# Fedora_API_A_Service_services_types.py 
# generated by ZSI.generate.wsdl2python
##################################################


import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED

##############################
# targetNamespace
# http://www.fedora.info/definitions/1/0/types/
##############################

class FedoraAPI_2_0_ns:
    targetNamespace = "http://www.fedora.info/definitions/1/0/types/"

    class Property_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "Property")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.Property_Def.schema
            TClist = [ZSI.TC.String(pname="name", aname="_name", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="value", aname="_value", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._name = None
                    self._value = None
                    return
            Holder.__name__ = "Property_Holder"
            self.pyclass = Holder

    class ArrayOfString_Def(ZSI.TC.Array, TypeDefinition):
        #complexType/complexContent base="SOAP-ENC:Array"
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ArrayOfString")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ofwhat = ZSI.TC.String(None, typed=False)
            atype = (u'http://www.w3.org/2001/XMLSchema', u'string[]')
            ZSI.TCcompound.Array.__init__(self, atype, ofwhat, pname=pname, childnames='item', **kw)

    class passByRef_Def(ZSI.TC.String, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "passByRef")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

    class passByValue_Def(ZSI.TC.String, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "passByValue")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

    class datastreamInputType_Def(ZSI.TC.String, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "datastreamInputType")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

    class userInputType_Def(ZSI.TC.String, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "userInputType")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

    class defaultInputType_Def(ZSI.TC.String, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "defaultInputType")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

    class MethodParmDef_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "MethodParmDef")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.MethodParmDef_Def.schema
            TClist = [ZSI.TC.String(pname="parmName", aname="_parmName", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="parmType", aname="_parmType", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="parmDefaultValue", aname="_parmDefaultValue", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","ArrayOfString",lazy=False)(pname="parmDomainValues", aname="_parmDomainValues", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.Boolean(pname="parmRequired", aname="_parmRequired", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="parmLabel", aname="_parmLabel", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="parmPassBy", aname="_parmPassBy", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","passByRef",lazy=False)(pname="PASS_BY_REF", aname="_PASS_BY_REF", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","passByValue",lazy=False)(pname="PASS_BY_VALUE", aname="_PASS_BY_VALUE", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","datastreamInputType",lazy=False)(pname="DATASTREAM_INPUT", aname="_DATASTREAM_INPUT", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","userInputType",lazy=False)(pname="USER_INPUT", aname="_USER_INPUT", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","defaultInputType",lazy=False)(pname="DEFAULT_INPUT", aname="_DEFAULT_INPUT", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._parmName = None
                    self._parmType = None
                    self._parmDefaultValue = None
                    self._parmDomainValues = None
                    self._parmRequired = None
                    self._parmLabel = None
                    self._parmPassBy = None
                    self._PASS_BY_REF = None
                    self._PASS_BY_VALUE = None
                    self._DATASTREAM_INPUT = None
                    self._USER_INPUT = None
                    self._DEFAULT_INPUT = None
                    return
            Holder.__name__ = "MethodParmDef_Holder"
            self.pyclass = Holder

    class DatastreamDef_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "DatastreamDef")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.DatastreamDef_Def.schema
            TClist = [ZSI.TC.String(pname="ID", aname="_ID", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="label", aname="_label", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="MIMEType", aname="_MIMEType", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._ID = None
                    self._label = None
                    self._MIMEType = None
                    return
            Holder.__name__ = "DatastreamDef_Holder"
            self.pyclass = Holder

    class ListSession_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ListSession")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.ListSession_Def.schema
            TClist = [ZSI.TC.String(pname="token", aname="_token", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.InonNegativeInteger(pname="cursor", aname="_cursor", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.InonNegativeInteger(pname="completeListSize", aname="_completeListSize", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="expirationDate", aname="_expirationDate", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._token = None
                    self._cursor = None
                    self._completeListSize = None
                    self._expirationDate = None
                    return
            Holder.__name__ = "ListSession_Holder"
            self.pyclass = Holder

    class RepositoryInfo_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "RepositoryInfo")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.RepositoryInfo_Def.schema
            TClist = [ZSI.TC.String(pname="repositoryName", aname="_repositoryName", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="repositoryVersion", aname="_repositoryVersion", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="repositoryBaseURL", aname="_repositoryBaseURL", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="repositoryPIDNamespace", aname="_repositoryPIDNamespace", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="defaultExportFormat", aname="_defaultExportFormat", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="OAINamespace", aname="_OAINamespace", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","ArrayOfString",lazy=False)(pname="adminEmailList", aname="_adminEmailList", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="samplePID", aname="_samplePID", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="sampleOAIIdentifier", aname="_sampleOAIIdentifier", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="sampleSearchURL", aname="_sampleSearchURL", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="sampleAccessURL", aname="_sampleAccessURL", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="sampleOAIURL", aname="_sampleOAIURL", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","ArrayOfString",lazy=False)(pname="retainPIDs", aname="_retainPIDs", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._repositoryName = None
                    self._repositoryVersion = None
                    self._repositoryBaseURL = None
                    self._repositoryPIDNamespace = None
                    self._defaultExportFormat = None
                    self._OAINamespace = None
                    self._adminEmailList = None
                    self._samplePID = None
                    self._sampleOAIIdentifier = None
                    self._sampleSearchURL = None
                    self._sampleAccessURL = None
                    self._sampleOAIURL = None
                    self._retainPIDs = None
                    return
            Holder.__name__ = "RepositoryInfo_Holder"
            self.pyclass = Holder

    class ArrayOfMethodParmDef_Def(ZSI.TC.Array, TypeDefinition):
        #complexType/complexContent base="SOAP-ENC:Array"
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ArrayOfMethodParmDef")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ofwhat = FedoraAPI_2_0_ns.MethodParmDef_Def(None, typed=False)
            atype = (u'http://www.fedora.info/definitions/1/0/types/', u'MethodParmDef[]')
            ZSI.TCcompound.Array.__init__(self, atype, ofwhat, pname=pname, childnames='item', **kw)

    class ObjectMethodsDef_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ObjectMethodsDef")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.ObjectMethodsDef_Def.schema
            TClist = [ZSI.TC.String(pname="PID", aname="_PID", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="bDefPID", aname="_bDefPID", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="methodName", aname="_methodName", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","ArrayOfMethodParmDef",lazy=False)(pname="methodParmDefs", aname="_methodParmDefs", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="asOfDate", aname="_asOfDate", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._PID = None
                    self._bDefPID = None
                    self._methodName = None
                    self._methodParmDefs = None
                    self._asOfDate = None
                    return
            Holder.__name__ = "ObjectMethodsDef_Holder"
            self.pyclass = Holder

    class ComparisonOperator_Def(ZSI.TC.String, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ComparisonOperator")
        def __init__(self, pname, **kw):
            ZSI.TC.String.__init__(self, pname, pyclass=None, **kw)
            class Holder(str):
                typecode = self
            self.pyclass = Holder

    class Condition_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "Condition")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.Condition_Def.schema
            TClist = [ZSI.TC.String(pname="property", aname="_property", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","ComparisonOperator",lazy=False)(pname="operator", aname="_operator", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="value", aname="_value", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._property = None
                    self._operator = None
                    self._value = None
                    return
            Holder.__name__ = "Condition_Holder"
            self.pyclass = Holder

    class ArrayOfCondition_Def(ZSI.TC.Array, TypeDefinition):
        #complexType/complexContent base="SOAP-ENC:Array"
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ArrayOfCondition")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ofwhat = FedoraAPI_2_0_ns.Condition_Def(None, typed=False)
            atype = (u'http://www.fedora.info/definitions/1/0/types/', u'Condition[]')
            ZSI.TCcompound.Array.__init__(self, atype, ofwhat, pname=pname, childnames='item', **kw)

    class FieldSearchQuery_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "FieldSearchQuery")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.FieldSearchQuery_Def.schema
            TClist = [GTD("http://www.fedora.info/definitions/1/0/types/","ArrayOfCondition",lazy=False)(pname="conditions", aname="_conditions", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="terms", aname="_terms", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._conditions = None
                    self._terms = None
                    return
            Holder.__name__ = "FieldSearchQuery_Holder"
            self.pyclass = Holder

    class ArrayOfProperty_Def(ZSI.TC.Array, TypeDefinition):
        #complexType/complexContent base="SOAP-ENC:Array"
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ArrayOfProperty")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ofwhat = FedoraAPI_2_0_ns.Property_Def(None, typed=False)
            atype = (u'http://www.fedora.info/definitions/1/0/types/', u'Property[]')
            ZSI.TCcompound.Array.__init__(self, atype, ofwhat, pname=pname, childnames='item', **kw)

    class MIMETypedStream_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "MIMETypedStream")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.MIMETypedStream_Def.schema
            TClist = [ZSI.TC.String(pname="MIMEType", aname="_MIMEType", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.Base64String(pname="stream", aname="_stream", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","ArrayOfProperty",lazy=False)(pname="header", aname="_header", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._MIMEType = None
                    self._stream = None
                    self._header = None
                    return
            Holder.__name__ = "MIMETypedStream_Holder"
            self.pyclass = Holder

    class ObjectProfile_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ObjectProfile")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.ObjectProfile_Def.schema
            TClist = [ZSI.TC.String(pname="pid", aname="_pid", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="objLabel", aname="_objLabel", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="objContentModel", aname="_objContentModel", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="objType", aname="_objType", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="objCreateDate", aname="_objCreateDate", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="objLastModDate", aname="_objLastModDate", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="objDissIndexViewURL", aname="_objDissIndexViewURL", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="objItemIndexViewURL", aname="_objItemIndexViewURL", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._pid = None
                    self._objLabel = None
                    self._objContentModel = None
                    self._objType = None
                    self._objCreateDate = None
                    self._objLastModDate = None
                    self._objDissIndexViewURL = None
                    self._objItemIndexViewURL = None
                    return
            Holder.__name__ = "ObjectProfile_Holder"
            self.pyclass = Holder

    class ObjectFields_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ObjectFields")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.ObjectFields_Def.schema
            TClist = [ZSI.TC.String(pname="pid", aname="_pid", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="label", aname="_label", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="fType", aname="_fType", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="cModel", aname="_cModel", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="state", aname="_state", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="ownerId", aname="_ownerId", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="cDate", aname="_cDate", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="mDate", aname="_mDate", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="dcmDate", aname="_dcmDate", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="bDef", aname="_bDef", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="bMech", aname="_bMech", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="title", aname="_title", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="creator", aname="_creator", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="subject", aname="_subject", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="description", aname="_description", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="publisher", aname="_publisher", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="contributor", aname="_contributor", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="date", aname="_date", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="type", aname="_type", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="format", aname="_format", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="identifier", aname="_identifier", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="source", aname="_source", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="language", aname="_language", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="relation", aname="_relation", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="coverage", aname="_coverage", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="rights", aname="_rights", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._pid = None
                    self._label = None
                    self._fType = None
                    self._cModel = None
                    self._state = None
                    self._ownerId = None
                    self._cDate = None
                    self._mDate = None
                    self._dcmDate = None
                    self._bDef = []
                    self._bMech = []
                    self._title = []
                    self._creator = []
                    self._subject = []
                    self._description = []
                    self._publisher = []
                    self._contributor = []
                    self._date = []
                    self._type = []
                    self._format = []
                    self._identifier = []
                    self._source = []
                    self._language = []
                    self._relation = []
                    self._coverage = []
                    self._rights = []
                    return
            Holder.__name__ = "ObjectFields_Holder"
            self.pyclass = Holder

    class ArrayOfObjectFields_Def(ZSI.TC.Array, TypeDefinition):
        #complexType/complexContent base="SOAP-ENC:Array"
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ArrayOfObjectFields")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ofwhat = FedoraAPI_2_0_ns.ObjectFields_Def(None, typed=False)
            atype = (u'http://www.fedora.info/definitions/1/0/types/', u'ObjectFields[]')
            ZSI.TCcompound.Array.__init__(self, atype, ofwhat, pname=pname, childnames='item', **kw)

    class FieldSearchResult_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "FieldSearchResult")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = FedoraAPI_2_0_ns.FieldSearchResult_Def.schema
            TClist = [GTD("http://www.fedora.info/definitions/1/0/types/","ListSession",lazy=False)(pname="listSession", aname="_listSession", minOccurs=0, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("http://www.fedora.info/definitions/1/0/types/","ArrayOfObjectFields",lazy=False)(pname="resultList", aname="_resultList", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._listSession = None
                    self._resultList = None
                    return
            Holder.__name__ = "FieldSearchResult_Holder"
            self.pyclass = Holder

    class ArrayOfObjectMethodsDef_Def(ZSI.TC.Array, TypeDefinition):
        #complexType/complexContent base="SOAP-ENC:Array"
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ArrayOfObjectMethodsDef")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ofwhat = FedoraAPI_2_0_ns.ObjectMethodsDef_Def(None, typed=False)
            atype = (u'http://www.fedora.info/definitions/1/0/types/', u'ObjectMethodsDef[]')
            ZSI.TCcompound.Array.__init__(self, atype, ofwhat, pname=pname, childnames='item', **kw)

    class ArrayOfDatastreamDef_Def(ZSI.TC.Array, TypeDefinition):
        #complexType/complexContent base="SOAP-ENC:Array"
        schema = "http://www.fedora.info/definitions/1/0/types/"
        type = (schema, "ArrayOfDatastreamDef")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ofwhat = FedoraAPI_2_0_ns.DatastreamDef_Def(None, typed=False)
            atype = (u'http://www.fedora.info/definitions/1/0/types/', u'DatastreamDef[]')
            ZSI.TCcompound.Array.__init__(self, atype, ofwhat, pname=pname, childnames='item', **kw)

# end class FedoraAPI_2_0_ns (tns: http://www.fedora.info/definitions/1/0/types/)
