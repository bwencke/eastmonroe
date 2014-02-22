import cgi
import webapp2
from data import Candidate
from addCandidateForm import AddCandidateForm
from addCandidateForm import AddCandidateToDatastore

from editCandidate import EditCandidateForm
from editCandidate import EditCandidateToDatastore

from addEventForm import AddEventForm
from addEventForm import AddEventToDatastore

from viewCandidates import ViewCandidates
from viewEvents import ViewEvents

from MainButtons import MainButtons

MAIN_PAGE_LOGIN = """\
<html>
    <head>
        <link rel="stylesheet" href="/stylesheets/style.css">
    </head>
	<body>
		<form action="/main" method="post" id="login">
			<div class="contentBox">
            <h1>Blackwood Consulting</h1>
            <table>
                <tr>
                    <td>
                        User:
                    </td>
                <td>
                        <select>
                                <option value="" disabled="disabled" selected="selected">-----</option>
                                <option value="ben">Ben</option>
                                <option value="joe">Joe</option>
                                <option value="paul">Paul</option>
                        </select>
                </td>
                </tr></table>
					<a class="butt" href="javascript:void()" onClick="document.getElementById('login').submit()">Log In</a>			
		</form>
        </div>
	</body>
</html>
"""

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.write(MAIN_PAGE_LOGIN)


class Submission(webapp2.RequestHandler):

	def post(self):
		self.response.write('<html><body>')
        	rep = cgi.escape(self.request.get('rep'))


application = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/main', MainButtons),
        ('/submit', Submission),
        ('/addCandidate', AddCandidateForm),
        ('/persistCandidate', AddCandidateToDatastore),
        ('/addEvent', AddEventForm),
        ('/persistEvent', AddEventToDatastore),
        ('/viewCandidates', ViewCandidates),
        ('/viewEvents', ViewEvents),
        ('/editCandidate', EditCandidateForm),
        ('/persistExistingCandidate', EditCandidateToDatastore)
], debug=True)


