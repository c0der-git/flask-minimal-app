import os
import logging
from dotenv import load_dotenv
load_dotenv() #load env. variables

from flask import Flask
from views import view #load views/routes

#debug lines
app_name = os.environ.get('APP_NAME')
logging.debug("Application name: "+app_name)

app = Flask(__name__)
app.register_blueprint(view)

if __name__ == '__main__':
    app.run()
