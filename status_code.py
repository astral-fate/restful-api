from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    return "<h1>hello world!</h1>"


def checkPostedData(PostedData, functionName):
    if (functionName=="AddNumbers"):
        if "x" not in PostedData or "y" not in PostedData:
            return 301
        else:

            return 200


class AddNumbers(Resource):
    def post(self):
        PostedData=request.get_json();

        #checking if it's posted

        status_code = checkPostedData(PostedData, "AddNumbers");



        if (status_code!=200):
            retJson = {
            "Message": "An error happend",
            "Status": status_code
            }
            return jsonify(retJson)


        x =PostedData["x"]
        y=PostedData["y"]
        x=int(x)
        y=int(y)
        sum = x+y
        retMap = {
        "add": sum

        }


        return jsonify(retMap)












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
    dataDict=request._json()

    return jsonify(dataDict)
"""
