from flask import Flask, render_template, abort
from Answer import load_db
from flask_sqlalchemy import SQLAlchemy
from models import *
from sqlalchemy import create_engine
from controllers.RestController import RestController

app = Flask(__name__)
counter = 0
APP_ENV = 'dev';

db_name = 'rdb'
db_pass = 'Kris12#$'
db_user = 'Kris'
db_url = '51.158.130.90'
db_port = '47097'
db_type = 'postgresql'

app.config['SQLALCHEMY_DATABASE_URI'] = db_type + '://'+db_user+':'+db_pass+'@'+db_url+':'+db_port+'/' + db_name

# print(db_type + '://'+db_user+':@'+db_url+'@'+db_url+':'+db_port+'/' + db_name)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)
engine  = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
connection = engine.connect()
value = '2'
value1 = 'kupa'
query = 'select * from public."Alerts"'

results = connection.execute(query)

print(results)

# class Alerts(db.Model):
#     query = db.Query = 'SELECT * FROM public."Alerts"'
#     # al


print ('działam')
@app.route('/')
def hello_world():  # put application's code here
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    return render_template("welcome.html")

@app.route('/date/<int:index>')
def date_view(index):  # put application's code here
    try:
        # db = load_db()
        return render_template("date.html", answer = db[index],index = index, maxIndex = len(db) -1)
    except IndexError:
        return render_template("main/404.html")

@app.route('/count')
def count():  # put application's code here
    global counter
    counter += 1
    return render_template("counter.html", counter=counter)
# return 'This page was served at '+str(counter)

@app.route('/pages/<string:pageName>')
def generate_subpage(pageName):  # put application's code here
    try:
        return render_template("Pages/" + pageName + ".html", templateName = pageName)
    except:
        return render_template("main/404.html")

@app.route('/rest/', methods=['GET'])
def rest_query():
    try:
        rC = RestController()
        rC.query()

        return 1
    except OSError as err:
        print("OS Error: "+err)
        return render_template("main/500.html")

@app.route('/rest/', methods=['POST'])
def rest_update():
    try:
        return 1
    except:
        return render_template("main/500.html")

@app.route('/rest/', methods=['PUT'])
def rest_put():
    try:
        return 1
    except:
        return render_template("main/500.html")

if __name__ == '__main__':

    app.run
    print('poszedłem juz tutaj')