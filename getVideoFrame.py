import numpy as np
import cv2
import os
import shutil

#Clear Data
frameFolder = 'D:\Python Workspace\Project_1\\frame\\'
for filename in os.listdir(frameFolder):
    file_path = os.path.join(frameFolder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

#Capture Frames
cap = cv2.VideoCapture('D:\Python Workspace\Project_1\\video\\counter.mp4')
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (288, 608), interpolation=cv2.INTER_CUBIC)
    if(count%2==0):
        cv2.imwrite('{}frame_{:d}.jpg'.format(frameFolder,count//2), frame)
    print(count)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count += 1
cap.release()
cv2.destroyAllWindows()