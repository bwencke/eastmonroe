import cgi
import webapp2
from data import Candidate

ADD_CANDIDATE_FORM = """\
<html>
    <head>
     <link rel="stylesheet" href="/stylesheets/style.css">
    </head>
	<body><div class = "contentBox">
		<form action="/persistCandidate" method="post" name="addCandidate">
			<h1>Add Candidate</h1>
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
				<tr>
                                    <td>
                                        Background:
                                    </td>
                                    <td>
                                        <input type="<textarea rows="4" cols="50"></textArea>" name="background">
                                    </td>
				</tr>
			</table>
            <a class="butt" onClick="document.getElementById('addCandidate').submit()">Submit</a>
		</form></div>
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
        candidate.background = self.request.get('background')
        candidate.put()

