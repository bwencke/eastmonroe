import cgi
import webapp2
from google.appengine.ext import ndb
from data import Candidate

STYLE = """\
    <head>
         <link rel="stylesheet" href="/stylesheets/style.css">
    </head>
    """

class ViewCandidates(webapp2.RequestHandler):

    def get(self):
        candidates = Candidate.query().fetch(20)

        self.response.out.write('<html>' + STYLE + '<body><div class="contentBox"><h1>Candidates</h1><table><tr class="head"><td>Name</td><td>Email</td><td>Major</td><td>University</td></tr>')
        i = 0;
        for candidate in candidates:
            i=i+1
            self.response.out.write('<tr')
            if(i%2 == 0):
                self.response.out.write(' class="odd"')
            self.response.out.write('><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' %
                                    (candidate.name,
                                    candidate.email,
                                     candidate.major,
                                     candidate.university))
        self.response.out.write('</table><form action="/main" method="post"><input type="submit" value="Main Menu"></form></div></body></html>')


#<a href="/" class="butt">Main Menu</a>
