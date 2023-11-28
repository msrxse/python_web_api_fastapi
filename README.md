# python_web_api_fastapi


## ensure correct environment is active

```
source venv/bin/activate

```

## To start the server 

```
uvicorn api:app --port 8080 --reload
```

## To test the application you can send a GET request using curl

```
curl -X 'GET' 'http://127.0.0.1:8080/todo' -H 'accept: application/json'
```

## to send a POST request

```
curl -X 'POST' \
'http://127.0.0.1:8080/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "id": 1,
    "item": "First Todo is to finish this book!"
    }'
```

## GET to retrieve passed todo_id

```
curl -X 'GET' \
'http://127.0.0.1:8080/todo/1' \
-H 'accept: application/json'
```

## PUT to update specific todo

```
curl -X 'PUT' \
'http://127.0.0.1:8080/todo/1' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"item": "Read the next chapter of the book."
}'
```

## Delete existing todo

```
curl -X 'DELETE' \
'http://127.0.0.1:8080/todo/1' \
-H 'accept: application/json'
```