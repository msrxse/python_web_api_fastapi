# python_web_api_fastapi

We are building an event planner application. In this application, registered users will be able to 
create, update, and delete events. Events created can be viewed by navigating to the event page created 
automatically by the application.

## Activate your virtual environment and start your application

```
source venv/bin/activate

python main.py # not "uvicorn api:app --port 8080 --reload" since we use the uvicorn.run() method
```

### to create same file in several existing folders

```
touch {database,routes,models}/__init__.py
```

### To create 2 same files in 2 different folders

```
touch {routes,models}/{events,users}.py
```

## TESTS

### Sign in user

```
curl -X 'POST' \
'http://0.0.0.0:8080/user/signup' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "user@example.com",
"password": "Strong!"
}'
```

### Sign up user

```
curl -X 'POST' \
'http://0.0.0.0:8080/user/signin' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"email": "user@example.com",
"password": "Strong!"
}'
```

### Get all events

```
curl -X 'GET' \
'http://0.0.0.0:8080/event/' \
-H 'accept: application/json'
```

### Post an event

```
curl -X 'POST' \
'http://0.0.0.0:8080/event/new' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "id": 1,
    "title": "FastAPI Book Launch",
    "image": "https://linktomyimage.com/image.png",
    "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
    "tags": [
        "python",
        "fastapi",
        "book",
        "launch"
    ],
    "location": "Google Meet"
}'
```

### Get single event

```
curl -X 'GET' \
'http://0.0.0.0:8080/event/1' \
-H 'accept: application/json'
```

### Delete single route

```
curl -X 'DELETE' \
'http://0.0.0.0:8080/event/1' \
-H 'accept: application/json'
```

### Delete all routes

```
curl -X 'DELETE' \
'http://0.0.0.0:8080/event/' \
-H 'accept: application/json'
```