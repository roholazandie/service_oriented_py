from xmlrpc.client import ServerProxy

client = ServerProxy('http://localhost:3000')
r = client.wikipedia.ask_wikipedia("Einstein")
print(r)


r = client.gpt2.complete("I am going")
print(r)

r = client.weather.get_temperature("London,GB")
print(r)