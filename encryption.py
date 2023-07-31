from PIL import Image
from random import randint


#Import/create images and their pixel maps
PK = Image.open("pk.png","r")
PK = PK.resize((256,256),Image.ANTIALIAS)
PKrgb = PK.convert("RGB")

MSG = Image.open("msgImg.png","r")
MSGrgb = MSG.convert("RGB")

PUB = Image.open("pub.png","r")
PUB = PUB.resize((256,256),Image.ANTIALIAS)
PUBrgb = PUB.convert("RGB")

ENCRimg = Image.new('RGB',(256,256),color = (0,0,0))
ENCRpixels = ENCRimg.load()
DECRimg = Image.new('RGB',(256,256),color = (0,0,0))
DECRpixels = DECRimg.load()

#create text files for each image (for testing/debugging)
msgimgtxt = open("msgimg.txt","w+")
pubtxt = open("pub.txt","w+")
pktxt = open("pk.txt","w+")
enctxt = open("enc.txt","w+")
dectxt = open("dec.txt","w+")
for i in range(0,256):
    for j in range(0,256):
        #get RGB values from all three images
        pubR,pubG,pubB = PUBrgb.getpixel((i,j))
        priR,priG,priB = PKrgb.getpixel((i,j))
        msgR,msgG,msgB = MSGrgb.getpixel((i,j))
        #write RGB values to txt file (for testing/debugging)
        msgimgtxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,msgR,msgG,msgB))
        pubtxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,pubR,pubG,pubB))
        pktxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,priR,priG,priB))
        #Calculate new encrypted image RGB values
        ENCRpixels[i,j] = (
        (int(pubR/2) + int(priR/2) + msgR)%255,
        (int(pubG/2) + int(priG/2) + msgG)%255,
        (int(pubB/2) + int(priB/2) + msgB)%255)
        #Write the rgb values to text file (for testing/debugging)
        enctxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,ENCRpixels[i,j][0],ENCRpixels[i,j][1],ENCRpixels[i,j][2]))
 
        #perform the decrypt operation on these pixels
        red = int(ENCRpixels[i,j][0]) - int(pubR/2) - int(priR/2)
        green = int(ENCRpixels[i,j][1]) - int(pubG/2) - int(priG/2)
        blue = int(ENCRpixels[i,j][2]) - int(pubB/2) - int(priB/2)
        if(red < 0):
            red = red + 255
        if(green < 0):
            green = green + 255
        if(blue < 0):
            blue = blue + 255
 
        #set the rgb values of our decrypted image (testing only)
        DECRpixels[i,j] = (red,green,blue)
        dectxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,DECRpixels[i,j][0],DECRpixels[i,j][1],DECRpixels[i,j][2]))
        
        #close/save all files
msgimgtxt.close()
pubtxt.close()
pktxt.close()
enctxt.close()
dectxt.close()
DECRimg.save("dec.png")
ENCRimg.save("enc.png")