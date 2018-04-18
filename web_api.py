import json
from flask import Flask
from flask.ext.script import Manager
from db import *

app=Flask(__name__)
manager=Manager(app)

@app.route('/ment2ent?q=<ment>')
def ment2ent_api():
	ment_cursor=ment2ent(ment)
	r=ment_cursor.search()
	if r:
		return json.dumps(r,ensure_ascii=False)
	else:
		return json.dumps({'status':'Error','return':[]},ensure_ascii=False)

@app.route('/triples?q=<ent>')
def triples_api()
	triples_cursor=triples(ent)
	r=triples_cursor.search()
	if r:
		return return json.dumps(r,ensure_ascii=False)
	else:
		return json.dumps({'status':'Error','return':[]},ensure_ascii=False)

if __name__=='__main__':
	manager.run()