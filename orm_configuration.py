from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.sqlite3'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format('postgres','root','localhost','Ravindra')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}/{}'.format('ulfwyuusmjmijj','3a308426d39891d560b4f10f51bf6f2bb9e3d03a4bb5b3ce647bd37a07aba8a7','ec2-54-158-1-189.compute-1.amazonaws.com','df2gpp8l5bfvqe')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
