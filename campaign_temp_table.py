#!/usr/bin/python3

#This creates the campaign tables based on parameters, which will be used to track emails receptions
#Takes the name of the campaign, the campaign end date
import sys

def table_creation(campaign_name,users,template):
    import psycopg2
    import getpass
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        if __name__ == '__main__': print "Unable to connect to DB!"
        return -1
    cur = conn.cursor()
    
    command = """BEGIN TRANSACTION;
CREATE TABLE campaign_%s (
     userID int REFERENCES userList(id),
     template int REFERENCES templates(id),
     opened boolean DEFAULT false,
     failed boolean DEFAULT false,
     dateSent timestamp without time zone default current_timestamp,
     dateOpened timestamp without time zone default null,
     dateFailed timestamp without time zone default null
);
""" % (campaign_name)

    for user in users:
        command = command + """INSERT INTO campaign_%s(userID,template) VALUES
    (%s,%s)
;
""" % (campaign_name,user[0],template)

	command = command + 'INSERT INTO tracking_campaigns(name) VALUES (%s);' % campaign_name

    command = command + 'COMMIT;'
    
    #print command

    cur.execute(command)

    return 1
