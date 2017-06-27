from adclassifier import google_interface

inputpath = r'D:\adclassifier\labelled_dataset\non_political\images2'
outputpath = r'D:\adclassifier\labelled_dataset\non_political\api_responses\vision'

google_interface.text_from_image(inputpath=inputpath, outputpath=outputpath)
