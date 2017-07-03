from adclassifier import google_interface

inputpath = r'D:\adclassifier\labelled_dataset\non_political\audios'
outputpath = r'D:\adclassifier\labelled_dataset\non_political\api_responses\speech'

google_interface.text_from_audio(inputpath=inputpath, outputpath=outputpath)
