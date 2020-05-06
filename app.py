from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user1'
app.config['MYSQL_PASSWORD'] = '*******'
app.config['MYSQL_DB'] = 'AIGAMING'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        email = details['email']
        #lastName = details['lname']
        cur = mysql.connection.cursor()
        temp = cur.execute('SELECT * FROM coupon WHERE email_id = %s', [email])
        #mysql.connection.commit()
        #cur.close()
        #acc = cur.fetchall()
        if temp > 0:
        	acc = cur.fetchall()
        	#return render_template('users.html',userDetails=userDetails)
        	print(acc)
        	return acc[0][1]

        	#return render_template('users.html',acc=acc)
        	#return 'success'
        else:
        	return 'Not found'
    return render_template('index.html')





#cursor.execute('SELECT * FROM coupon WHERE email = %s', email)






'''from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
#import yaml

app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user1'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'AIGAMING'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        #name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        #cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True) '''
