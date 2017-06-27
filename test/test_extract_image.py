from adclassifier import data_process

inputpath = r'D:\adclassifier\labelled_dataset\non_political\videos'
outputpath = r'D:\adclassifier\labelled_dataset\non_political\images'

data_process.extract_frame(inputpath=inputpath, outputpath=outputpath)

