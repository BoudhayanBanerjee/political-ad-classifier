import os

inputPath = r'D:\adclassifier\labelled_dataset\political\images2'

#frame = 'frame-%02d.png' % (frameNum)
for videoFolder in os.listdir(inputPath):
    countframe = len(os.listdir(os.path.join(inputPath, videoFolder)))
    selectframe = ['frame-%02d.png' % (countframe), 'frame-%02d.png' % (countframe - 1), 'frame-%02d.png' % (countframe - 2)]
    for file in os.listdir(os.path.join(inputPath, videoFolder)):
        if file not in selectframe:
            os.remove(os.path.join(inputPath, videoFolder, file))
