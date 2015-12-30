# _*_ coding: utf-8 _*_

from flask import Flask , render_template
app = Flask(__name__)

@app.route("/gg/<name>")
def hello(name):
	return "hello %s"%name

@app.route("/test")
def test():
	return "test world"

if __name__ == '__main__':
	app.run()