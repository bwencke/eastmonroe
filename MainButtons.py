import cgi
import webapp2

BUTTONS = """\
<html>
    <head>
    <link rel="stylesheet" href="/stylesheets/style.css">
    </head>
        <body>
            <div class="contentBox" style="width:500px;">
            <h1>What would you like to do?</h1>
            <a class="butt" href='/viewCandidates'>View Candidates</a>
            <a class="butt" href='/addCandidate'>Add Candidate</a>
            <a class="butt" href='/viewEvents'>View Events</a>
            <a class="butt" href='/addEvent'>Add Event</a>
            </div>
    </body>
</html>
"""

class MainButtons(webapp2.RequestHandler):
	
	def post(self):
		self.response.write(BUTTONS);
