
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
        deleting_title.key.delete()

        self.response.write(delete_template.render(the_variables))
class EditWebtoon(webapp2.RequestHandler):
    def post(self):
        edit_template = the_jinja_env.get_template('html/editPage.html')
        webtoon_for_editing = self.request.get('hiddenValueForEdit')
        The_entitity_chosen= NewWebtoon.query().filter(NewWebtoon.title_class == webtoon_for_editing).get()
        The_entitity_chosen_title=The_entitity_chosen.title_class
        The_entitity_chosen_pic=The_entitity_chosen.picture_class
        The_entitity_chosen_link=The_entitity_chosen.link_class
        the_variables_for_edit = {
            "value_from_form_for_edit": The_entitity_chosen,
        }

        self.response.write(edit_template.render(the_variables_for_edit))
class EditWebtoonConfirm(webapp2.RequestHandler):
    def post(self):
        editConfirm_template = the_jinja_env.get_template('html/editConfirm.html')
        title_for_it=self.request.get('hiddenDateValueForEditing')
        link_editing = self.request.get('linkEditing')
        title_editing=self.request.get('titleEditing')
        pic_editing=self.request.get('picEditing')

        The_webtoon_chosen= NewWebtoon.query().filter(NewWebtoon.title_class ==title_for_it).get()
        The_webtoon_chosen.title_class=title_editing
        The_webtoon_chosen.picture_class=pic_editing
        The_webtoon_chosen.link_class=link_editing
        The_webtoon_chosen.put()
        print("This is the webtoon")
        print(title_for_it)

        the_variable_for_edit = {
            "editing_title": title_editing,
            "editing_link": link_editing,
            "editing_pic": pic_editing,
        }


        self.response.write(editConfirm_template.render(the_variable_for_edit))
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/addComicConfirm', ShowComic),
    ('/deleteConfirm', DeleteWebtoon),
    ('/editPage', EditWebtoon),
    ('/editConfirm', EditWebtoonConfirm), #this maps the root url to the Main Page Handler
], debug=True)
