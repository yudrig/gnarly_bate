#!usr/bin/python

#Temporary fix (hopefully). Should be able to send via database using both no conditions and a query but python polymorphism is hard so this file will allow sending with query while sendToMany will send only with database
import sys

def sendViaDatabase(queryType,query,senderName,senderAddress,subject,message):
    import psycopg2
    import sendMail

    try:
        conn = psycopg2.connect("dbname = 'groupg' user = 'kevinwoll'")
    except:
        print "Unable to connect to DB!"
        return 0
    cur = conn.cursor()
    
    #TODO: This query shit is driving me crazy. The query needs to recognize the 'query' parameter as a string, not a column. Input also needs to be scrubbed (; DROP TABLE userlist)

    #users =  cur.execute("SELECT * FROM userlist " +  query + ";")
    queryStart = 'SELECT * FROM userlist WHERE ' + queryType + ' ' + 
    cur.execute(queryStart + " = %s;", (query,))
    users = cur.fetchall()

    if users != None:
        for user in users:
            fullName = user[1] + ' ' + user[2]
            sendMail.sendIt(fullName, user[4], senderName, senderAddress, subject, message)
    else:
        return 0

def main():
    queryType = input("""Enter 1 to match """)
    query = input();
    senderName = input('Full Name of Sender: ')
    
    sendViaDatabase(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])

if __name__ == '__main__': main()
