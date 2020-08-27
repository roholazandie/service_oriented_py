# Service Oriented Programming in Python
![Alt text](xmlrpc_diagram1.png)

In this repository we explore the service-oriented programming using python. I tried to
implement it in a way that the services can be added/removed on the fly using the services_config.yml

## How to run?
Run the server:
```
python xmlrpc_server.py
```

Run the client:
```
python xmlrpc_client.py
```


## Use Flask as server
We also included the flask as a proxy to access the services without direct interactions with the XMLRPC and through 
curl. For this run the server:
```
python xmlrpc_server.py
```
Run the flask:
```
python flask_server.py
```
You should [download](https://github.com/roholazandie/sentiment_classification) the models if you want to use the sentiment analysis service, because it's a local service:

Send the curl commands:
```
curl --header "Content-Type: application/json" --request POST --data '{"text":"I love this life."}' http://localhost:5000/api/ask_sentiment
```
```
curl --header "Content-Type: application/json" --request POST --data '{"text":"I would love to, yes!", "concepts": ["yes", "no"]}' http://localhost:5000/api/ask_semantic_similarity_with_concepts
```
```
curl --header "Content-Type: application/json" --request POST --data '{"text":"This is a good game"}' http://localhost:5000/api/ask_gpt
```
```
curl --header "Content-Type: application/json" --request POST --data '{"text":"Einstein"}' http://localhost:5000/api/ask_wikipedia
```
```
curl --header "Content-Type: application/json" --request POST --data '{"text":"London,GB"}' http://localhost:5000/api/ask_weather
```
