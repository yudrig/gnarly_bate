import sys

def fetch_email_body(queryType, query):
        import psycopg2
        
        try:
                conn = psycopg2.connect("dbname = 'groupg' user = 'thomasrhatigan'")
        except:
                print "Unable to connect!"
                return 0
        cur = conn.cursor()

        queryStart = 'SELECT * FROM templates WHERE ' + queryType + ' ' 
        cur.execute(queryStart + " = %s;", (query,))
        bodies = cur.fetchall()
        
        print bodies
        return 1

def main():
        queryType = raw_input("Please enter a query type: ")
        query = raw_input("Please enter a query")
	print str(queryType)

        fetch_email_body(str(queryType),str(query))

if __name__ == '__main__': main()       
