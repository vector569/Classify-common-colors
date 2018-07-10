import os
import numpy as np
import subprocess
import cv2
import pandas as pd

# Downloading individual images
def img_download(keyword, image_size = "medium",N = 100):
	command = "googleimagesdownload -k " + keyword + " -s " + image_size + " -l " + str(N) + " -f jpg" + " --chromedriver /home/arav/Desktop/data/Github/chromedriver_linux64/chromedriver"
	os.system(command)

# Download function (as an abstraction)
def download(img_list,image_size,N):
	for img in img_list:
		img_download(img,image_size,N)


# Returns all file names as a list to names_grab(...)
def process_name(string):
	string = str(string).strip('\'').strip('b\'')
	ls = string.split("\\n")
	del(ls[-1])
	return ls
	
# Return existing file names to rename(...)
def names_grab(img):
	command = "cd ~/Desktop/data/Github/Project1/downloads/" + img + " && ls"
	proc = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	list_of_names = process_name(out)
	return list_of_names

# Rename downloaded files
def rename(img_list):
	dictionary = {}
	for img in img_list:
		print(img)
		list_of_names = names_grab(img)
		dictionary[img] = len(list_of_names)
		i = 1
		for name in list_of_names:
			command1 = "cd ~/Desktop/data/Github/Project1/downloads/" + img + " && " 
			command2 = "mv " + "'" + name + "'" + " " + str(i) + ".jpg"
			command = command1 + command2
			os.system(command)
			i += 1
	return dictionary

# Compression and writing the image as a CSV file for analysis
def square_compression_and_writing_csv(img_list,N,height,width,name_of_csv,dictionary):
	k = 0
	list_data = []
	for img in img_list:
		print(img)
		length = dictionary[img]
		for i in range(1,length+1):
			string = "/home/arav/Desktop/data/Github/Project1/downloads/" + img + "/" + str(i) + ".jpg"
			pic = cv2.imread(string,cv2.IMREAD_COLOR)
			print(i)
			if pic is not None:
				pic = np.asarray(cv2.resize(pic,(height,width)))
				pic = np.array(pic.reshape(1,1,-1)[0][0]).tolist()
				pic.append(img)
				list_data.append(pic)
				k += 1
			else:
				length -= 1
	pdf = pd.DataFrame(list_data)
	pdf.to_csv(name_of_csv)


def create_csv(img_list, N,image_size = "medium", height = 4, width = 4, name_of_csv = "data.csv"):

	# img_list    -> Keywords of images to be downloaded from Google Images
	# N           -> Number of images to be downloaded (N>=1)
	# image_size  -> Size of images to be downloaded
	# height      -> Height of compressed image
	# width       -> Width of compressed image
	# name_of_csv -> Name of csv file to be saved

	try:
		#download(img_list,image_size,N)
		#print("\nDownload Successful\n")
		dictionary = rename(img_list)
		pdf = square_compression_and_writing_csv(img_list,N,height,width,name_of_csv,dictionary)
	except:
		print("Error")
		
		
