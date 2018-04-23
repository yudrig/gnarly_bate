#!/usr/bin/python

def campaign_management():

    #while loop makes sure input is valid before moving on
    sure = False
    while(not sure):
        sure = True
        selection = raw_input("""What would you like to do?
    1) Create campaign
    2) View current campaigns
    3) End a campaign prematurely
    4) Nevermind
    """)

        if selection == '1':
            create_campaign() 
        elif selection == '1':
            view_campaigns()
        elif selection == '3':
            end_campaign()
        elif selection == '4':
            import GEMBAM
            print "Oh okay"
            GEMBAM.welcome_message()
        else:
            print "Invalid input. Please try again"
            sure = False

def view_campaigns():
    import psycopg2
    import getpass
    print 'Campaigns in progress:'
    try:
        conn = psycopg2.connect("dbname = 'groupg' user = '%s'" % getpass.getuser())
    except:
        return -1
    cur = conn.cursor()

    campaigns = cur.execute('SELECT * FROM tracking_campaigns;')

    for campaign in campaigns:
        print campaign

    #TODO: analyticy stuff should probably go here

def create_campaign():
    import searchUsers
    import searchTemplates
    import campaign_temp_table
    campaign_name = raw_input("Campaign name: ")
    sure = False
    users = list()
    while(not sure):
        buffer_users = searchUsers.gather_inputs()        
        for buffer_user in buffer_users:
            #Check for duplicates at this stage
            add = True
            for user in users:
                if user[0] == buffer_user[0]:
                    add = False
            if add:
                users.append(buffer_user)

        i = 1
        print "This includes:"
        for user in users:
            print str(i) + '. ' + user[1] + ' ' + user[2] + ' at address ' + user[4]
            i = i + 1
        
        u_selection = raw_input("""What now?
1) Add another query
2) Continue
3) Cancel
""")

        if u_selection == '1':
            sure = False
        elif u_selection == '2':
            sure = True
        elif u_selection == '3':
			print "Okay then"
			return 0
        else:
            print "Invalid input. Please try again."
            sure = False

    template = None
    sure = False
    while(not sure):
        t_selection = raw_input("""What type of template would you like to use?
1) Manually entered
2) Generated from pieces
3) Saved template
4) Cancel
""")
        
        if t_selection == '1':
            #TODO: write this
            template = add_template()
        elif t_selection == '2':
            #TODO: also write this
            template = piecemeal_email()
        elif t_selection == '3':
            sure = True
            #List all templates and allow selection of one by ID
            all_templates = searchTemplates.searchTemplates(5,None)
            print 'Templates available:'
            ids = list()
            print 'ID\tSubject\tBody\tDifficulty'
            for choice in all_templates:
                ids.append(choice[0])
                print '%s\t%s\t%s\t%s' % (choice[0],choice[1],choice[2],choice[3])
            template = raw_input('ID of chosen template:')
            try:
                template = int(template)
            except ValueError:
                print 'Invalid input. Please try again.'
                sure = False
            if template not in ids:
                print 'Error: Not a template'
                sure = False
        elif t_selection == '4':
            print 'Oh okay'
            return 0
        else:
            print 'Invalid input. Please try again.'
            sure = False

    campaign_temp_table.table_creation(campaign_name,users,template)
