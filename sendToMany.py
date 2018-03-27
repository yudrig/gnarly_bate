#!usr/bin/python3

#using sendMail.py, sends a given email with a given send address, name, and subject to every user in the database

import sys
import psycopg2
import sendMail

def sendMany(senderName, senderAddress, subject, message):

    try:
        conn = psycopg2.connect("dbname = 'groupg' user = 'kevinwoll'")
    except:
        print "Unable to connect to DB!"
        return 0
    cur = conn.cursor()

    cur.execute("""SELECT * FROM userlist""")
    users = cur.fetchall()

    for user in users:
        fullName = user[1] + ' ' + user[2]
        sendMail.sendIt(fullName, user[4], senderName, senderAddress, subject, message)

def main():
    sendMany(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

if __name__ == '__main__': main()
