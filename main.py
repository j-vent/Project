# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
def valid_month(month):
		months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
		for i in range (12):
			if month.capitalize() == months[i].capitalize():
				return (months[i])
	
def valid_day(day):
		if day.isdigit():
			intday = int(day)
			if intday > 0 and intday <= 31:
				return (day)
def valid_year(year):
		if year.isdigit():
			intyear = int(year)
			if intyear >= 1900 and intyear <= 2020:
				return (intyear)
form= """
<form method = "post">
	What is your birthday?
	<br>
	<label>Month<input type ="text" name = "month" value="%(month)s"></label>
	<label>Day<input type ="text" name = "day" value="%(day)s"></label>
	<label>Year<input type ="text" name = "year" value="%(year)s"></label>
	<div style= "color: red">%(error)s</div>
	<br>
	<br>
	<input type = "submit">
	
</form>

"""

class MainPage(webapp2.RequestHandler):
	
	
	def write_form(self, error= "", month= "", day ="", year= ""):
		self.response.out.write(form % {"error": error,
										"month": month,
										"day": day,
										"year": year})
	
	def get(self):
	#self.response.headers['Content-Type'] = 'text/plain'
		self.write_form()
		
	
	
	
 
	def post(self):
		user_month = valid_month(self.request.get('month'))
		user_day = valid_day(self.request.get('day'))
		user_year = valid_year(self.request.get('year'))
		
		#self.response.out.write("Thanks! That was a valid day!")
		
		if not (user_month and user_day and user_year):
			self.write_form("That does not look valid fam")
		else:
			self.response.out.write("Thanks! That was a valid day!")

	
            		
'''
class TestHandler(webapp2.RequestHandler):
	def get(self): #change to post
		q = self.request.get("q")
		self.response.out.write(q)
		
		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write(self.request)
		
	

'''
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
