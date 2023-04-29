from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.htm')

@app.route('/display/')
def new_emp():
    return render_template('display.htm')

@app.route('/registration/', methods = ['POST', 'GET'])
def registration_page():
    msg = ''
    if request.method == 'POST':

        try:
            empID = request.form['id']
            empName = request.form['name']
            empGender = request.form['gender']
            empPhone = request.form['phone']
            empBdate = request.form['bdate']

            with sqlite3.connect('/home/emre/week11working/week11/employee.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO information (EmpID, EmpName, EmpGender, EmpPhone, EmpBdate) VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format(empID, empName, empGender, empPhone, empBdate))
                con.commit()
                msg = "Record successfully added"
                con.close()

        except:
            #print("In except statement")
            con.rollback()
            msg = "Error in insert operation"
            con.close()
        finally:
            #print("In finally statement")
            return render_template("reg.htm", msg = msg)




@app.route('/info/')
def information_page():
    con = sqlite3.connect('/home/emre/week11working/week11/employee.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM information;")

    rows = cur.fetchall()
    return render_template('info.htm', rows = rows)

if __name__ == "main":
    app.run(debug == True)
