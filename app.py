from flask import Flask, flash, jsonify, redirect, render_template, request, session
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/important")
def important():
    return render_template("important.html")

@app.route("/notes")
def notes():
    return render_template("notes.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/todo")
def todo():
    return render_template("todo.html")

@app.route("/ongoing")
def ongoing():
    return render_template("ongoing.html")

@app.route("/completed")
def completed():
    return render_template("completed.html")

@app.route("/archieve")
def archieve():
    return render_template("archieve.html")

@app.route("/trash")
def trash():
    return render_template("trash.html")