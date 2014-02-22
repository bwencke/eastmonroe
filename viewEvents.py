import cgi
import webapp2
from google.appengine.ext import ndb
from data import Event

class ViewEvents(webapp2.RequestHandler):

    def get(self):
        events = Event.query().fetch(20)

        self.response.out.write('<html><body><form action="/main" method="post"><table><tr class="head"><td>Name</td><td>&nbsp&nbsp&nbsp</td><td>Date</td></tr>')
        for event in events:
            self.response.out.write('<tr><td>%s</td><td></td><td>%s</td></tr>' %
                                    (event.name,
                                    event.date))

        self.response.out.write("""<tr><td><input type="submit" value="Main Menu"></td></tr>""")
        self.response.out.write('</table></body></html>')
