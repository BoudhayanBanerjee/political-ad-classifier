from adclassifier import google_interface

inputpath = r'D:\adclassifier\labelled_dataset\political\test'
outputpath = r'D:\adclassifier\labelled_dataset\political\text'

google_interface.json_parser(inputpath=inputpath, outputpath=outputpath, filetype='web')
