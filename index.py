import cgi
import webapp2
from data import AnotherClass

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

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.write(MAIN_PAGE_HTML)


class Submission(webapp2.RequestHandler):

	def post(self):
		self.response.write('<html><body>')
		name = cgi.escape(self.request.get('name'))
        	car = cgi.escape(self.request.get('car'))
		self.response.write('Hello, ' + name + '. We like your ' + car + '</body></html>')

application = webapp2.WSGIApplication([
	('/', MainPage),
	('/submit', Submission),
	('/anotherPage/', AnotherClass)
], debug=True)
