#!usr/bin/python

import sys

def searchUsers(queryCategory,search_condition,operator):
    import psycopg2
    import getpass
    
    #Connecting to database
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        return -1
    cur = conn.cursor()

    #Dictionary of columns to parameterize queries
    #TODO: Make this a little more elegant
    column_dictionary = {1:'SELECT * FROM userlist WHERE ID ',2:'SELECT * FROM userlist WHERE firstname',3:'SELECT * FROM userlist WHERE lastname',4:'SELECT * FROM userlist WHERE score',5:'SELECT * FROM userlist WHERE email', 6:'SELECT * FROM userlist'}
    #Dictionary of operators
    operator_dictionary = {1:'>', 2:'>=', 3:'=', 4:'<=', 5:'<', 6:'!='}

    #Building query from dictionary and parameters
    if queryCategory == 6:
        query = column_dictionary.get(queryCategory)
    else:
        try:
            query = column_dictionary.get(queryCategory) + operator_dictionary.get(operator)
        #If get() returns None, end in error. Putting this here simplifies error catching to one stage rather than the four that would be necessary if it were done preemptively
        except TypeError:
		    return -2

    #Executing query
    if search_condition == None:
        cur.execute(query)
    else:
        cur.execute(query + ' %s',(search_condition,))
    users = cur.fetchall()

    return users

#Main method if run alone
#Gathers inputs manually
def gather_inputs():
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
                condition = int(condition)
            except ValueError:
                print 'ERROR: Invalid input ' + condition
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
    
    return searchUsers(queryType,condition,comparison)

def main():
    print gather_inputs()

if __name__ == '__main__': main()
