#!/usr/bin/python2

#creates the campaign tables based on parameters, which will be used to track emails receptions
#Takes the name of the campaign, the campaign end date
import sys
import psycopg2
import getpass

def table_updating(campaignID,userIDs,incident):
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        print "Unable to connect to DB!"
        return -1
    cur = conn.cursor() 
    cur.execute("select * from information_schema.tables where table_name=%s", ("campaign_"+campaignID,))
    if cur.rowcount:    
       cur.execute("""BEGIN TRANSACTION;
       UPDATE %s SET %s = TRUE, date_%s = current_timestamp WHERE userID = %s;
       COMMIT;""" % ( "campaign_"+campaignID , incident , incident , user))
