#!/usr/bin/python2
import sys
from PIL import Image

def imageCreation(EmailID, userID=[]):
#pass in the ids will not be searching for them creating images
#parameters user id and emial ids as tuprles
#opens the image pixel.png
#set while to the length of the userID list
        for user in userID :
                im1 = Image.open("pixel.png")
                # print(im1.format, im1.size,im1.mode)
                #create copy of the orignal image
                im2 = im1.copy()
                #Call the UserID and EmailID to apply the UserID and EmailID for the image name
                Identification ="""pix_%s_%s.png"""%(EmailID, user[0])
                im2.save(Identification,format="png")
                #print for for the confirm that it has been created
                #print(im2.format, im2.size, im2.mode)

#should accept an array list of userIDs then hard code which EmailID
def main():
        imageCreation(sys.argv[1],[])

if __name__ == '__main__' : main()
