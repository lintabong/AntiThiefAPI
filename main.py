from flask import Flask

app = Flask(__name__)


@app.route('/data')
def get_drink():
    return {"data": {
        "status":"aman",
        "activity":"berdiri"
        }
    }

if __name__ == "__main__":
    app.run(debug=True)
