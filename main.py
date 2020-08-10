
#main.py
# the import section
import webapp2
import jinja2
import os
from google.appengine.ext import ndb
import time

# This initializes the jinja2 Environment.
# This will be the same in every app that uses the jinja2 templating library.
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class NewWebtoon(ndb.Model):
  title_class = ndb.StringProperty(required=True)
  picture_class = ndb.TextProperty(required=True)
  link_class= ndb.StringProperty(required=True)
  date_class=ndb.FloatProperty(required=True)

class HomePage(webapp2.RequestHandler):
    def get(self):  # for a get request
        home_template = the_jinja_env.get_template('index.html')
        webtoon_all=NewWebtoon.query().order(NewWebtoon.date_class).fetch()
        self.response.write(home_template.render({'webtoon_info': webtoon_all,
                                                    }))  # the response
class ShowComic(webapp2.RequestHandler):
    def post(self):
        results_template = the_jinja_env.get_template('html/addComic.html')
        # Access the user data via the form's input elements' names.
        title_of_comic = self.request.get('titleGiven')
        pic_of_comic = self.request.get('picGiven')
        link_of_comic=self.request.get('linkGiven')
        # Organize that user data into a dictionary.
        the_variable_dict = {
            "title_from_form": title_of_comic,
            "pic_from_form": pic_of_comic,
            "link_from_comic": link_of_comic,
        }
        new_entity=NewWebtoon(title_class=title_of_comic, picture_class=pic_of_comic, link_class=link_of_comic, date_class=time.time())
        new_entity.put()
        print(new_entity)
        # pass that dictionary to the Jinja2 `.render()` method
        self.response.write(results_template.render(the_variable_dict))
class DeleteWebtoon(webapp2.RequestHandler):
    def post(self):
        delete_template = the_jinja_env.get_template('html/deletePage.html')
        title_for_deleting = self.request.get('hiddenValue')
        the_variables = {
            "value_from_form": title_for_deleting,
        }
        deleting_title = NewWebtoon.query().filter(NewWebtoon.title_class == title_for_deleting).get()
        print(title_for_deleting)
        print("this is key below")
        print(deleting_title)
        deleting_title.key.delete()

        self.response.write(delete_template.render(the_variables))


# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/addComicConfirm', ShowComic),
    ('/deleteConfirm', DeleteWebtoon), #this maps the root url to the Main Page Handler
], debug=True)
