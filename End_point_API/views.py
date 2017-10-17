from End_point_API import app
from flask import render_template
import sqlite3


@app.route('/')
@app.route('/index')
def index():
    return render_template('end_point_api/index.html')


@app.route('/jobs/<location>')
def loc_job(location):

    conn = sqlite3.connect('job_db.sqlite3')

    db = conn.cursor()

    db.execute("SELECT * FROM jobs WHERE Location=?", (location,))

    jobs = db.fetchall()

    context = {'jobs': jobs}

    conn.commit()

    conn.close()

    return render_template('end_point_api/location_job.html', context=context)
