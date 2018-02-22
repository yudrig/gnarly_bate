#!/usr/bin/python

import smtplib
import sys

#This sends SMTP mail via command line arguments.
#args: senderName, senderAddress, recieverName, receiverAddress, subject, message

message = """From: %s <%s>
To: %s <%s>
Subject: %s

%s""" % (sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
print message

try:
	smtpObj = smtplib.SMTP('localhost')
	smtpObj.sendmail(sys.argv[2],sys.argv[4],message)
	sys.exit(0)
except smtplib.SMTPException:
	sys.exit(1)
