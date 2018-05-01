#!usr/bin/python

import sys

def searchTemplates(queryType,condition):
    import psycopg2
    import getpass
    
    #Connecting to database
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        return -2
    cur = conn.cursor()

    #Dictionary of columns to parameterize queries
    #TODO: Make this a little more elegant
    column_dictionary = {1:'SELECT * FROM templates WHERE id',2:'SELECT * FROM templates WHERE subject',3:'SELECT * FROM templates WHERE body',4:'SELECT * FROM templates WHERE difficulty',5:'SELECT * FROM templates'}

    #Building query from dictionary and parameters
    try:
        query = column_dictionary.get(queryType)
        if queryType is not 5:
            query = query + '='
    #If get() returns None, end in error. Putting this here simplifies error catching to one stage rather than the four that would be necessary if it were done preemptively
    except TypeError:
        return -1

    #Executing query
    if condition == None:
        cur.execute(query)
    else:
        cur.execute(query + ' %s',(condition,))
    template = cur.fetchall()

    return template

#Gathers inputs manually
def gather_inputs():
    queryType = raw_input("""Select category:
1 to search ID
2 to search subject
3 to search body
4 to search difficulty
5 to fetch all
""")
    try:
        queryType = int(queryType)
    except ValueError:
        print 'ERROR: Invalid input'
        return -1
    
    condition = None
    if queryType is not 5:
        condition = raw_input("Condition: ")

    return searchTemplates(queryType,condition)

def main():
    print gather_inputs()

if __name__ == '__main__': main()
