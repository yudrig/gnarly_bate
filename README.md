# gnarly_bate
Phishing Training Platform
Kevin Woll, Jason Massimino, Thomas Rhatigan (ConnCorp)

Phishing Training Platform developed by Conncorp. A user friendly spam email training system for use in businesses created for a school project. This program creates, sends, and tracks fake spam emails for the purpose of training employees to recognize and in the future avoid falling victim to phishing email scams.

Build Version 1.6

Install
Visit https://github.com/yudrig/gnarly_bate and download the files located there run GEMBAM and first time step


The program is robust and user friendly for any level of technical use. High level of detailed choices for users to make along. Each of these options are calls to other functions. Installation of CronTab and libraries Psycopg, Smtplib, PIL or Pillow, and Getpass. Other libraries used should already be installed with python installation. Two websites are also needed along with a server.One website for the hosting of the pixels that will be inserted into the emails. The second website will be the debrief site letting the user know that they have be phished. 
Manage email campaigns
Brings you to Campaign management which is another menu that is the user interface for campaigns which is were the options for creation, viewing and ending of a campaign are available through interaction with Crontab.
Manage user information
Brings you to User interface that allows User alteration. (In progress)
Manage email information
Brings you to User interface that allows email alteration. (In progress)
First time setup 
Setup up the Database with the expected parameters of the tables. Will alert you if there is an error with database configuration. Schema creation happens within here. Calls the setup function that needs sets the database name and sets the username to the current user. This is done with getpass.getuser(). 
Expected Input: “schema.psql” as schema for the tables to be set up 
Expected Output: Creation of tables needed for database.
Manage Email Campaigns

Create Campaign
Server needs to be set up for this option. The option interacts with Campaign branch and Sending branch.Gather the users from the database with the searchUsers from the Sending branch. Also list all the users for this campaign. A temporary table is created with campaign_temp_tables for comparison at the end of the campaign. Prompt for the next set of actions to take included adding another query or just continuing to next step of campaign creation. Adding another query repeats the previous section to add another criteria to the users to be tested.  Saved template accesses the already stored templates (Options 1 and 2 are In progress). Presents the template available then prompts users to choose a template based on ID. Final step is to set the amount of hours you would want the campaign to last. 
Expects Input: Campaign.campaign_temp_table.table_creation(campaign_name,users,template,end) 
Expected Output: 'Campaign successfully created!'
View current Campaigns 
Server needs to be set up for this option. Connection is established between the database and the user. This will view the active campaigns in the format of name of campaign, ID of campaign, campaign started and campaign end date. The start is set upon creation of campaign and end time is set by user. The start and finish are checked by crontab. 
Expected Input:Choosing the option 
Expected Output: List of the campaigns that are defined as active.
End a Campaign Prematurely 
Server needs to be set up for this option. Prompts user for the ID of the campaign that you would want to end. If campaign is not active then error message appears else Campaign is ended success message appears. 
Expects Input:Campaign.campaign_temp_table.end_campaign(selection)
Expected Output:”Campaign ended successfully!”
Tracking Components/Cron Parse 

Image Creation
The point of the image creation function is to create images that can be used to track if an email was viewed. This is accomplished by viewing the server logs and a specific GET request. The function that performs the log parsing is ReturnParse. 
Expected Input: imageCreation expects an EmailID and an array of userIDs
Expected Output:Creates an image and names the pixel by the convention pix_(EmailID)_(user[0])

RunCamp
Interacts with campaign_temp_tables and ReturnParse. The function that does the comparison between the server logs and the database. If the pix and url arrays are values found within the database then the update is made to the table. If the pixel has been viewed then it will be updated by looping through the array of arrays that was set up by ReturnParse thus pulling the Email and user IDs are pulled from the string.
Expected Input: Array of Pix and Array of Url from the function ReturnParse.getPixelTrack and ReturnParse.getURLTrack Expected Output: Either an update to the table_updateing to the pix and url arrays.
ReturnParse
ReturnParse needs to have access to the server logs and two active web sites on the server. ReturnParse looks for specific strings of text within the logs. This happens by looking in each line of args.log_file then checks with an if condition for String of “website” and “pix_” and “?ID” for the respective if statements for pulling the information. The are two empty arrays pix and url that are used to hold the ID numbers.  Example of possible log file located within code and website.
Expected Input: Server logs which is called ‘log_file’
Expected Output: Returns the EmailID and User ID
Campaign_temp_table
Connects to the database to create campaigns by logging the campaign_name, users, template, end for the table creation. This creates a table for the campaign and commits to the database so it can be monitored by crontab and tracked with the Check End. Sets up table for campaign tracking with timestamps of when tracking functions are called and checked.
Expected Input:Campaign name, Users from database, template from database and end date from user
Expected Output:Creation of the campaign with the passed parameters

Table_updating updates the table with the tracking information from ReturnParse. 
Expected Input: campaignID, userID,incident  to know which campaign to update with which user should be updated by the incident which is the PIX tracking update and the URL tracking update
Expected Output:The user statuses for Pix and Url are updated to reflect “opened” and “failed” for the user with the exact ID

End_campaign preforms a final check with table_updating that does the final score altering
Expected Input: CampaignID is needed to end a campaign
Expected Output: Score UPDATE  happens based on either “Opened” or “failed” to the user[0] by a for loop number of users

Check End
Connects to the Database and Checks the campaign IDs to see if they have reached the end time. This includes campaign_temp_table and datetime. All tracking_campaigns are pulled where that are set to active then compared to the current time. This is checked by crontab every minute as per our recommendation so high level of accuracy can be maintained. 

Make Tables
Provides the PSQL code for table creation with the correct values and types.
Sending

Search Users
Connects to the database and allows the user to set up search parameters for selecting users data. The table values that can be queried are ID , FirstName, Lastname, score, and all categories. Comparisons can be done with next step in which you can select either greater than, greater than or equal to, equal to, less than or equal to or not equal to the selected criteria. This covers all conditions that a user may want to search for.Users are expected to know which information they would want to gather.
Expected Input:User input for the option which is queryCategory, search_condition and operator
Expected Output: Return of the values of the userList where the conditions are met

Search Templates
Connects to the database and allows the user to set up search parameters for selecting template data. The table values that can be queried are ID , subject, body, difficulty and all categories. Users are expected to know which templates they would want to gather.

randLine
Used in random email generation. Opens a preset file and pulls a random line that will be used as a header for the email. More headers can be added by following the similar format of the text document.Expected Input: A file is need with the format of a header for an email
Expected Output: A line from the file is randomly returned

Fetchbody
Connects to the database and prompts user for queryType and the query. queryType is the value of the body and query is exact text the user is looking for.
Expected Input: User prompt for the value that will be queried and the query 
Expected Output: Returns the queried results

Unresolved issues:
1.Does not send emails on timer campaign development took precedence over this function and this could not be 
2.Currently requires a website that needs “jasonmassimino” and the name of the different website has to be “thomasrhatigan” 
3.Does not automatically configure the crontab
	CronPasrse/runCamp.py/ needs to be added to a crontab manually 
