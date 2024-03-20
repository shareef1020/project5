from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return 'you are in homepage'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/index2',methods=['GET'])
def index2():
    return render_template('index2.html')

@app.route('/login-form',methods=['POST'])
def login_form_data():
    num1=request.form['a_val']
    num2=request_form['b_val']
    return{'response':int(num1)+int(num2)}

@app.route('/add',methods=['GET'])
def addition():
    return render_template('add.html')

@app.route('/addition-form',methods=['POST'])
def adding_data():
    num1=request.form['a_val']
    num2=request_form['b_val']
    return{'response':[int(num1)+int(num2)]}

app.run()
