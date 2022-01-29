from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

myUser = "lincoding_root"
myPass = "5c(3(U!z-PqA"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://lincoding_root:5c(3(U!z-PqA@103.147.154.24/lincoding_skeletonML"

class user(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   username = db.Column(db.String(50))
   password = db.Column(db.String(50))


@app.route('/data', methods = ['PUT' , 'GET'])
def getData():
    myStatus = request.args.get('status')
    myActivity = request.args.get('activity')
    print(myStatus,myActivity)
    return 'status = {}, activity = {}'.format(myStatus,myActivity)

@app.route('/user')
def get_drink():
    return jsonify({"user":{"username":"admin","password":"admin"}})

if __name__ == "__main__":
    app.run(debug=True)
