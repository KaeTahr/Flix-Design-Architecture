from flask import Flask, request, render_template, Blueprint
import models
import initiate_database
import Recommendations as R

app = Flask(__name__)
models.start_mappers()
content = Blueprint("rec", __name__, template_folder="templates/")

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200

@app.route("/rec")
def display_recommendations():
    return render_template('rec.html')

@app.route("/rec", methods=['POST'])
def form_post():
    username = request.form['username']
    p1 = request.form.get('p1')
    p2 = request.form.get('p2')
    p3 = request.form.get('p3')
    p4 = request.form.get('p4')
    p5 = request.form.get('p5')
    order = request.form['order']

    pref = []
    if p1:
        pref.append(int(p1))
    if p2:
        pref.append(int(p2))
    if p3:
        pref.append(int(p3))
    if p4:
        pref.append(int(p4))
    if p5:
        pref.append(int(p5))
    if len(pref) != 3:
        return 'please submit only 3 preferences'

    if order == 'Ascending':
        rec_res = R.StrategyRecommendationAsc(pref[0], pref[1], pref[2])
    else:
        rec_res = R.StrategyRecommendationDesc(pref[0], pref[1], pref[2])

    rec_list_titles = []
    rec_list = rec_res.run_algorithm()
    for i in rec_list:
        rec_list_titles.append(i.movie_title)

    if len(rec_list) == 0:
        initiate_database.main()
        rec_list = rec_res.run_algorithm()
        for i in rec_list:
            rec_list_titles.append(i.movie_title)

    return render_template('results.html', username=username, results=rec_list_titles)