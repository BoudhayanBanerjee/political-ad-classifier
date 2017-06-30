from adclassifier import google_interface

inputpath = r'D:\adclassifier\labelled_dataset\non_political\api_responses\speech'
outputpath = r'D:\adclassifier\labelled_dataset\non_political\text_datasets\speech'

google_interface.json_parser(inputpath=inputpath, outputpath=outputpath, filetype='audio')
