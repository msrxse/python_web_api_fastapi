# python_web_api_fastapi

We are building an event planner application. In this application, registered users will be able to 
create, update, and delete events. Events created can be viewed by navigating to the event page created 
automatically by the application.

## Activate your virtual environment and start your application

```
source venv/bin/activate

uvicorn api:app --port 8080 --reload
```

### to create same file in several existing folders

```
touch {database,routes,models}/__init__.py
```

### To create 2 same files in 2 different folders

```
touch {routes,models}/{events,users}.py
```

