
#main.py
# the import section
import webapp2
import jinja2
import os

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):  # for a get request
        home_template = the_jinja_env.get_template('index.html')
        self.response.write(home_template.render())  # the response

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage), #this maps the root url to the Main Page Handler
], debug=True)
