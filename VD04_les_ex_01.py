from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/new/")
# @app.route("/newpage/")
# @app.route("/новаястраница/")
# def new():
#     return "new page"

# @app.route("/")
# @app.route("/<password>")
# def hello_world(password=None):
#     return "Доступ разрешен!" if password == "123" else "Доступ ЗАПРЕЩЕН!"

# @app.route("/")
# def hello_world():
#     html = """
#     <h1>Hello World!</h1>
#     <p>Hello World!</p>
#     """
#     return html

@app.route("/")
def first_page():
    return render_template("VD04_les_ex_01.html")

@app.route("/second/")
def second_page():
    return render_template("VD04_les_ex_02.html")



if __name__ == "__main__":
    app.run()