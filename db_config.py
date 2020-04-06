from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'GDya0c7r3q'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ne5S5N7u08'
app.config['MYSQL_DATABASE_DB'] = 'GDya0c7r3q'
app.config['MYSQL_DATABASE_HOST'] = 'remotemysql.com'
mysql.init_app(app)