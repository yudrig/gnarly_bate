import campaign_temp_table
import datetime

cur = campaign_temp_table.psql_connect();

cur.execute("SELECT id,close FROM tracking_campaigns WHERE active='t'")

now = datetime.datetime.now()
camps = cur.fetchall()

for campID in camps:
	if campID[1].time() < now.time():
		#print campID[1]
		campaign_temp_table.end_campaign(campID[0])

