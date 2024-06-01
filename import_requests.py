import requests
import base64 

CLIENT_ID = '0e400e60659b466780d38ea32396a156'
CLIENT_SECRET = '2cded03a54ae48eab27aa551e7c2dc1d'

client_credentials = f'{CLIENT_ID}:{CLIENT_SECRET}'
client_credentials_base64 = base64.b64encode(client_credentials.encode())


token_url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': f'Basic {client_credentials_base64.decode()}'
}

data = {
    'grant_type': 'client_credentials'
}


response = requests.post(token_url, data=data, headers=headers)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print("Access token obtained successfully.")
else:
    print("Error obtaining access token.")
    exit()