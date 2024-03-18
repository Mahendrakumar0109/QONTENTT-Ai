# app/server.py

from flask import Flask, jsonify, request
from flask_graphql import GraphQLView
from app.schema import schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

from app.models import db
db.init_app(app)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
