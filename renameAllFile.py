import os

FILE_TYPE = '.jpg'
RENAME = 'frame_'
PATH = 'D:\\Python Workspace\\Project_1\\frame'
counter = 0
fileList = sorted(os.listdir(PATH))
print(fileList)

# for getFile in fileList:
#     old_file = os.path.join(PATH,getFile)
#     new_file = os.path.join(PATH,"{}{}{}".format(RENAME,counter,FILE_TYPE))
#     os.rename(old_file,new_file)
#     print("Done!")

# print("There are {} files\' name has been changed!".format(counter))

