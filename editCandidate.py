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
    <h1>Edit Candidate</h1>
    <table>
    <tr>
    <td>
    Name:
    </td>
    <td>
    <input type="text" name="name" value="%s">
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
    <input type="email" name="email" value="%s">
    </td>
    </tr>
    <tr>
    <td>
    University:
    </td>
    <td>
    <select name="university">
    <option value="" disabled="disabled" selected="selected">-----</option>
    <option %svalue="purdue">Purdue University</option>
    <option %svalue="illinois">University of Illinois</option>
    <option %svalue="depauw">Depauw University</option>
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
    <option %svalue="cs">Computer Science</option>
    <option %svalue="engr">Engineering</option>
    <option %svalue="comm">Communication</option>
    </select>
    </td>
    </tr>
    <tr>
    <td>
    GPA:
    </td>
    <td>
    <input type="text" name="gpa" value="%s">
    </td>
    </tr>
    <tr>
    <td>
    Background:
    </td>
    <td>
    <input type="background" name="background" value="%s">
    </td>
    </tr>
    <tr>
    <td>
    Interests:
    </td>
    <td>
    <input type="interests" name="interests" value="%s">
    </td>
    </tr>
    <tr>
    <td>
    Notes:
    </td>
    <td>
    <input type="notes" name="notes" value="%s">
    </td>
    </tr>
    <tr>
    <td style="padding-bottom:20px;">
    Status:
    </td>
    <td style="padding-bottom:20px;">
    <select>
    <option value="" disabled="disabled" selected="selected">-----</option>
    <option %svalue="Pre-Interview">Pre-Interview</option>
    <option %svalue="Offer Pending">Offer Pending</option>
    <option %svalue="Offer Accepted">Offer Accepted</option>
    <option %svalue="Offer Rejected">Offer Rejected</option>
    <option %svalue="Decline to Move Forward">Decline to Move Forward</option>
    </select>
    </td>
    </tr>
    <tr>
    <td style="border-top:1px solid black; padding-top:20px;">Upload a Resume</td>
    <td style="border-top:1px solid black; padding-top:20px;"><input style="border:none" type="file" name="resume" id="resume"></td>
    
    </tr></table>
    <a class="butt" href="javascript:void()" onClick="document.getElementById('addCandidate').submit()">Submit</a>
    
    </form></div>
	</body>
    </html>
    """

class EditCandidateForm(webapp2.RequestHandler):
    
	def post(self):
        	#candidates = Candidate.query().fetch(20)
            candidate = Candidate.query(Candidate.email == self.request.get('email')).fetch(1)[0]
            self.response.out.write(ADD_CANDIDATE_FORM %
                                (candidate.name,
                                 candidate.email,
                                 "selected " if candidate.university=="purdue" else "",
                                 "selected " if candidate.university=="illinois" else "",
                                 "selected " if candidate.university=="depauw" else "",
                                 "selected " if candidate.major=="cs" else "",
                                 "selected " if candidate.major=="engr" else "",
                                 "selected " if candidate.major=="comm" else "",candidate.GPA,
                                 candidate.background,
                                 candidate.interests,
                                 candidate.notes,
                                 "selected " if candidate.status=="Pre-Interview" else "",
                                 "selected " if candidate.status=="Offer Pending" else "",
                                 "selected " if candidate.status=="Offer Accepted" else "",
                                 "selected " if candidate.status=="Offer Rejected" else "",
                                 "selected " if candidate.status=="Decline to Move Forward" else "",))


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

