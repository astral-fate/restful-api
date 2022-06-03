from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<h1>hello world!</h1>"




class AddNumbers(Resource):
    def post(itself):
        PostedData=request.get_json()
        x =PostedData["x"]
        y=PostedData["y"]
        x=int(x)
        y=int(y)
        sum = x+y
        retJson = {
        "add": sum
        }
        return jsonify(retJson)



api.add_resource(AddNumbers,"/Add")



if __name__=="__main":
    app.run(debug=True)


#if __name__ == "__main__":
#create_app().run()


"""
@app.route("/saymornin")
def say_mornin():
    to_do_list=['Breakfast', 'Urdu', 'Journling', 'Workout', 'Python']
    daylist=' '.join(to_do_list)
    age=10*2

    info = {'name': 'Fatma',
             'age': age,
             'avtivites': daylist}

    return jsonify(info)



@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
    dataDict=request.get_json()

    return jsonify(dataDict)
"""
