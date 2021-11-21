import os
from dataclasses import dataclass
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message


app = Flask(__name__, static_folder="frontend/build/static", template_folder="frontend/build")

# app configurations
if os.getcwd() == '/app':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL_PGSQL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['MAIL_SERVER'] = os.environ.get('EMAIL_HOST')
app.config['MAIL_PORT'] = os.environ.get('EMAIL_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')
app.config['MAIL_USE_TLS'] = True



db = SQLAlchemy(app)
mail = Mail(app)


# SQLAlchemy Models
@dataclass
class Project(db.Model):

    id:int
    title:str
    details:str
    image:str
    live_url:str
    github_repo:str

    __tablename__ = 'avishek_project'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    details = db.Column(db.Text,nullable=False)
    image = db.Column(db.String(255),default='placeholder.png')
    live_url = db.Column(db.String(200), nullable=False)
    github_repo = db.Column(db.String(200), nullable=False)

    def __str__(self):
        return self.title


# view routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/', methods=['GET'])
@cross_origin()
def get_all_projects():
    projects = Project.query.all()

    for project in projects:
        project.image = f'https://res.cloudinary.com/davishek7/image/upload/v1/{project.image}'
    return jsonify({'projects' : projects})


@app.route('/api/contact_view/', methods=['POST'])
@cross_origin()
def contact_view():

    name = request.form['name']
    subject = request.form['subject']
    email = request.form['email']
    message = request.form['message']

    msg = Message(
                f'{subject} from {name}({email})',
                sender = "Avishek Das",
                recipients = [os.environ.get('RECEIVER_EMAIL')]
                 )
    msg.body = message
    mail.send(msg)

    return jsonify({'status':True,'message':f'Thank you {name} for contacting me! I will be back to you later.'})


# running the app
if __name__ == '__main__':
    if os.getcwd() == '/app':
        app.debug = False
    else:
        app.debug = True
    app.run()
