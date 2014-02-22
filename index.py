import cgi
import webapp2
from data import Candidate
from newCandidate import NewCandidate

MAIN_PAGE_HTML = """\
<html>
	<body>
		<form action="/submit" method="post">
			<table>
				<tr>
					<td>
						Name:
					</td>
					<td>
						<input type="text" name="name">
					</td>
				</tr>
                <tr>
                    <td>
                        Select Box:
                    </td>
                    <td>
                        <select name="car">
                            <option value="volvo">Volvo</option>
                            <option value="saab">Saab</option>
                            <option value="mercedes">Mercedes</option>
                            <option value="audi">Audi</option>
                        </select>
                    </td>
                </tr>
				<tr>
					<td></td>
                    <td>
					<input type="submit" value="SUBMIT"></div>
					</td>
				</tr>			
			</table>
		</form>
	</body>
</html>
"""

MAIN_PAGE_LOGIN = """\
<html>
	<body>
		<form action="/submit" method="post">
			<table>
                <tr>
                    <td>
                        Login:
                    </td>
                    <td>
                        <select name="rep">
                            <option value="Joe">Joe</option>
                            <option value="Paul">Paul</option>
                            <option value="Ben">Ben</option>
                        </select>
                    </td>
                </tr>
				<tr>
					<td></td>
                    <td>
					<input type="submit" value="SUBMIT">
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
	('/', MainPage),
	('/submit', Submission),
    ('/newCandidate', NewCandidate)
], debug=True)
