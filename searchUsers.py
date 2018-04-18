#!usr/bin/python

import sys

def searchUsers(queryType,condition,comparison):
    import psycopg2
    import sendMail
    
    #Connecting to database
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = 'kevinwoll'")
    except:
        #Only print error if run as main, alway return -1 on failure
        if __name__ == '__main__': print "Unable to connect to DB!"
        return -1
    cur = conn.cursor()

    #Dictionary of columns to parameterize queries
    #TODO: Make this a little more elegant
    column_dictionary = {1:'SELECT * FROM userlist WHERE ID ',2:'SELECT * FROM userlist WHERE firstname',3:'SELECT * FROM userlist WHERE lastname',4:'SELECT * FROM userlist WHERE score',5:'SELECT * FROM userlist WHERE email', 6:'SELECT * FROM userlist'}
    #Dictionary of comparisons
    comparison_dictionary = {1:'>', 2:'>=', 3:'=', 4:'<=', 5:'<', 6:'!='}

    #Building query from dictionary and parameters
    if queryType == 6:
        query = column_dictionary.get(queryType)
    else:
        try:
            query = column_dictionary.get(queryType) + comparison_dictionary.get(comparison)
        #If get() returns None, end in error. Putting this here simplifies error catching to one stage rather than the four that would be necessary if it were done preemptively
        except TypeError:
            if __name__ == '__main__':
                print 'ERROR: Out of range'
                return -1

    #Executing query
    if condition == None:
        cur.execute(query)
    else:
        cur.execute(query + ' %s',(condition,))
    users = cur.fetchall()#When this is changed to fetchone()you will only grab the first value which is the ID in which we need

    if(__name__ == '__main__'):
        print users
    else:
        return users

#Main method if run alone
#Gathers inputs manually
def main():
    queryType = raw_input("""Select category:
1 to search ID
2 to search first name
3 to search last name
4 to search score
5 to search email address
6 to send without category 
""")
    try:
        queryType = int(queryType)
    except ValueError:
        print 'ERROR: Invalid input'
        return -1

    #If searching an int field, change input to int and get comparison
    comparison = 3
    condition = None
    if queryType != 6:
        condition = raw_input("Condition: ")
        if queryType == 1 or queryType == 4:
            try:
                condtiion = int(condition)
            except ValueError:
                print 'ERROR: Invalid input ' + query
                return -1

            comparison = raw_input("""Select comparison type:
1:>
2:>=
3:=
4:<=
5:<
6:!=
""")
            try:
                comparison = int(comparison) 
            except ValueError:
                print 'ERROR: Invalid input'

    searchUsers(queryType,condition,comparison)

if __name__ == '__main__': main()
