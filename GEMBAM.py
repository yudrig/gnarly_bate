#!/usr/bin/python2
#GNARLY EMPLOYEE MAIL BATEING APPLICATION MANAGER

def send_email():
    selection = raw_input("""How would you like to send emails?
1) Right now
2) On a schedule
3) Nevermind
""")
    import Sending.sending_methods

    if selection == '1':
        Sending.sending_methods.send_now()
    elif selection == '2':
        print 'Not yet implemented'
        #send_later()
    elif selection == '3':
        print 'Oh, alright'
        welcome_message()
    else:
        print 'Invalid input. Please try again.'
        send_email()

def email_campaign():
    import Campaign.campaign_management
    Campaign.campaign_management.campaign_management()

def add_user():
    import psycopg2
    import getpass
    
    first_name = raw_input('What is the first name of the user you would like to add?')
    last_name = raw_input('What is the last name of the user you would like to add?')
    email = raw_input('What is the email address of the user you would like to add?')

    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        print 'Unable to connect to the DB!'
        return -1
    cur = conn.cursor()

    cur.execute("INSERT INTO userlist(firstname,lastname,email) VALUES (%s,%s,%s);",(first_name,last_name,email))
    print "User added!"
    welcome_message()

def add_email():
    #TODO: Make work
    import psycopg2
    import getpass
    import Generation.testGenerate

    selection = raw_input("""Add Email by:
1: Random Generation
2: Manual Input
3: Nevermind
""")

    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        print 'Unable to connect to the DB!'
        return -1
    cur = conn.cursor()
    file = open("Generation/txt/Suffix.txt")
    fileLines = file.read().splitlines()
    
    if selection == '1':
        choices = "1) Random\n"
        i=0
        for line in fileLines:
            if (i > 0):
                choices += str(i+1) + ") " + line[1:] + "\n"
	    i+=1

        selection2 = int(raw_input(choices));
	
        if selection2 < i or selection2 > 0:
           suffix = fileLines[selection2-1][1:]
        else:
            suffix = ""
        hold = Generation.testGenerate.genEmail("[NAME]",suffix)
        subject = hold[0]
        body = hold [1]
    elif selection == '2':
        subject = raw_input("Subject:")
        body = raw_input("Body:")
    elif selection == '3':
        welcome_message()
    else:
        print "Try Again"
        add_email()

    print subject
    print body
    cur.execute("INSERT INTO templates(subject,body,difficulty) VALUES (%s,%s,%s);",(subject,body,"3"))


def user_info():
    selection = raw_input("""Would you like to:
1) Add a new user
2) Update a user
3) Delete a user
4) Search users
5) Nevermind
""")

    if selction == '1':
        add_user()
    elif selection == '2':
        update_user()
    elif selection == '3':
        delete_user()
    elif selection == '4':
        search_users()
    elif selection == '5':
        print 'Oh, alright'
        welcome_message()
    else:
        print 'Invalid input. Please try again.'
        user_info()

def email_info():
    selection = raw_input("""Would you like to:
1) Add whole emails
2) Add email fragments
3) Modify whole emails
4) Modify fragments
4) Remove whole emails
5) Remove fragments
6) Nevermind
""")
    
    if selection == '1':
        add_email()
    elif selection == '2':
        add_fragment()
    elif selection == '3':
        modify_whole()
    elif selection == '4':
        modify_fragment()
    elif selection == '5':
        remove_whole()
    elif selection == '6':
        remove_fragment()
    else:
        print 'Invalid input. Please try again.'
        email_info()

def analyze_results():
    print 'Not yet implemented'
    welcome_message()

def welcome_message():
    selection = raw_input("""Welcome to GEMBAM, the Gnarly Employee Bateing Application Manager! 
1) Send emails
2) Manage email campaigns
3) Manage user information
4) Manage email information
5) Analyze results
6) None
Please enter your selection:
""")

    if selection == '1':
        send_email()
    elif selection == '2':
        email_campaign()
    elif selection == '3':
        user_info()
    elif selection == '4':
        email_info()
    elif selection == '5':
        analyze_results()
    elif selection == '6':
        print 'Goodbye!'
        return 0
    else:
        print 'Invalid input. Please try again.'
        welcome_message()

def main():
    welcome_message()
if __name__=='__main__':main()
