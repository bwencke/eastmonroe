import cgi
import webapp2
from google.appengine.ext import ndb
from data import Candidate

class ViewCandidates(webapp2.RequestHandler):

    def get(self):
        candidates = Candidate.query().fetch(20)

        self.response.out.write('<html><body><form action="/main" method="post"><table><tr class="head"><td>Name</td><td>&nbsp&nbsp&nbsp</td><td>Email</td></tr>')
        for candidate in candidates:
            self.response.out.write('<tr><td>%s</td><td></td><td>%s</td></tr>' %
                                    (candidate.name,
                                    candidate.email))

        self.response.out.write("""<tr><td><input type="submit" value="Main Menu"></td></tr>""")
        self.response.out.write('</table></body></html>')
