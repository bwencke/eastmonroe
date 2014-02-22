import webapp2
from google.appengine.ext import ndb

class AnotherClass(webapp2.RequestHandler):

    def get(self):
        self.response.write('<html><body>hi</body></html>');

class Candidate(ndb.Model):
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    major = ndb.StringProperty(indexed=True)
    university = ndb.StringProperty(indexed=True)
    GPA = ndb.FloatProperty()
    background = ndb.TextProperty()
    interests = ndb.TextProperty()
    otherInfo = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    