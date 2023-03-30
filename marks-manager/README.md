# Marks Manager

## A Simple Flask based CRUD Application to Store your marks 

### Check the Flask Documentation for createing a flask application
[Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/installation/)
- Create virtual environment
- Initialize the Flask application
- Active the environment
- Configure flask run

 In Terminal type python to open the python shell then execute the following command

```
from app import app,db
with app.app_context():
    db.create_all()
```