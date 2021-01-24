from flask import Flask,render_template,request,jsonify
from flask_pymongo import PyMongo 
app=Flask(__name__)

app.config["MONGO_DBNAME"]="DEMO1"
app.config["MONGO_URI"]="mongodb://localhost:27017/DEMO1"
mongo = PyMongo(app)
@app.route("/")
def demo1():
    return render_template("index.html")
@app.route("/servers",methods=['POST','GET'])
def server():
    output=[]
    if request.method =="POST":

            framework=mongo.db.DEMO1
            name=request.form['name']
            img=request.form['img']
            summary=request.form['summary']
            framework_id=framework.insert({'name':name,'img':img,'summary':summary})
            new_framework=framework.find_one({'_id':framework_id})
            output={'name':new_framework['name'], 'img':new_framework['img'],'summary':new_framework['summary']}
    
            return render_template('server.html',result=output)
    else:
        return render_template('server.html')
@app.route("/insert",methods=['POST','GET'])
def insert():
            output=[]
    

            framework=mongo.db.DEMO1
            name=request.json['name']
            img=request.json['img']
            summary=request.json['summary']
            framework_id=framework.insert({'name':name,'img':img,'summary':summary})
            new_framework=framework.find_one({'_id':framework_id})
            output={'name':new_framework['name'], 'img':new_framework['img'],'summary':new_framework['summary']}
            
            return jsonify({'result':output})
app.run(debug=True)