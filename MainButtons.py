import cgi
import webapp2

BUTTONS = """\
<html>
        <body>
            <button type="button" onClick="window.location='/viewcandidate'">View Candidates</button>
            <button type="button" onClick="window.location='/addcandidate'">Add Candidates</button>
            <button type="button" onClick="window.location='/viewevent'">View Events</button>
            <button type="button" onClick="window.location='/addevent'">Add Event</button>
        </body>
</html>
"""

class MainButtons(webapp2.RequestHandler):
	
	def post(self):
		self.response.write(BUTTONS);
