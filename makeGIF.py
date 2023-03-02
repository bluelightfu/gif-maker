import os
import imageio

png_dir = 'D:\Python Workspace\Project_1\\frame'
images = []
counter = 0
frames = os.listdir(png_dir)
while (counter <len(frames)):
    file_path = os.path.join(png_dir, "frame_{}.jpg".format(counter))
    images.append(imageio.imread(file_path))
    counter += 1

imageio.mimsave('.\\Project_1\\gif\\新增專案.gif', images,fps=5)
print("GIF Done!")