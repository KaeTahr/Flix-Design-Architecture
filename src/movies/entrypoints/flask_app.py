from flask import Flask, request, render_template, Blueprint
import models
import initiate_database
import form_verifier

app = Flask(__name__)
models.start_mappers()
content = Blueprint("rec", __name__, template_folder="templates/")

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

@app.route("/")
def display_recommendations():
    return render_template('rec.html')

@app.route("/", methods=['POST'])
def form_post():
    username = request.form['username']
    p1 = request.form.get('p1')
    p2 = request.form.get('p2')
    p3 = request.form.get('p3')
    p4 = request.form.get('p4')
    p5 = request.form.get('p5')
    order = request.form['order']

    pref = []
    pref = form_verifier.parseform(p1,p2,p3,p4,p5)

    if len(pref) != 3:
        return 'please submit only 3 preferences'

    rec_list = form_verifier.orderPrefs(order, pref)
    rec_list_titles = []
    for i in rec_list:
        rec_list_titles.append(i.movie_title)

    if len(rec_list) == 0:
        initiate_database.main()
        rec_list = form_verifier.orderPrefs(order, pref)
        for i in rec_list:
            rec_list_titles.append(i.movie_title)

    return render_template('results.html', username=username, results=rec_list_titles)
