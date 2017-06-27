from adclassifier import data_process

inputpath = r'D:\adclassifier\labelled_dataset\non_political\videos'
outputpath = r'D:\adclassifier\labelled_dataset\non_political\audios'

data_process.extract_audio(inputpath=inputpath, outputpath=outputpath)
