import cgi
import webapp2
from data import Candidate
from addCandidateForm import AddCandidateForm
from addCandidateForm import AddCandidateToDatastore

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
                        <option value="" disabled="disabled" selected="selected">select your name</option>
                        <option value="Joe">Joe</option>
                        <option value="Paul">Paul</option>
                        <option value="Ben">Ben</option>
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
<<<<<<< HEAD
        ('/submit', Submission),
        ('/addCandidate', AddCandidateForm),
        ('/persistCandidate', AddCandidateToDatastore),
=======
	('/submit', Submission),
    ('/addCandidate', AddCandidateForm),
    ('/persistCandidate', AddCandidateToDatastore),
    ('/viewCandidates', ViewCandidates)
>>>>>>> dca283c1693b16ae285cb80917703af6f6d73eeb
], debug=True)


