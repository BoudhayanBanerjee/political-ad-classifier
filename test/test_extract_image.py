from adclassifier.adclassifier import data_process

inputpath = r'D:\ypai\data\json\video'
outputpath = r'D:\ypai\data\json\image'

data_process.extract_frame(input_path=inputpath, output_path=outputpath)
print("ok")
