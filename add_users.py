import getpass
import psycopg2
import campaign_temp_table

users = ['Alexus', 'Bowers','Adan', 'Roy','Norah', 'Dunn','Scarlet', 'Joseph','Joyce', 'Thornton','Aniyah', 'Mccarty','Brody', 'Henry','Sidney', 'Becker','Julie', 'Oconnell','Carley', 'Pena','Kasey', 'Kidd','Kaiden', 'Dorsey','Mariyah', 'Banks','Kash', 'Salazar','Brennan', 'Monroe','Daniela', 'Mckinney','Anabelle', 'Chen','Bryant', 'Bishop','Jayvon', 'Burgess','Leilani', 'Benson']

try:
    conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
except:
    if __name__ == '__main__': print "Unable to connect to DB!"

cur = conn.cursor()

command = "INSERT INTO userlist(firstname,lastname,email) VALUES"
x = 0
while x < len(users):
    command = command + "(\'%s\',\'%s\',\'%s\')," % (users[x],users[x+1], users[x][0]+users[x+1]+'@conncorp.adelphi.edu')
    x = x+2

print command
