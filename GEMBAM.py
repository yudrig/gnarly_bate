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
        add_whole()
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
