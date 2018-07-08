import os
import numpy as np
import subprocess
import cv2
import pandas as pd

# Downloading individual images
def img_download(keyword, iamge_size = "icon",N = 100):
	command = "googleimagesdownload -k " + keyword + " -s " + image_size + " -l " + str(N) + " -f jpg"
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
	for img in img_list:
		list_of_names = names_grab(img)
		i = 1
		for name in list_of_names:
			command1 = "cd ~/Desktop/data/Github/Project1/downloads/" + img + " && " 
			command2 = "mv " + "'" + name + "'" + " " + str(i) + ".jpg"
			command = command1 + command2
			os.system(command)
			i += 1

# Compression and writing the image as a CSV file for analysis
def square_compression_and_writing_csv(img_list,N,height,width,name_of_csv):
	k = 0
	pd = pd.DataFrame(None,columns=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'])
	for img in img_list:
		for i in range(1,N+1):
			string = "/home/arav/Desktop/data/Github/Project1/downloads/" + img + "/" + str(i) + ".jpg"
			pic = cv2.imread(string,cv2.IMREAD_COLOR)
			pic = np.asarray(cv2.resize(pic,(height,width)))
			pic = pic.reshape(1,1,-1)[0][0]
			#H, W,_ = pic.shape
			#pic = np.asarray(pic)
			#print(str(np.arange(16)).split(' '),"\n")



# Main function
if __name__ == "__main__":

	img_list = ["black", "white"]  # Keywords of images to be downloaded from Google Images
	N = 3                          # Number of images to be downloaded (N>=1)
	image_size = "medium"          # Size of images to be downloaded
	height = 4                     # Height of compressed image
	width = 4		       # Width of compressed image
	name_of_csv = "data.csv"
	
	try:
		#download(img_list,image_size,N)
		#print("\nDownload Successful\n")
		#rename(img_list)
		square_compression_and_writing_csv(img_list,N,height,width,name_of_csv)
		#print(img)

	except:
		print("Error")
		
		
