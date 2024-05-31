import cv2
import glob
import re
img_array = []
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts
for filename in sorted(glob.glob('img-dict/*.png'), key=numericalSort):
    img = cv2.imread(filename)
    #img = cv2.resize(img, (3840,2160))
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
forc=cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('scenario2.mp4',forc, 30, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()