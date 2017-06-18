from adclassifier import google_interface

inputpath = r'D:\ypai\data\json\json'
outputpath = r'D:\ypai\data\json\text'

google_interface.json_parser(inputpath=inputpath, outputpath=outputpath, filetype='audio')
