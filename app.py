from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>hello world!</h1>"

@app.route("/saymornin")
def say_mornin():
    to_do_list=['Breakfast', 'Urdu', 'Journling', 'Workout', 'Python']
    daylist=' '.join(to_do_list)
    age=10*2

    info = {'name': 'Fatma',
             'age': age,
             'avtivites': daylist}

    return jsonify(info)




if __name__ == "__main__":
    app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
