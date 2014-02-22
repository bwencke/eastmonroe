import cgi
import webapp2

BUTTONS = """\
<html>
        <body>
            <button type="button" onClick="window.location='/viewCandidates'">View Candidates</button>
            <button type="button" onClick="window.location='/addCandidate'">Add Candidate</button>
            <button type="button" onClick="window.location='/viewEvents'">View Events</button>
            <button type="button" onClick="window.location='/addEvent'">Add Event</button>
        </body>
</html>
"""

class MainButtons(webapp2.RequestHandler):
	
	def post(self):
		self.response.write(BUTTONS);
