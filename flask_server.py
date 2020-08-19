from flask import Flask, jsonify, request, make_response
from configs import XMLRPCConfig
from xmlrpc_client import XMLRPCClient



app = Flask(__name__)
config = XMLRPCConfig.from_yaml("services_config.yml")
xmlrpcclinet = XMLRPCClient(config)

@app.route('/api/ask_gpt', methods=['POST'])
def ask_gpt():
    r = request.get_json()
    service_response = xmlrpcclinet.ask_gpt(r['text'])
    response = make_response(jsonify({"response": service_response}))
    return response

@app.route('/api/ask_wikipedia', methods=['POST'])
def ask_wikipedia():
    r = request.get_json()
    service_response = xmlrpcclinet.ask_wikipedia(r['text'])
    response = make_response(jsonify({"response": service_response}))
    return response


@app.route('/api/ask_weather', methods=['POST'])
def ask_weather():
    r = request.get_json()
    service_response = xmlrpcclinet.ask_weather(r['text'])
    response = make_response(jsonify({"response": service_response}))
    return response



if __name__ == '__main__':
   app.run()



#curl --header "Content-Type: application/json" --request POST --data '{"text":"This is a good game"}' http://localhost:5000/api/ask_gpt
#curl --header "Content-Type: application/json" --request POST --data '{"text":"Einstein"}' http://localhost:5000/api/ask_wikipedia
#curl --header "Content-Type: application/json" --request POST --data '{"text":"London,GB"}' http://localhost:5000/api/ask_weather
