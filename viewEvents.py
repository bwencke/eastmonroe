import cgi
import webapp2
from google.appengine.ext import ndb
from data import Event

STYLE = """\
    <head>
         <link rel="stylesheet" href="/stylesheets/style.css">
    </head>
    """

class ViewEvents(webapp2.RequestHandler):

    def get(self):
        events = Event.query().fetch(20)

        self.response.out.write('<html>' + STYLE + '<body><div class="contentBox"><h1>Events</h1><table><tr class="head"><td>Name</td><td>Location</td><td>Date</td><td>Time</td></tr>')
        i = 0;
        for event in events:
            i=i+1
            self.response.out.write('<tr')
            if(i%2 == 0):
                self.response.out.write(' class="odd"')
            self.response.out.write('><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' %
                                    (event.name,
                                    event.location,
                                     event.date,
                                     event.time))
        self.response.out.write('</table><form action="/main" method="post"><input type="submit" value="Main Menu"></form></div></body></html>')







#    def get(self):
#        events = Event.query().fetch(20)
#
#        self.response.out.write('<html><body><form action="/main" method="post"><table><tr class="head"><td>Name</td><td>&nbsp&nbsp&nbsp</td><td>Date</td></tr>')
#        for event in events:
#            self.response.out.write('<tr><td>%s</td><td></td><td>%s</td></tr>' %
#                                    (event.name,
#                                    event.date))
#
#        self.response.out.write("""<tr><td><input type="submit" value="Main Menu"></td></tr>""")
#        self.response.out.write('</table></body></html>')
