import os
import logging
from dotenv import load_dotenv
load_dotenv() #load env. variables

from flask import Flask
from views import view #load views/routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(view)

    #debug lines
    app_name = os.environ.get('APP_NAME')
    logging.debug("Application name: "+app_name)

    return app

def run_app():
    app = create_app()

    #Development server run
    if __name__ == '__main__':
        app.run()



run_app()