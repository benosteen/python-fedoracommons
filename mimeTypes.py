class mimeTypes(object):
    def getDictionary(self):
        mimetype_to_extension = {}
        extension_to_mimetype = {}
        mimetype_to_extension['text/plain'] = 'txt'
        mimetype_to_extension['text/xml'] = 'xml'
        mimetype_to_extension['text/css'] = 'css'
        mimetype_to_extension['text/javascript'] = 'js'
        mimetype_to_extension['text/rtf'] = 'rtf'
        mimetype_to_extension['text/calendar'] = 'ics'
        mimetype_to_extension['application/msword'] = 'doc'
        mimetype_to_extension['application/msexcel'] = 'xls'
        mimetype_to_extension['application/x-msword'] = 'doc'
        mimetype_to_extension['application/vnd.ms-excel'] = 'xls'
        mimetype_to_extension['application/pdf'] = 'pdf'
        mimetype_to_extension['text/comma-separated-values'] = 'csv'
        
        # And hacky reverse lookups
        for mimetype in mimetype_to_extension:
            extension_to_mimetype[mimetype_to_extension[mimetype]] = mimetype
        
        mimetype_extension_mapping = {}
        mimetype_extension_mapping.update(mimetype_to_extension)
        mimetype_extension_mapping.update(extension_to_mimetype)
        
        return mimetype_extension_mapping
