from adclassifier import google_interface

inputpath = r'D:\adclassifier\labelled_dataset\non_political\api_responses\vision'
outputpath = r'D:\adclassifier\labelled_dataset\non_political\text_datasets\vision\original'

google_interface.json_parser(inputpath=inputpath, outputpath=outputpath, filetype='image')
