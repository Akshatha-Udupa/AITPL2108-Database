from flask import Flask ,Response ,request ,render_template, url_for, escape, session, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Password123@",
  database="db"
)
cursor = connection.cursor()
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM login WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            msg = "Login Successful"
            return render_template('1stpage.html')
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor.execute('INSERT into login values(%s, %s)',(username, password))
        connection.commit()
        print("done")
    return render_template('register.html', msg=msg)




if __name__ == '__main__':
    app.run(debug=True)
