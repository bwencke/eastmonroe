import cgi
import webapp2
from data import Candidate

ADD_CANDIDATE_FORM = """\
<html>
	<body>
		<form action="/persistCandidate" method="post">
			<table>
				<tr>
					<td>
						New Candidate:
					</td>
				</tr>
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
                                        Email:
                                    </td>
                                    <td>
                                        <input type="email" name="email">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        University:
                                    </td>
                                    <td>
                                        <input type="text" name="university">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Major:
                                    </td>
                                    <td>
                                        <input type="text" name="major">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        GPA:
                                    </td>
                                    <td>
                                        <input type="number" name="gpa">
                                    </td>
				</tr>
			</table>
            <input type="submit" value="Submit">
		</form>
	</body>
</html>
"""

class AddCandidateForm(webapp2.RequestHandler):

	def get(self):
		self.response.write(ADD_CANDIDATE_FORM)


class AddCandidateToDatastore(webapp2.RequestHandler):
    
    def post(self):
        self.response.write("Candidate Added.")
        candidate = Candidate()
        candidate.name = self.request.get('name')
        candidate.email = self.request.get('email')
        candidate.university = self.request.get('university')
        candidate.major = self.request.get('major')
        candidate.gpa = self.request.get('gpa')
        candidate.put()

