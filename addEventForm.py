import cgi
import webapp2
from data import Event

ADD_EVENT_FORM = """\
<html>
	<body>
		<form action="/persistEvent" method="post">
			<table>
				<tr>
					<td>
						New Event:
					</td>
				</tr>
                                <tr>
                                    <td>
                                        Name:
                                    </td>
                                    <td>
                                        <input type="text" name="name">
                                    </td>
                                </tr>
				<tr>
                                    <td>
                                        Location:
                                    </td>
                                    <td>
                                        <input type="text" name="location">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Date:
                                    </td>
                                    <td>
                                        <input type="date" name="date">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Time:
                                    </td>
                                    <td>
                                        <input type="time" name="time">
                                    </td>
				</tr>
			</table>
                        <input type="submit" value="Submit">
		</form>
	</body>
</html>
"""

class AddEventForm(webapp2.RequestHandler):

	def get(self):
		self.response.write(ADD_EVENT_FORM)


class AddEventToDatastore(webapp2.RequestHandler):
    
    def post(self):
        self.response.write("Event Added.")
        event = Event()
        event.name = self.request.get('name')
        event.location = self.request.get('location')
        event.date = self.request.get('date')
        event.time = self.request.get('time')
        event.put()
        self.response.write("""<html><body><table><tr><td><form action="/main" method="post"><input type="submit" value="Main Menu"></form></td></tr></table></html></body>""")

