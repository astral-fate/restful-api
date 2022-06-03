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


We install flask_restful as follows

      pip3 install flask-restful
      
to check it was installed
      python3
      import flask_restful as fr
      
![image](https://user-images.githubusercontent.com/63984422/171782651-7b35571c-ebd1-4410-bce9-5753b609a188.png)
      


