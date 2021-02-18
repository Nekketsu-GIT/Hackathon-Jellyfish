# Hackathon-Jellyfish

This is a simple cryptocurrency notification app in Django using the CoinAPI API. It is composed by:

`accounts:` CREATE, READ, UPDATE, DELETE user and LOGIN/SIGNUP/LOGOUT

`Alerts`:  CREATE, READ, UPDATE, DELETE alerts and provide a front-end to performs operations

Users will receive regular notifications that concern an asset_id based on the alerts they have defined.

###### **Pre-requist:**

-_Data base server_: By default, I connect it to an online mysql database. So if we need to connect to a local or another db we have to modifier databases on setting.py

-_python_: To run app We need a python interpreter. Instruction are given for use a virtual env and i

###### **How to run it**


Clone the project and open it with an IDE. I recommend Pycharm.
Then open a terminal in pycharm and follow this instructions:

_1_. Create va virtual environment and activate it:
 
`virtualenv env`

`.\env\Scripts\activate`

_2_. Install requirements: 

`pip install -r requirements.txt`

_4_. Run the server: 

`python manage.py runserver`

_4_. Run the task scheduler: 

`python manage.py qcluster`



###### **Test User ansd Alert Rest api**

Here is an POSTMAN collection to test the API CRUD for alerts and user:

https://www.getpostman.com/collections/36efcec5b146c544f4df

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/36efcec5b146c544f4df)


