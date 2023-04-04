import os
from dotenv import load_dotenv
load_dotenv() #load env. variables

from flask import Flask
from views import view #load views/routes

#debug lines
name = os.environ.get('FLASK_APP')
print(name)

app = Flask(__name__)
app.register_blueprint(view)

if __name__ == '__main__':
    app.run()
