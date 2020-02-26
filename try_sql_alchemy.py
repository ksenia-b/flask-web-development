from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.customers'

db = SQLAlchemy(app)
# Approach 1
# customer = db.Table('customers', db.metadata, autoload=True, autoload_with=db.engine)


@app.route('/')
def index():
    results = db.session.query(customer).all()
    for r in results:
        print(r.name)

    return ''
