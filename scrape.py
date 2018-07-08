import os

# Downloading individual images
def img_download(keyword, iamge_size = "icon",N = 100):
	command = "googleimagesdownload -k " + keyword + " -s " + image_size + " -l " + str(N)
	os.system(command)

# Download function (as an abstraction)
def download(img_list,image_size,N):
	for img in img_list:
		img_download(img,image_size,N)


if __name__ == "__main__":

	img_list = ["black", "white"]  # Keywords of images to be downloaded from Google Images
	N = 1                          # Number of images to be downloaded (N>=1)
	image_size = "icon"            # Size of images to be downloaded
	height = 4                     # Height of compressed image
	width = 4		       # Width of compressed image
	
	try:
		download(img_list,image_size,N)
		#square_compression()


	except:
		print("Error")
		
		
