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
                                                <input type="radio" name="sex" value="male">Male<br>
                                        </td>
                                        <td>
                                                <input type="radio" name="sex" value="female">Female
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
                                        <select>
                                        <option value="" disabled="disabled" selected="selected">-----</option>
                                        <option value="purdue">Purdue University</option>
                                        <option value="illinois">University of Illinois</option>
                                        <option value="depauw">Depauw University</option>
                                        </select>
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Major:
                                    </td>
                                    <td>
                                        <select>
                                        <option value="" disabled="disabled" selected="selected">-----</option>
                                        <option value="cs">Computer Science</option>
                                        <option value="engr">Engineering</option>
                                        <option value="comm">Communication</option>
                                        </select>
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        GPA:
                                    </td>
                                    <td>
                                        <input type="text" name="gpa">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Background:
                                    </td>
                                    <td>
                                        <input type="background" name="background">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Interests:
                                    </td>
                                    <td>
                                        <input type="interests" name="interests">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Notes:
                                    </td>
                                    <td>
                                        <input type="notes" name="notes">
                                    </td>
				</tr>
			</table>

                        <tr>
                                <td>
                                        <label for="file">Upload a Resume</label>
                                        <input type="file" name="resume" id="resume"><br>  
                                </td>
                        </tr>

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
        candidate.sex = self.request.get('sex')
        candidate.name = self.request.get('name')
        candidate.email = self.request.get('email')
        candidate.university = self.request.get('university')
        candidate.major = self.request.get('major')
        candidate.gpa = self.request.get('gpa')
        candidate.background = self.request.get('background')
        candidate.resume = self.request.get('resume')
        candidate.resume = self.request.get('interests')
        candidate.resume = self.request.get('notes')
        candidate.put()

        self.response.write("""<html><body><table><tr><td><button type="button" onClick="window.location='/main'">Main Menu</button></td><tr/></table></html></body>""")

