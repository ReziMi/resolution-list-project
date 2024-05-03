import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "!@#zxy$%QW&*(!@3edD4567!@#$%^&*()_+-"
app.config["SESSION_COOKIE_NAME"] ="!(!@3edD4@#zxy$%QW&*567!@#$%^&*()_+-"

@app.route("/", methods=["POST", "GET"])
def index():
    session["all_items"], session["show_items"]=get_db()
    return render_template("index.html", all_items=session["all_items"], show_items=session["show_items"])

@app.route("/add_items", methods=["post"])
def add_items():
    session["show_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html", all_items=session["all_items"],
                                         show_items=session["show_items"])

@app.route("/remove_items", methods=["post"])
def remove_items():
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["show_items"]:
            idx = session["show_items"].index(item)
            session["show_items"].pop(idx)
            session.modified = True

    return render_template("index.html", all_items=session["all_items"],
                                         show_items=session["show_items"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('bucket_list.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM bucket_list")
        all_data = cursor.fetchall()
        all_data = [val[1] for val in all_data]  # Fetch the item from each row

        show_list=all_data.copy()
        random.shuffle(show_list)
        show_list=show_list[:5]
    return all_data, show_list


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()