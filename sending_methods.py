def send_now():
    import searchUsers
    import sendMail

    sure = False
    while(not sure):
        users = searchUsers.main()
        print "Users found: "
        for user in users:
            print user[1] + ' ' + user[2] + ' at address ' + user[4]

            acceptable = raw_input("Is this acceptable? (y or n)")
        if (acceptable == 'n'):
            selection = raw_input ("""Would you like to 
1) search again
2) quit
""")
            if (selection == '1'):
                send_now()
            if (selection == '2'):
                print "Goodbye"
                return
        elif (acceptable == 'y'):
            sure = True
        else:
            print "Invalid input, please try again"

    senderName = raw_input("Sender Name: ")
    senderAddress = raw_input("Sender Address: ")
    subject = raw_input("Subject: ")
    message = raw_input("Message: ")

    for user in users:
        sendIt(user[1] + ' ' + user[2], user[4], senderName, senderAddress, subject, message)
