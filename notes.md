## NOTE: These notes are for early development purposes and should probably just be thrown away at this point. 

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



