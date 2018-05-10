def makeHTML(inCamp, inUser,inBody):
	out = """<p><img src="http://panther.adelphi.edu/~ke21231/tracker.php?id=[CAMP_ID]_[USER_ID]" alt="" width="1" height="1" /></p>
	<p>[BODY_TEXT]</p>
	<p><a href="http://compsci.adelphi.edu/~jasonmassimino/?ID=[CAMP_ID]_[USER_ID]&amp;png">Click Here</a></p>
	"""


	out = out.replace("[CAMP_ID]",inCamp)
	out = out.replace("[USER_ID]",inUser)
	out = out.replace("[BODY_TEXT]", inBody)

	return out
