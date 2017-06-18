from adclassifier import data_process

inputpath = r'D:\ypai\data\json\video'
outputpath = r'D:\ypai\data\json\audio'

data_process.extract_audio(inputpath=inputpath, outputpath=outputpath)
