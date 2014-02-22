import webapp2
from data import Candidate

class NewCandidate(webapp2.RequestHandler):

    def post(self):
        candidate = Candidate()
        candidate.name = self.request.get('candidateName')
        #candidate.email = self.request.get('candidateEmail')
        #candidate.university = self.request.get('candidateEmail')
        candidate.put()
