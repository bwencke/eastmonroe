import cgi
import webapp2
from data import Candidate
from addCandidateForm import AddCandidateForm
from addCandidateForm import AddCandidateToDatastore
from addEventForm import AddEventForm
from addEventForm import AddEventToDatastore

from viewCandidates import ViewCandidates

from MainButtons import MainButtons

MAIN_PAGE_LOGIN = """\
<html>
    <head>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="stylesheets/css/bootstrap.min.css">
    
    <!-- Optional theme -->
    <link rel="stylesheet" href="stylesheets/css/bootstrap-theme.min.css">
    
    <!-- Latest compiled and minified JavaScript -->
    <script src="/stylesheets/js/bootstrap.min.js"></script>
    </head>
	<body>
		<form action="/main" method="post">
			<table>
                <tr>
                    <td>
                        Login:
                    </td>
                <td>
                        <select>
                                <option value="" disabled="disabled" selected="selected">-----</option>
                                <option value="ben">Ben</option>
                                <option value="joe">Joe</option>
                                <option value="paul">Paul</option>
                        </select>
                </td>
                </tr>
				<tr>
					<td></td>
                    <td>
					<input type="submit" value="Submit">
					</td>
				</tr>			
			</table>
		</form>
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
], debug=True)


