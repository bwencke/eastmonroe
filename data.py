import webapp2

class AnotherClass(webapp2.RequestHandler):
	
	def get(self):
		self.response.write('<html><body>hi</body></html>');
