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
<<<<<<< HEAD
=======
        ('/addEvent', AddEventForm),
        ('/persistEvent', AddEventToDatastore),
        ('/viewCandidates', ViewCandidates),
>>>>>>> a27edcff6acdb340823fc53c9c3694d4224566cb
], debug=True)


