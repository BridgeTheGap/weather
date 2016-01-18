import webapp2

form = '''
Get weather information from <em>SK Planet Weather Planet API</em>
<br>
<form method="get" action="http://apis.skplanetx.com/weather/current/minutely?version=1&lat=%(lat)s&lon=%(lon)s">
	<label>Latitude:
		<input name="lat">
	</label>
	<label>Longitude:
		<input name="lon">
	</label>
	<input type="submit">
</form>
'''



class MainPage(webapp2.RequestHandler):
	def submit_form(self, lat="", lon=""):
		self.response.out.write(form % {"lat":lat,
										"lon":lon})

	def safe_request_lat(self):
		input_lat = self.request.get("lat")
		if input_lat.isdigit():
			return input_lat
		return "37.5714000000"

	def safe_request_lon(self):
		input_lon = self.request.get("lon")
		if input_lon.isdigit():
			return input_lon
		return "126.9658000000"

	def get(self):
		print self.request
		print "!!!!!!!!!!!!!"
		print self.response
		lat = self.safe_request_lat()
		lon = self.safe_request_lon()
		self.submit_form(lat, lon)

app = webapp2.WSGIApplication([
	('/', MainPage), ('/weather', MainPage)
], debug=True)