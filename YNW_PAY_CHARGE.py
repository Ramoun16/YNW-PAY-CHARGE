import Client

entered_code = int(input())
client = Client()
result = client.checkCode(entered_code)
print(result)
