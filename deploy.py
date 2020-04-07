from flask import Flask

app = Flask(__name__)

import pymysql
from flask import jsonify
from flask import flash, request


from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'GDya0c7r3q'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ne5S5N7u08'
app.config['MYSQL_DATABASE_DB'] = 'GDya0c7r3q'
app.config['MYSQL_DATABASE_HOST'] = 'remotemysql.com'
mysql.init_app(app)
		
@app.route('/users')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user")
		rows = cursor.fetchall()
		message = {
			
			'status': 404,
			'data' : rows,
			'message': 'Not Found: ' + request.url,
			
		}
		resp = jsonify(message)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/select/<int:id>')
def select(id):
	try:
		page = id * 10 - 10
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user LIMIT %s ,10", page)
		rows = cursor.fetchall()
		message = {

			'status': 404,
			'data' : rows,
			'message': 'Not Found: ' + request.url,
			
		}
		resp = jsonify(message)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/user/<int:id>')
def user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()
