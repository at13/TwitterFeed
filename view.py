from flask import Flask
import os
import sqlite3
import json
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import psycopg2

from flask_sqlalchemy import SQLAlchemy
import urlparse


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    urlparse.uses_netloc.append("postgres")
    x = os.environ['DATABASE_URL']
    url = urlparse.urlparse(x)
    conn =  psycopg2.connect(database=url.path[1:],user=url.username,password=url.password,host=url.hostname,port=url.port)
    return conn

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    conn = connect_db()
    return conn

@app.route('/', methods=['GET', 'POST'])
def base():
	if request.method == 'POST':
		id = request.form['id']
		#print id
		conn  = get_db()
		print conn
		cur = conn.cursor()
		cur.execute('select count(*) FROM startupIndia')
		size  = cur.fetchone()[0]
		limit = int(size) - int(id)
		#print limit
		cur.execute('select * from startupIndia limit %s', (limit,))
		r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
		#entries = cur.fetchall()
		#print json.dumps(r)
		return json.dumps(r)
	return render_template('show_entries.html')




if __name__ == "__main__":
	app.run(debug=True)