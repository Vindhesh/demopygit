from flask import Flask
import sqlalchemy
from sqlalchemy import Column, Integer, Text

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///pin.db'
db = sqlalchemy(app)

# class Pin(db.Model):
#     id = Column(Integer, primary_key = True)
#     title = Coulmn(Text, unique = False)
#     image = Column(Text, unique = False)

db.create_all()

app.debug = True

@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run()
