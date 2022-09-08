## NOTE: These notes are for early development purposes and should probably just be thrown away at this point. 

## Note: These were the instructions given for the assignment and are not usefull to anyone but the author. 



Write a CRUD REST API using Python for a single resource type. You may use a framework (we use Tornado, but that is not required for this assessment).

The application must satisfy these requirements:

1.Written in Python 3.8 or later.
2. Endpoints to create, read, list, update, and delete objects called "Widgets"
3. Widget objects include the following properties (at least):
    1. Name (utf8 string, limited to 64 chars)
    2. Number of parts (integer)
    3. Created date (date, automatically set)
    4. Updated date (date, automatically set)

4. Widgets are persisted to and retrieved from a SQLite file database.
5. Include a README that describes how to setup and run the application.


Ideas to make the project even better:

- Include unit or functional test coverage
- Include an OpenAPI spec
- PEP8 compliance
- Pass standard lint tests (ie: flake8 or similar)
- Pass bandit security analysis
- Use Python type annotations


Please send your public github repository, with your completed assessment, to scottm@aweber.com within a week.




# Notes 
The common API endpoint for widgets is as follows:

`localhost/widgets`

by specifying the HTTP verb and passing or not passing associated data, we can infer
what the user is tyring to do and keep the API nice and tidy. 

For example:

`HTTP POST : localhost/widgets/name/parts` along with widget data will either create or update existing entry. **widget names are unique**

`HTTP GET : localhost/widgets` will return a list of all widgets. When specifying any data, it will return relavent widgets

`HTTP DELETE : localhost/widgets` along with widget data will delete the record from the database.





## Datbase Design

### Widgets Table

Row = Widget <br>
 - ID
 - Name (unique, utf8, <= 64 char)
 - Number of parts (integer)
 - Created date (SQLite Date)
 - Updated Date (SQLite Date)



