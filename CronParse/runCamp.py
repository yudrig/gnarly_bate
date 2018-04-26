import campaign_temp_table
import ReturnParse

pix = []
url = []

pix = ReturnParse.getPixelTrack()
url = ReturnParse.getURLTrack()

if pix is not None:
	for p in pix:
		mail = p[0]
		user = p[1]
		table_updating.table_updating(mail,user,"opened")
if url is not None:
	for u in url:
		mail = u[0]
		user = u[1]
		table_updating.table_updating(mail,user,"failed")

