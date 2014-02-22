import cgi
import webapp2
from google.appengine.ext import ndb
from data import Candidate

STYLE = """\
    <head>
        <style>
            html {
                font-family:Helvetica, Sans-serif;
                font-size:11px;
            }
            td {
                padding:8px;
                padding-left:10px;
                padding-right:10px;
            }
            tr.even {
                background-color:rgb(255,238,230);
            }
            .head {
                background-color:#D95B43;
                color:white;
            }
        </style>
    </head>
    """

class ViewCandidates(webapp2.RequestHandler):

    def get(self):
        candidates = Candidate.query().fetch(20)

        self.response.out.write('<html>' + STYLE + '<body><h1>Candidates</h1><table><tr class="head"><td>Name</td><td>Email</td><td>Major</td><td>University</td></tr>')
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
        self.response.out.write("""<tr><td><input type="submit" value="Main Menu"></td></tr>""")
        self.response.out.write('</table></body></html>')
