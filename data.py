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
<<<<<<< HEAD
    #resume = ndb.
=======

class Event(ndb.Model):
    name = ndb.StringProperty(indexed=True)
    location = ndb.StringProperty(indexed=True)
    date = ndb.DateProperty(indexed=True)
    time = ndb.TimeProperty(indexed=True)
    
>>>>>>> a27edcff6acdb340823fc53c9c3694d4224566cb
