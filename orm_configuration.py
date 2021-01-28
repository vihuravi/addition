from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.sqlite3'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format('postgres','root','localhost','Ravindra')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{}:{}@{}/{}'.format('mbbahlmmqpgreu','0650cb25ad80e017f52369fbca5b4d5cf4e6b6b9c38e1d6dcdf96c25d86733ea','ec2-174-129-199-54.compute-1.amazonaws.com','dak07p1lijngks')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
