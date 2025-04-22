from flask import Flask, flash, jsonify, redirect, render_template, request, session
app = Flask(__name__)


NAV_ITEMS = [
    {"endpoint": "index", "url": "/", "icon": "bi-clipboard-data", "icon_fill": "bi-clipboard-data-fill", "label": "Dashboard"},
    {"endpoint": "important", "url": "/important", "icon": "bi-star", "icon_fill": "bi-star-fill", "label": "Important"},
    {"endpoint": "notes", "url": "/notes", "icon": "bi-journals", "icon_fill": "bi-pencil-square", "label": "Notes"},
    {"endpoint": "schedule", "url": "/schedule", "icon": "bi-calendar-minus", "icon_fill": "bi-calendar-minus-fill", "label": "Schedule"},

    {"endpoint": "todo", "url": "/todo", "icon": "bi-folder", "icon_fill": "bi-folder-fill", "label": "Todo"},
    {"endpoint": "ongoing", "url": "/ongoing", "icon": "bi-folder", "icon_fill": "bi-folder-fill", "label": "Ongoing"},
    {"endpoint": "completed", "url": "/completed", "icon": "bi-folder", "icon_fill": "bi-folder-fill", "label": "Completed"},

    {"endpoint": "archieve", "url": "/archieve", "icon": "bi-folder", "icon_fill": "bi-folder-fill", "label": "Archieve"},
    {"endpoint": "trash", "url": "/trash", "icon": "bi-trash", "icon_fill" : "bi-trash-fill", "label": "Trash"},
]


@app.route("/")
def index():
    return render_template("index.html", NAV_ITEMS=NAV_ITEMS)

@app.route("/important")
def important():
    return render_template("important.html", NAV_ITEMS=NAV_ITEMS)

@app.route("/notes")
def notes():
    return render_template("notes.html", NAV_ITEMS=NAV_ITEMS)

@app.route("/schedule")
def schedule():
    return render_template("schedule.html", NAV_ITEMS=NAV_ITEMS)

@app.route("/todo",methods=["GET", "POST"])
def todo():
     if request.method == "POST":
        # name = request.form.get("name")
        # month = request.form.get("month")
        # day = request.form.get("day")
        # if not name:
        #     return redirect("/")
        # if not month:
        #     return redirect("/")
        # if not day:
        #     return redirect("/")

        # db.execute("INSERT INTO birthdays (name, month, day) VALUES(?,?,?)", name, month, day)
        # return redirect("/")
        return render_template("todo.html", NAV_ITEMS=NAV_ITEMS)
     else:
        # TODO: Display the entries in the database on index.html
        # birthdays = db.execute("SELECT * FROM birthdays")
        # return render_template("todo.html", birthdays=birthdays)
        return render_template("todo.html", NAV_ITEMS=NAV_ITEMS)

@app.route("/ongoing")
def ongoing():
    return render_template("ongoing.html", NAV_ITEMS=NAV_ITEMS)

@app.route("/completed")
def completed():
    return render_template("completed.html", NAV_ITEMS=NAV_ITEMS)

@app.route("/archieve")
def archieve():
    return render_template("archieve.html", NAV_ITEMS=NAV_ITEMS)

@app.route("/trash")
def trash():
    return render_template("trash.html", NAV_ITEMS=NAV_ITEMS)