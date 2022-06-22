# Neighbor-Hood

`By Ninah Odoyo`

# Description  
This is a neighborhood app where a user must signup first, be able to join a hood owned by the hood admin, and once you 
join a hood, one can see businesses and posts in only that hood they belong to.  

## User Story  

- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Create businesses and posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

## Setup and Installation  
To get the project .......  

##### Cloning the repository:  
 ```bash 
https://github.com/devninah/neighbourhood
```
##### Navigate into the folder and install requirements  
 ```bash 
cd hood 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m env venv
```  
##### Install Dependencies  
 ```bash 
 python3 env/bin/activate
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate  
 ```bash 
 make migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python3 manage.py run test 
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  

- [Python](https://www.python.org/)  
- [Django](https://docs.djangoproject.com/en/2.2/)  
- [Heroku](https://heroku.com)  

## Contact Information   


-   Email- [Ninah Odoyo]
(mailto:ododyoninah@gmail.com)
-   Linkedin - [Ninah Odoyo](https://www.linkedin.com/in/ninahodoyo/)

## License 

* *MIT License:*
* Copyright (c) 2022 **Ninah Odoyo**

[Go Back to the top](#Neighbor-Hood)