from flask import Flask
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
# db = SQLAlchemy(app)

myUser = "lincoding_root"
myPass = "5c(3(U!z-PqA"


# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://lincoding_root:5c(3(U!z-PqA@103.147.154.24/lincoding_skeletonML"

def mysqlconnect():
    # To connect MySQL database
    global conn
    global cur
    conn = pymysql.connect(
        host='redfin.id.rapidplex.com',
        user='lincodin_myroot',
        password="myguard813",
        db='lincodin_exampleDB',
    )

    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print(output)

    # To close the connection
    conn.close()


# class user(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    username = db.Column(db.String(50))
#    password = db.Column(db.String(50))

@app.route('/')
def index():
    return 'index'


@app.route('/data', methods=['PUT', 'GET'])
def getData():
    myStatus = request.args.get('status')
    myActivity = request.args.get('activity')
    print(myStatus, myActivity)

    try:
        cur.execute("INSERT INTO tweets (geom) VALUES (%s)" % (myStatus))
    except TypeError:
        print("Could not INSERT")

    conn.close()

    return 'status = {}, activity = {}'.format(myStatus, myActivity)


@app.route('/user')
def get_drink():
    return jsonify({"user": {"username": "admin", "password": "admin"}})


if __name__ == "__main__":
    app.run(debug=True)
