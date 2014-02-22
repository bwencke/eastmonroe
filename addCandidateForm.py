import cgi
import webapp2
from data import Candidate
from MainButtons import MainButtons

ADD_CANDIDATE_FORM = """\
<html>
    <head>
     <link rel="stylesheet" href="/stylesheets/style.css">
    </head>
	<body><div class = "contentBox">
		<form action="/persistCandidate" method="post" id="addCandidate">
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
        Gender:
    </td>
    <td>
    <input style="width:25px;" type="radio" name="sex" value="male">Male<br>
    <input style="width:25px;" type="radio" name="sex" value="female">Female
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
                                    <td style="padding-bottom:20px;">
                                        Notes:
                                    </td>
                                    <td style="padding-bottom:20px;">
                                        <input type="notes" name="notes">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Status:
                                    </td>
                                    <td>
                                        <select>
                                        <option value="" disabled="disabled" selected="selected">-----</option>
                                        <option value="Pre-Interview">Pre-Interview</option>
                                        <option value="Offer Pending">Offer Pending</option>
                                        <option value="Offer Accepted">Offer Accepted</option>
                                        <option value="Offer Rejected">Offer Rejected</option>
                                        <option value="Decline to Move Forward">Decline to Move Forward</option>
                                        </select>
                                    </td>
				</tr>
                        <tr>
                                        <td style="border-top:1px solid black; padding-top:20px;">Upload a Resume</td>
                                        <td style="border-top:1px solid black; padding-top:20px;"><input type="file" name="resume" id="resume"></td> 

                    </tr></table>
    <a class="butt" href="javascript:void()" onClick="document.getElementById('addCandidate').submit()">Submit</a>
                        
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

        self.response.write("""<html><body><table><tr><td><form action="/main" method="post"><input type="submit" value="Main Menu"></form></td></tr></table></html></body>""")

