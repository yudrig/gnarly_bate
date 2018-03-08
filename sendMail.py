#!/usr/bin/python

#TODO:make this work both alone and with other class
import getpass
import smtplib
import sys

#This sends SMTP mail via command line arguments.
#args: senderName, senderAddress, recieverName, receiverAddress, subject, message

def sendIt(senderName, senderAddress, recieverName, receiverAddress, subject, message):
    message = """From: %s <%s>
To: %s <%s>
Subject: %s

%s""" % (senderName, senderAddress, recieverName, receiverAddress, subject, message)
    #(pixel_byte_string, mime_type) = pytracking.get_open_tracking_pixel()
    #print message

    try:
        #TODO: Send mail from arbitrary server
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(getpass.getuser()+'@compsci.adelphi.edu',receiverAddress,message)
        sys.exit(0)
    except smtplib.SMTPException:
        print("Mail not sent!")
        sys.exit(1)
    #import pytracking
    #(pixel_byte_string, mime_type) = pytracking.get_open_tracking_pixel()
    return 1

def main():
    sendIt(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])

if __name__ == '__main__': main()
