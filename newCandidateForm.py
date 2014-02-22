import cgi
import webapp2

ADD_CANDIDATE_FORM = """\
<html>
	<body>
		<form action="/addCandidate" method="post">
			<table>
				<tr>
					<td>
						New Candidate:
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
                                        Email:
                                    </td>
                                    <td>
                                        <input type="email" name="email">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        University:
                                    </td>
                                    <td>
                                        <input type="text" name="university">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        Major:
                                    </td>
                                    <td>
                                        <input type="text" name="major">
                                    </td>
				</tr>
				<tr>
                                    <td>
                                        GPA:
                                    </td>
                                    <td>
                                        <input type="number" name="gpa">
                                    </td>
				</tr>
			</table>
		</form>
	</body>
</html>
"""

class AddCandidateForm(webapp2.RequestHandler):

	def get(self):
		self.response.write(ADD_CANDIDATE_FORM)
