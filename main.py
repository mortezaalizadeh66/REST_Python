import requests
import pandas as pd
import json

data = {
    "transactionId": "6",
    "type": "PURCHASE",
    "amount": "2000"
}

url = 'https://d83o3hcaf5.execute-api.us-east-1.amazonaws.com/test/trr'
query_params = '&'.join([f"{key}={value}" for key, value in data.items()])

response = requests.get(url + '?' + query_params)
#text to json
json_data = json.loads(response.text.replace("'", "\""))
#Json to Matrix
#df = pd.DataFrame.from_dict([json_data])
#print(df)
print("TransactionId", json_data['transactionId'])
print("type", json_data['type'])
print("amount", json_data['amount'])
print("Message", json_data['message'])
