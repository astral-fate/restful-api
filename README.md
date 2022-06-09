# restful-api







           sudo apt install python3-flask -y




![image](https://user-images.githubusercontent.com/63984422/149629653-fde5273b-e5a7-4d71-928a-a56bdaec7b72.png)


![image](https://user-images.githubusercontent.com/63984422/149629764-fc8a647d-f8ac-4469-95cf-445988856626.png)




Downlaoding Postman using the follwing commands


     get https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz
     sudo tar -xzf postman.tar.gz -C /opt
     rm postman.tar.gz
     sudo ln -s /opt/Postman/Postman /usr/bin/postman 


     
Then we write

    postman
    
    
it will open the interface for us

![image](https://user-images.githubusercontent.com/63984422/171550401-931f9c50-eb19-488c-80d9-e28439e5c5aa.png)


We tried a POST requset with the following server

     @app.route('/add_two_nums', methods=['POST'])
     def add_two_nums():
        dataDict=request.get_json()
        return jsonify(dataDict)


![image](https://user-images.githubusercontent.com/63984422/171554885-535b5c1c-2517-4ad3-ba40-daf72784d416.png)



## What is a REST-FUL API?

RESTFUL APIs are a style of server, that allow us to interract between the user interface and the requested info from the front-end user, then we procces the requests of the user, to provides the user with a response.



## Installing flask-restful 



We install flask_restful as follows

      pip3 install flask-restful
      
to check it was installed
      python3
      import flask_restful as fr
      
![image](https://user-images.githubusercontent.com/63984422/171782651-7b35571c-ebd1-4410-bce9-5753b609a188.png)
      




## Restful API Resource Method Chart


we have to first import Api, and Resource library from flask

     from flask_restful import Resource, Api
     
     
The resources can either be (+, -, /, * )


## Setting our Api


     
      app = Flask(__name__)
      api = Api(app)
      

## The syntax for creating an api

     Resource(+, -, /, * ) Method(POST, GET, PUT, DELETE) PATH(/NameOfPath) usedfor Parameter ErrorCode
     

## Defining the path 

   api.add_resource(AddNumbers,"/Add")

## Example on RESTFUL API 


We first have to define a class for our Api, for example

     class AddNumber(Resource):
     pass
     
     
     
     class SubNumber(Resource)
     pass
     
     
     class MultyNumber(Resource)
     pass
     
     
     class DivideNumber(Resource)
     pass
     


We  first want to focus on one class, that is AddNumber, hence we will be adding a new function o our class:

     class AddNumbers(Resource):
     def post(itself)
        pass


## Getting the posted data  

step 1: Getting the posted data

        postedData = request.get_json()
        x=postedData["x"]
        y =postedData["y]
        x=int(x)
        y=int(y)
        sum = x+y
        retMap = {

          "Summation": sum
         

         }
         
         
         
![image](https://user-images.githubusercontent.com/63984422/171791179-c2f328cf-e87c-406c-8f3d-8e258885e923.png)
         

step 2: Verify validity of posted data

       def checkPostedData(PostedData, functionName):
           if (functionName=="AddNumbers"):
               if "x" not in PostedData or "y" not in PostedData:
                   return 301
               else:

                   return 200
       
       
       status_code = checkPostedData(postedData, "add")
       
       
       
        if (status_code!=200):
            retJson = {
            "Message": "An error happend",
            "Status": status_code
            }
            return jsonify(retJson)
            
            


 

![image](https://user-images.githubusercontent.com/63984422/171983498-99aa2ac4-b0ef-4afc-8a1a-52eb2c1799ec.png)




## Installing Docker

![image](https://user-images.githubusercontent.com/63984422/171984996-183b6ac9-4b9a-4f55-a87a-13b5c4fb23a4.png)


![image](https://user-images.githubusercontent.com/63984422/171985069-f5c67144-90c2-48bd-9911-743ba1fe4464.png)

![image](https://user-images.githubusercontent.com/63984422/171985628-2eb698cd-780b-41bc-a50c-c72824986001.png)

## Installing Docker Compose

By writing these commands to install Docker Compose verison 2.5 from repositary

  sudo curl -L https://github.com/docker/compose/releases/download/2.5/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose 
  


![image](https://user-images.githubusercontent.com/63984422/171985979-467c5846-ff8b-42c7-8843-5552a007335e.png)


Then we set the path of Docker Compose

 sudo chmod +x /usr/local/bin/docker-compose
  
To check which version we have, we write the following command  

docker-compose --version

![image](https://user-images.githubusercontent.com/63984422/171986131-34a5226d-6cce-4f37-9349-7341c0dd5ab3.png)

