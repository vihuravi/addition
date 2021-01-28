from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.sqlite3'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format('postgres','root','localhost','Ravindra')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}/{}'.format('rspegiimwvxbnb','0aefdf8ab5635c605073428a74476ef90d70c2993143053b5a64f96bf322e87a','ec2-3-220-193-133.compute-1.amazonaws.com','dfe7h4r2crqel0')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
