from flask import Flask, request,render_template

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@127.0.0.1:3306/Blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "my_codeee"

from extensions import *
from model import *
from controllers import *


if __name__ == "__main__":
    # app.init_app(db)
    # app.init_app(migrate)
    app.run(port=5000,debug=True)