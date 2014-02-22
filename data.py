import webapp2
from google.appengine.ext import ndb

class Candidate(ndb.Model):
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    major = ndb.StringProperty(indexed=True)
    university = ndb.StringProperty(indexed=True)
    GPA = ndb.FloatProperty()
    background = ndb.TextProperty()
    interests = ndb.TextProperty()
    notes = ndb.TextProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    #resume = ndb.
