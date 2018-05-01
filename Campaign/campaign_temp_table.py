#!/usr/bin/python2

#creates the campaign tables based on parameters, which will be used to track emails receptions
#Takes the name of the campaign, the campaign end date
import sys
import psycopg2
import getpass

def psql_connect():
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        if __name__ == '__main__': print "Unable to connect to DB!"
        return -1
    return conn.cursor()

def table_creation(campaign_name,users,template,end):
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        print "Unable to connect to DB!"
        return -1
    cur = conn.cursor()
    
    command = """BEGIN TRANSACTION;
CREATE TABLE campaign_%s (
     userID int REFERENCES userList(id),
     opened boolean DEFAULT false,
     failed boolean DEFAULT false,
     dateSent timestamp without time zone default current_timestamp,
     date_opened timestamp without time zone default null,
     date_failed timestamp without time zone default null
);
""" % (campaign_name)

    for user in users:
        command = command + """INSERT INTO campaign_%s(userID) VALUES
    (%s)
;
""" % (campaign_name,user[0])

    command = command + 'INSERT INTO tracking_campaigns(name,close,email) VALUES (\'%s\', current_timestamp + interval \'%s hour\',%s);' % (campaign_name,end,template)

    command = command + 'COMMIT;'
    
    #print command

    cur.execute(command)

    return 1

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


def end_campaign(campaignID):
    cur = psql_connect()
    
    #Final log checks before close
    table_updating(campaignID,users,'opened')
    table_updating(campaignID,users,'failed')

    cur.execute('SELECT name FROM tracking_campaigns WHERE id = %s',(campaignID,))
    campaignName = cur.fetchone()

    cur.execute('SELECT userID FROM campaign_%s',(campaignID,))
    users = cur.fetchall()
    
    cur.execute('SELECT userid,opened,failed FROM campaign_%s;',(campaignName))

    for user in users:
        if user[1]:
            cur.execute('UPDATE userlist SET score = score + 1 WHERE id = %s;',(user[0]))
        if user[2]:
            cur.execute('UPDATE userlist SET score = score - 3 WHERE id = %s;',(user[0]))

    cur.execute("""BEGIN TRANSACTION;
    UPDATE tracking_campaigns SET active = 'f' WHERE id = %s;
    ALTER TABLE campaign_%s RENAME TO archived_%s;
    
    COMMIT;
    """,(campaignID,campaignName,campaignName))

    return 1 
