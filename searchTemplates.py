#!usr/bin/python

import sys

def searchTemplates(queryType,condition):
    import psycopg2
    
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
    column_dictionary = {1:'SELECT * FROM templates WHERE id',2:'SELECT * FROM templates WHERE subject',3:'SELECT * FROM templates WHERE body',4:'SELECT * FROM templates WHERE difficulty'}

    #Building query from dictionary and parameters
    try:
        query = column_dictionary.get(queryType) + '='
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
    template = cur.fetchall()

    if(__name__ == '__main__'):
        print template
    else:
        return template

#Main method if run alone
#Gathers inputs manually
def main():
    queryType = raw_input("""Select category:
1 to search ID
2 to search subject
3 to search body
4 to search difficulty
""")
    try:
        queryType = int(queryType)
    except ValueError:
        print 'ERROR: Invalid input'
        return -1
    
    condition = raw_input("Condition: ")

    searchTemplates(queryType,condition)

if __name__ == '__main__': main()
