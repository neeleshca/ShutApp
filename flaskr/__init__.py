import os
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, jsonify, session, make_response

from flask import Flask
from PIL import Image
import datetime
from flaskr.db import get_db
from redis import Redis
import rq
import os
import requests

os.environ['NO_PROXY'] = '127.0.0.1'
queue = rq.Queue('save-image', connection=Redis.from_url('redis://'))


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    from . import db
    db.init_app(app)

    @app.route("/")
    def images():
        return render_template("main.html")
    

    # a simple page that says hello
    @app.route("/submitted", methods=['POST'])
    def submitted():
        db = get_db()
        try:
            file = request.files["file"]
            username  = request.form.get("username")
        except:
            print("Bad request\n")
            return make_response(jsonify({}), 400)

        im = Image.open(file)
        try:    
            db.execute(
                'INSERT INTO user (username, created) VALUES (?, ?)',
                (username, datetime.datetime.now())
            )
            db.commit()
            print("Sucessful insert\n")
            job = queue.enqueue('tasks.crop', im,username+"."+im.format.lower())
            return make_response(jsonify({}), 201)
        except:
            print("Bad request, duplicate username\n")
            return make_response(jsonify({}), 400)
    
    return app
