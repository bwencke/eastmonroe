import cgi
import webapp2
from google.appengine.ext import ndb
from data import Candidate
from editCandidate import EditCandidateForm

STYLE = """\
    <head>
         <link rel="stylesheet" href="/stylesheets/style.css">
    </head>
    """

class ViewCandidates(webapp2.RequestHandler):

    def get(self):
        candidates = Candidate.query().fetch(20)

        self.response.out.write('<html>' + STYLE + '<body><div class="contentBox"><h1>Candidates</h1><table><tr class="head"><td>Name</td><td>Email</td><td>Major</td><td>University</td><td></td></tr>')
        i = 0;
        for candidate in candidates:
            i=i+1
            self.response.out.write('<tr onClick="document.forms[\'candidate'+str(i)+'\'].submit();"')
            if(i%2 == 0):
                self.response.out.write(' class="even"')

            self.response.out.write('><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><form name="candidate%s" method="post" action="/editCandidate"><input type="hidden" name="email" value="%s"></form></td></tr>' %
                                    (candidate.name, candidate.email, candidate.major, candidate.university, str(i), candidate.email))

        self.response.out.write('</table><form action="/main" method="post"><input type="submit" value="Main Menu"></form></div></body></html>')


#<a href="/" class="butt">Main Menu</a>
>>>>>>> 9f24f42dc1c430c6c28e69c21f414668526e5824
