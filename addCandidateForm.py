import cgi
import webapp2
from data import Candidate
from MainButtons import MainButtons
from data import Event

ADD_CANDIDATE_FORM_1 = """\
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
    <input style="width:25px; height:auto;" type="radio" name="sex" value="male">Male
    <input style="width:25px; height:auto;" type="radio" name="sex" value="female">Female
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
                                        <select name="university">
                                        <option value="" disabled="disabled" selected="selected">-----</option>
                                        <option value="Purdue University">Purdue University</option>
                                        <option value="University of Illinois">University of Illinois</option>
                                        <option value="Depauw University">Depauw University</option>
                                        </select>
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Major:
                                    </td>
                                    <td>
                                        <select name="major">
                                        <option value="" disabled="disabled" selected="selected">-----</option>
                                        <option value="Computer Science">Computer Science</option>
                                        <option value="Engineering">Engineering</option>
                                        <option value="Communication">Communication</option>
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
				<tr>
				    <td>
                                        Initial Rating:
                                    </td>
                                    <td>
                                        <input type="range" name="score" min="1" max="10">
                                    </td>
				<tr>
                                    <td style="padding-bottom:20px;">
                                        Status:
                                    </td>
                                    <td style="padding-bottom:20px;">
                                        <select name="status">
                                        <option value="" disabled="disabled" selected="selected">-----</option>
                                        <option value="Pre-Interview">Pre-Interview</option>
                                        <option value="Offer Pending">Offer Pending</option>
                                        <option value="Offer Accepted">Offer Accepted</option>
                                        <option value="Offer Rejected">Offer Rejected</option>
                                        <option value="Decline to Move Forward">Decline to Move Forward</option>
                                        </select>
                                    </td>
				</tr>"""


ADD_CANDIDATE_FORM_2 =          """<tr>
                                        <td style="border-top:1px solid black; padding-top:20px;">Upload a Resume</td>
                                        <td style="border-top:1px solid black; padding-top:20px;"><input style="border:none" type="file" name="resume" id="resume"></td> 

                    </tr></table>
    <a class="butt" href="javascript:void()" onClick="document.getElementById('addCandidate').submit()">Submit</a>
                        
		</form></div>
	</body>
</html>
"""

class AddCandidateForm(webapp2.RequestHandler):

	def get(self):
		self.response.write(ADD_CANDIDATE_FORM_1)
		events = Event.query().fetch(20)
		#self.response.out.write('<tr>')
                for event in events:
                    self.response.out.write('<tr><td></td><td><input style="width:15px; height:15px" type="checkbox" name="event" value=%s>%s</td></tr>' %
                                            (event.name,
                                            event.name))
                #self.response.out.write('</tr>')
		self.response.write(ADD_CANDIDATE_FORM_2)


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
        candidate.interests = self.request.get('interests')
        candidate.notes = self.request.get('notes')
        candidate.status = self.request.get('status')
        candidate.put()

        self.response.write("""<html><body><table><tr><td><form action="/main" method="post"><input type="submit" value="Main Menu"></form></td></tr></table></html></body>""")










