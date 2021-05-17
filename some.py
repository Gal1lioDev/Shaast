import os
from glob import glob
from PIL import Image

for i, p in enumerate(glob(f'C:\\Users\\shukla\\Desktop\\Aaditya\\Coding\\Projects\\Python\\OpenCV\\Computer-Vision\\Datasets\\Shaast//*.jpeg')):
	print(p)
	#im = Image.open(p)
	#im.save(f'C:\\Users\\shukla\\Desktop\\Aaditya\\Coding\\Projects\\Python\\OpenCV\\Computer-Vision\\Datasets\\Shaast\\{p[94:-5]}.jpg')
    #os.rename(p, f'C:\\Users\\shukla\\Desktop\\Aaditya\\Coding\\Projects\\Python\\OpenCV\\Computer-Vision\\Datasets\\Shaast\\Some New/{p[:2]}.jpg')

'''for fn in os.listdir('C:\\Users\\shukla\\Desktop\\Aaditya\\Coding\\Projects\\Python\\OpenCV\\Computer-Vision\\Datasets\\Shaast'):
	print(fn)'''