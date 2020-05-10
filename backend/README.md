# CareDash Backend 
#### Anooj Shah

## Project Directory
`CareDash.py` contains the API. On line 12 in `caredash.py`, the `SQLALCHEMY_DATANASE_URI` can be changes to any database including but not limited to MySQL, PostgreSQL, Oracle, SQLite, etc...
`app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # CHANGE to MySQL URI, PostgreSQL URI, etc...`
In `caredash.py`, I left it as SQLite so it can run without having to put a username and password. However, please feel free to change it to the URI of your preferred database. 

`test.sh` is a test bash file that allows your to validate the API. 

## How to Deploy 
`run-app.sh` includes the bash code to deploy the API. To run (MacOS), perform the following command:
`sh run-app.sh PORT_NUMBER`

This command will install the python packages via pip. It will also run `setup.py` as this will delete the database (if it already exists) and then it will create a new one. Then it will run the flask application on the specified port number. NOTE: All tests in `test.sh` are for Port 3000. 

## Design Considerations
Currently, the Reviews table has a primary key column called "id" which is automatically inserted each time an insert/POST operation occurs. This means that each row in the Reviews table is unique. I have made an **assumption** that each review id is supposed to be **unique globally rather than indexed at 1** for each doctor. 
