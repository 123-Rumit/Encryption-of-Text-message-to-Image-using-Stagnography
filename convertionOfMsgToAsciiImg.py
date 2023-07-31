def rgbScrambler(pt,x,y,i):
    scrambleType = {
    0:(pt,x,y),
    1:(y,pt,x),
    2:(x,y,pt)
    }
    return scrambleType.get(i%3)
from PIL import Image
from random import randint
#Create a new Image, and a pixel map.
img = Image.new('RGB',(256,256),color = (0,0,0))
pixels = img.load()
msg = open("msg.txt", "r", encoding = "ASCII")
pt = bytearray(msg.read(), "utf-8")
xPts = [0]
yPts = [0]
for i in range(0, len(pt)):
    x = randint(0,254)
    y = randint(0,254)
    while((x in xPts)and(y in yPts)):
        #duplicate pair found, get a new pair
        x = randint(0,254)
        y = randint(0,254)
        #add new unique points to list
    xPts.append(x)
    yPts.append(y)
    
    pixels[xPts[i],yPts[i]] = rgbScrambler(pt[i],x,y,i)
    img.save('msgImg.png')
    r,g,b = pixels[0,0]
for i in range(0,len(pt),3):
    print(str(r),end = ' ')
    print(str(g),end = ' ')
    print(str(b))
    r,g,b = pixels[g,b]
    print(str(r),end = ' ')
    print(str(g),end = ' ')
    print(str(b))
    r,g,b = pixels[b,r]
    print(str(r),end = ' ')
    print(str(g),end = ' ')
    print(str(b))
    r,g,b = pixels[r,g]
    
    