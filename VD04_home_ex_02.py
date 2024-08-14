from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('VD04_home_ex_index.html')

@app.route('/blog/')
def blog():
    return render_template('VD04_home_ex_blog.html')

@app.route('/contacts/')
def contacts():
    return render_template('VD04_home_ex_contacts.html')

if __name__ == '__main__':
    app.run()
