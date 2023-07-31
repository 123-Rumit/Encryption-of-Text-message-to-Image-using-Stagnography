from PIL import Image 
from random import randint 
 
#Create a new Image, and a pixel map. 
img = Image.new('RGB',(256,256),color = (0,0,0)) 
pixels = img.load() 
for i in range(0,256):
    for j in range(0,256):
        r = randint(0,255)         
        g = randint(0,255)         
        b = randint(0,255)         
        pixels[i,j] = (r,g,b) 
img.save('pk.png') 
