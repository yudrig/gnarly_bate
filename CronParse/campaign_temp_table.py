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

    tracking_command = 'INSERT INTO tracking_campaigns(name,close,email) VALUES (\'%s\', current_timestamp + interval \'%s hour\',%s);' % (campaign_name,end,template)
    
    cur.execute(tracking_command)

    tracking_command = 'SELECT id FROM tracking_campaigns WHERE name = \'%s\';' % (campaign_name)

    cur.execute(tracking_command)
    campaign_id = cur.fetchall()

    command = """BEGIN TRANSACTION;
CREATE TABLE campaign_%s (
     userID int REFERENCES userList(id),
     opened boolean DEFAULT false,
     failed boolean DEFAULT false,
     dateSent timestamp without time zone default current_timestamp,
     date_opened timestamp without time zone default null,
     date_failed timestamp without time zone default null
);
""" % (campaign_id[0][0])

    for user in users:
        command = command + """INSERT INTO campaign_%s(userID) VALUES
    (%s)
;
""" % (campaign_id[0][0],user[0])

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
    cur.execute("select * from information_schema.tables where table_name=%s", ("campaign_"+str(campaignID),))
    if cur.rowcount:    
       cur.execute("""BEGIN TRANSACTION;
       UPDATE %s SET %s = TRUE, date_%s = current_timestamp WHERE userID = %s;
       COMMIT;""" % ( "campaign_"+str(campaignID) , incident , incident , user))


def end_campaign(campaignID):
    import CronParse.runCamp

    cur = psql_connect()

    cur.execute('SELECT userid,opened,failed FROM campaign_%s;',(campaignID,))
    users = cur.fetchall()

    for user in users:
        if user[1]:
            cur.execute('UPDATE userlist SET score = score + 1 WHERE id = %s;',(user[0]))
        if user[2]:
            cur.execute('UPDATE userlist SET score = score - 3 WHERE id = %s;',(user[0]))

    cur.execute("""BEGIN TRANSACTION;
    UPDATE tracking_campaigns SET active = 'f' WHERE id = %s;
    ALTER TABLE campaign_%s RENAME TO archived_%s;
    
    COMMIT;
    """,(campaignID,campaignID,campaignID))

    return 1 
