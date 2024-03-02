from matplotlib.image import imread     #to read the image
import matplotlib.pyplot as plt         #to display the image
import numpy as np                      #to manipulate arrays

'''
RBG image -> R channel + G channel +B channel
In pyton, we use a method called as Luminosity Method
Human eyes are mre sensitive to green than blue or red.
So this method accounts for the luminanace (brightness) of each chanel.

The formula we are using is:
gray_value = 0.2973 * R + 0.6274 * G + 0.0753 * B
This is from Adobe RGB values.

Additionally, there is a value called Gamma which we wont be using here
Gamma affects the relationship bw pixel value and their corresponding brightness
Gamma in most cases is close to 1 (so we wont be using it)
However if one wants to use it, then use the formua:
gray_value = 0.2973 * R**A + 0.6274 * G**A + 0.0753 * B**A
where A=1.04 -> Gamma Value
if you inc gamma value, the grescaledimage will appear darker, and if it is low, then it will appear lighter

Depending on need, these can be changed too,
e.g: sRBG Standard uses; G_V= 0.299*R + 0.587*G + 0.114*B 
'''

inp_img = imread("insert_image_address")
'''
sometimes there may be an error, and will consider '\' as an escape line. In that case, replace '\' with '\\'.
This will resolve the error
e.g: inp_img = imread(r"C:\Users\Gokul\Dropbox\My PC (Titan)\Desktop\Random Stuff\Naruto 2.jpeg")          -> may cause error
e.g: inp_img = imread("C:\\Users\\Gokul\\Dropbox\\My PC (Titan)\\Desktop\\Random Stuff\\Naruto 2.jpeg")    -> resolves error
'''

#to sepeate channels of input image into 3 parts
r,g,b=inp_img[:,:,0],inp_img[:,:,1],inp_img[:,:,2]

#defining weight of each corresponding channel
r_constant,g_constant,b_constant=0.2973,0.6274,0.0753

grayscale_image=r_constant*r + g_constant*g + b_constant*b

#creating a figure
fig=plt.figure(1)

#adding subplots
#121 -> 1x2 grid on first posn (leftmost) and 122 -> 1x2 grid on second posn (rightmost)
img1,img2=fig.add_subplot(121),fig.add_subplot(122)

#displaying image within first subplot
img1.imshow(inp_img)

# Display the grayscale image within the second subplot using the 'gray' colormap
img2.imshow(grayscale_image, cmap=plt.cm.get_cmap('gray'))

#show all figures 
fig.show()
plt.show()
