from resemble import*
Resemble.api_key('B2uOK6Cac0oo1r3frYJl7wtt')
    
#Gets the default Resemble project
project_uuid = Resemble.v2.projects.all(1,10)['items'][0]['uuid']
    
#Gets the voice uuid. In this example we'll obtain the first
voice_uuid = Resemble.v2.voices.all(1,10)['items'][0]['uuid']

#Creates a new Text-to-Speech job with the specified text and language.
body = 'This is a test'
response = Resemble.v2.clips.create_sync(project_uuid,
                                         voice_uuid,
                                         body,
                                         title = None,
                                         sample_rate = None,
                                         include_timestamps = None,
                                         is_public = None,
                                         is_archived = None,
                                         raw = None)
print(response)