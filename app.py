from flask import Flask, render_template, request

app = Flask(__name__)

HARD_CODED_USERNAME = "abc"
HARD_CODED_PASSWORD = "123"

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/login")
def log():
    return render_template('login.html')  

@app.route("/signup")
def signup():
    return render_template('signup.html') 

@app.route('/loginData', methods=['POST'])
def OnsubmitFunction():
    msg = ""  

    if request.method == 'POST': 
        username = request.form.get('username') 
        password = request.form.get('password')

        if username == HARD_CODED_USERNAME and password == HARD_CODED_PASSWORD:
            msg = "Login successful!"
        else:
            msg = "Invalid username or password. Try again."

    return render_template('login.html', message=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
