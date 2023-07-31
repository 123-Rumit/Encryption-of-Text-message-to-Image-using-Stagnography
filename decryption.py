from PIL import Image
'''
Debug 
'''
encrypted_image_pixels = open("encryptedPixels.txt","w+")
message_pixels = open("messagePixels.txt","w+")
pub_pixels = open("pubPixels.txt","w+")
private_pixels = open("privatePixels.txt","w+")
decrypted_message = open("decryptedMessage.txt","w+")
EncryptedImage = Image.open('enc.png')
encRGB = EncryptedImage.convert("RGB")
privateKey = Image.open('pk.png')
PK = privateKey.resize((256,256),Image.ANTIALIAS)
priRGB = PK.convert("RGB")
publicKey = Image.open('pub.png')
PUK = publicKey.resize((256,256),Image.ANTIALIAS)
publRGB = PUK.convert("RGB")
''' Initialize a 2d array to save decrypted pixels'''
decryptedPixel = [[]]
decryptedPixel = [[0 for i in range(256)] for i in range(256)]
''' Start processing images '''
for i in range(0,256):
    for j in range(0,256):
        ''' Get the pixel value at a given position '''
        pubR,pubG,pubB = publRGB.getpixel((i,j))
        encR,encG,encB = encRGB.getpixel((i,j))
        priR,priG,priB = priRGB.getpixel((i,j))
        ''' DEBUG '''
        encrypted_image_pixels.write("Location: %d,%d\nR: %d G: %d B: %d\n" % (i, j, encR, encG, encB))
        pub_pixels.write("Location: %d,%d\nR: %d G: %d B: %d\n" % (i, j, pubR, pubG, pubB))
        private_pixels.write("Location: %d,%d\nR: %d G: %d B: %d\n" % (i, j, priR, priG, priB))
        ''' Decryption Algorithm '''
        msgR = int(int(encR) - int(pubR/2) - int(priR/2))
        msgG = int(int(encG) - int(pubG/2) - int(priG/2))
        msgB = int(int(encB) - int(pubB/2) - int(priB/2))
        if( msgR < 0):
            msgR = msgR + 255
        if( msgG < 0):
            msgG = msgG + 255
        if( msgB < 0):
            msgB = msgB + 255
 
        ''' Save the decoded RGB values into a list to access later '''
        decryptedPixel[i][j] = int(msgR),int(msgG),int(msgB)
        ''' DEBUG '''
        #if (msgR != 0 and msgG != 0 and msgB != 0):
        message_pixels.write("Location: %d,%d\nR: %d G: %d B: %d\n" % (i, j, msgR, msgG, msgB))
 
''' Message extraction algorithm '''
msgCount = 0
Xa = 0
Ya = 0
while(True):
    message = decryptedPixel[Xa][Ya][msgCount%3]
    newXa = decryptedPixel[Xa][Ya][(msgCount+1)%3]
    Ya = decryptedPixel[Xa][Ya][(msgCount+2)%3]
    Xa = newXa
    msgCount = msgCount + 1
    if(Xa == 0 and Ya == 0):
        break
    print("%c" %(message),end = "")
    decrypted_message.write("%c" % (message))
message_pixels.close()
encrypted_image_pixels.close()
pub_pixels.close()
private_pixels.close()
decrypted_message.close()
EncryptedImage.close()
publicKey.close()
privateKey.close()