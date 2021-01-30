from flask import Flask
import sqlite3
from flask import Flask, flash, redirect, render_template, request, url_for, g, session
import os
 

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run


'''
# the database file we are going to communicate with
DATABASE = './assignment1.db'
# connects to the database
def get_db():
    # if there is a database, use it
    db = getattr(g, '_database', None)
    if db is None:
        # otherwise, create a database to use
        db = g._database = sqlite3.connect(DATABASE)
    return db

# converts the tuples from get_db() into dictionaries
# (don't worry if you don't understand this code)
def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

# given a query, executes and returns the result
# (don't worry if you don't understand this code)
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# home page
@app.route('/', methods=['Get', 'Post'])
def Checkout():
    # get database
    db = get_db()
    db.row_factory = make_dicts

    items = []
    # send the list of items to the user to select
    for item in query_db('SELECT * FROM item'):
        items.append(item)

    # close database
    db.close()
    return render_template('Checkout.html',items = items)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888,debug=True)
'''