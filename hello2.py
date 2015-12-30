# _*_ coding : utf-8 _*_
from flask import Flask ,render_template , request
# import MySQLdb as mysql
# db = mysql.connect(host="localhost" , user="root" , passwd="soft2015" , db="dbDemonstration")
# # from flaskext.mysql import MySQL
# # mysql = MySQL()
app = Flask(__name__)

# app.config['MYSQL_DATABASE_HOST'] ='223.195.109.208'
# app.config['MYSQL_DATABASE_USER'] ='root'
# app.config['MYSQL_DATABASE_PASSWORD'] ='soft2015'
# app.config['MYSQL_DATABASE_DB'] ='dbDemonstration'
# mysql.init_app(app)

@app.route("/start3")
def test3():
	return render_template('start3.html')

@app.route("/start2")
def test2():
	return render_template('start2.html')

@app.route("/start")
def test():
	return render_template('start.html')

@app.route("/")
def hello():
	return render_template('test.html')

# @app.route("/db")
# def dbcn():
# 	cursor = db.cursor()
# 	cursor.execute("set names utf8")
# 	cursor.execute("SELECT VERSION()")
# 	data = cursor.fetchone()
# 	return data

	# username = request.args.get('UserName')
	# password = request.args.get('Password')
	# cursor=mysql.connect().cursor()
	# cursor.execute("SELECT * FROM  agora_step1")
	# data= cursor.fetchone()
	# if date is None :
	# 	return "nono"
	# else:
	# 	return "yesyes"




if __name__ == '__main__':
	app.run()

