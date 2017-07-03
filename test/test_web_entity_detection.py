from adclassifier import google_interface

inputpath = r'D:\adclassifier\labelled_dataset\political\images'
outputpath = r'D:\adclassifier\labelled_dataset\political\api_responses\web'

google_interface.web_entity_detection(inputpath=inputpath, outputpath=outputpath)
