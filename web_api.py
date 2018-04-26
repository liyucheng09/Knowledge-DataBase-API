import json
from flask import Flask,request,jsonify
from flask_script import Manager
from db import *

app=Flask(__name__)
app.config['JSON_AS_ASCII']=False
manager=Manager(app)

@app.route('/')
def index():
	return '<h1>hello world!</h1>'

@app.route('/ment2ent')
def ment2ent_api():
	ment=request.args.get('q')
	ment_cursor=ment2ent(ment)
	r=ment_cursor.search()
	if r:
		return jsonify(r)
	else:
		return jsonify({'status':'Error','return':[]})

@app.route('/triples')
def triples_api():
	ent=request.args.get('q')
	triples_cursor=triples(ent)
	r=triples_cursor.search()
	if r:
		return jsonify(r)
	else:
		return jsonify({'status':'Error','return':[]})

if __name__=='__main__':
	manager.run()
