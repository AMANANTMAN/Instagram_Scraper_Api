import logging
import os
from flask import Flask
from flask_restful import Resource, Api
from instagrapi import Client
from instagrapi.exceptions import LoginRequired


cl = Client()
app = Flask(__name__)
api = Api(app)
logger = logging.getLogger()
# https://flask-restful.readthedocs.io/en/latest/index.html
# https://github.com/instaloader/instaloader

USERNAME = "acefunnyboy"
PASSWORD = "Mw6uykq4"

logger = logging.getLogger()


def login_user(USERNAME, PASSWORD):
    session = cl.load_settings("session.json")
    login_via_session = False
    login_via_pw = False
    if session:
        try:
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)
            try:
                cl.get_timeline_feed()
            except LoginRequired:
                logger.info(
                    "Session is invalid, need to login via username and password"
                )
                old_session = cl.get_settings()
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])
                cl.login(USERNAME, PASSWORD)
            login_via_session = True
        except Exception as e:
            logger.info(f"Couldn't login user using session information: {e}")
    if not login_via_session:
        try:
            logger.info(f"Attempting to login via username and password. username: {USERNAME}")
            if cl.login(USERNAME, PASSWORD):
                login_via_pw = True
        except Exception as e:
            logger.info(f"Couldn't login user using username and password: {e}")
    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self):
        return
    def delete(self):
        return
    def put(self):
        return
    
class Media_Comment(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self):
        return
    def delete(self):
        return
    def put(self):
        return
    
class Media_Comment_Chunk(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self):
        return
    def delete(self):
        return
    def put(self):
        return

class user_followers(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self):
        return
    def delete(self):
        return
    def put(self):
        return


class user_following(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self):
        return
    def delete(self):
        return
    def put(self):
        return
    
class user_info(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self):
        return
    def delete(self):
        return
    def put(self):
        return

class search_following(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self):
        return
    def delete(self):
        return
    def put(self):
        return

class search_followers(Resource):
    def get(self):
        return {"hello": "world"}
    def post(self):
        return
    def delete(self):
        return
    def put(self):
        return    

api.add_resource(Media_Comment,"/comment/media_comment")
api.add_resource(Media_Comment_Chunk,"/comment/media_comment_chunk")
api.add_resource(user_followers,"/users/user_followers")
api.add_resource(user_following,"/users/user_following")
api.add_resource(user_info, "/users/user_info")
api.add_resource(search_following,"/users/search_following")
api.add_resource(search_followers)
# I dont have anything else planned at this momment
# ok
# what do I do with that

# http://website.com/anthony
class Name(Resource):
    def get(self, name):
        if name == "joshua":
            return {"Hello": "World"}
        return {"You": "Are Dumb"}


api.add_resource(Name, "/<string:name>")

if __name__ == "__main__":
    login_user(USERNAME, PASSWORD)
    print(cl.user_info_by_username_v1("acefunnyboy"))
    #app.run(debug=False)
