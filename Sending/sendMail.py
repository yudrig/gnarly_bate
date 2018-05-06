#!/usr/bin/python3

#This sends SMTP mail via command line arguments.
#args: receiverName, receiverAddress, senderName, senderAddress, subject, message

import sys

def sendIt(receiverName, receiverAddress, senderName, senderAddress, subject, message):
    import getpass
    import smtplib
    message = """From: %s <%s>
To: %s <%s>
Subject: %s

%s""" % (receiverName, receiverAddress, senderName, senderAddress, subject, message)
    #(pixel_byte_string, mime_type) = pytracking.get_open_tracking_pixel()
    #print message

    try:
        #TODO: Send mail from arbitrary server
        smtpObj = smtplib.SMTP('clavin.adelphi.edu')
        smtpObj.sendmail(getpass.getuser()+'@compsci.adelphi.edu',receiverAddress,message)
        return 1
    except smtplib.SMTPException:
        return -1
    #import pytracking
    #(pixel_byte_string, mime_type) = pytracking.get_open_tracking_pixel()

def sendMany(recipients, recipientAddresses, senderName, senderAddress, subject, message):
    i = 0
    for receiver in recipients:
        sendIt(receiver, recipientAddresses[i], senderName, senderAddress, subject, message)
        i = i+1

def main():
    sendIt(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])

if __name__ == '__main__': main()
