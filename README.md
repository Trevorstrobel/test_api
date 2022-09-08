Author: Trevor Strobel <br> Date: 9/7/2022
# Test API

## About
This repository houses an API that allows the user to create, read, list, update, and delete objects called Widget's from a local SQLite databse. All instructions are written assuming the user has access to a terminal and a bash shell or something comparable. The download commands assume the user has the Aptitude package manager. This document also assumes that your machine has Python version 3.8 or higher installed as most OS's ship with Python installed.

<br>

## Installation
### Pip - The Python Package Installer

The Test API relies on a few libraries to function properly. To install these libraries, we need to leverage a tool called Pip. Install pip with the following command:

`sudo apt install python3-pip`
<br>


### SQLite 
Most modern operating systems ship with SQLite installed, but if you don't have it, you can install it with the following command:

`sudo apt install sqlite`

<br>

## Configuration
It is recommended to use a virtual environment so as not to clutter your machine with dependencies after you're done using this API. For information on how to do that, click [HERE](https://docs.python.org/3/library/venv.html)

<br>

Next, clone the repository to your machine. See [HERE](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for instructions on how to do that. 



With the repository cloned, change the working directory to "test_api" and run the following command to install all other necessary prerequisites:

`pip3 install -r requirements.txt`



## Running the API

To activate the API, you need only use the following command:

`python3 run.py`

<br><br><br>

# API Usage

This API fulfills five main functions regarding the manipulation of Widgets. Those functions are: **create, read, list, update, and delete**. 

### **Create and Update**
Create and update work very similarly, and are grouped together on the same endpoint. A request made to that endpoint would look something like this:

`POST localhost:5000/widget/name/parts/`

where name is the name of the widget, and parts are the number (Integer) of parts in the widget. If a widget with that name does not exist, a new record will be made in the database. If a record already exists with that name, the record will be updated. 

### **Read and Delete**
Reading or Deleting an entry from the database is as simple as specifying the name of the widget. The only difference is the HTTP Verb used on the endpoint. A read request would look as follows:

`GET localhost:5000/widget/name/`


where name is the name of the widget. If the widget does not exist, then a message is returned explaining that the record does not exist. 

A delete request would look as follows:

`DELETE localhost:5000/widget/name/`

where name is the name of the widget. If the widget does not exist, then a message is returned explaining that the record does not exist. 

### **List**

Finally, the list functionallity returns a JSON object containing the information on all of the rows of the database. A List request would look like this:

`GET localhost:5000/widget/`

