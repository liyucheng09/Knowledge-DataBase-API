import pymongo

connection=pymongo.MongoClient()
dbp=connection.DBpedia

result_template={
	'status':'',
	'return':'',
}

class ment2ent():
	def __init__(self,ment):
		self.ment=ment
	def search(self):
		if(self.ment==''):
			return None
		else:
			cursor=dbp.ment2ent.find({'m':self.ment})
			result=result_template
			rl=[]
			if cursor.count():
				for i in cursor:
					rl.append(i['e'])
				result['return']=rl
				result['status']='Ok'
			else:
				result['return']=rl
				result['status']='None'
		return result

class triples():
	def __init__(self,ent):
		self.ent=ent
	def search(self):
		if(self.ent==''):
			return None
		else:
			cursor=dbp.triples.find({'s':self.ent})
			rl=[]
			result={}
			if(cursor.count()):
				for i in cursor:
					rl.append([i['s'],i['p'],i['o']])
				result['status']='Ok'
				result['return']=rl
			else:
				result['status']='None'
				result['return']=rl
			return result
