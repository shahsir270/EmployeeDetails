
# Employee Register App



## API Reference


#### register employee

```
  GET /employee/ -- for get form
  POST  /employee/ -- for create
```

#### details of employee
##### here you can get employee details through email and you can delete and update employee details

```
  GET /employee/<email>/ -- for get data
  PUT /employee/<email>/ -- for update data
  DELETE /employee/<email> -- for delete data
 
```

## Usage

It's best to install Python projects in a Virtual Environment. Once you have set up a VE, clone this project

```
 git clone https://github.com/shahsir270/EmployeeDetails.git
```

```
  pip install -r requirements.txt #install required packages
  python manage.py migrate # run first migration
  python manage.py runserver # run the server
```
