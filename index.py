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
<<<<<<< HEAD
					<input type="submit" value="Submit"></div>
=======
					<input type="submit" value="SUBMIT">
>>>>>>> 6e27e94064204e7c8176ca3494d56b805f107f88
					</td>
				</tr>			
			</table>
		</form>
        <form action="/newCandidate" method="post">
            <input type="text" name="candidateName" value="Dennis Rodman">
            <input type="submit" value="SUBMIT">
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
<<<<<<< HEAD
        ('/', MainPage),
        ('/main', MainButtons)
=======
	('/', MainPage),
	('/submit', Submission),
    ('/addCandidate', AddCandidateForm),
    ('/persistCandidate', AddCandidateToDatastore),
    ('/viewCandidates', ViewCandidates)
], debug=True)


