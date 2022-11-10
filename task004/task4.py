from flask import Flask
from flask import request
from flask import Response
import requests
 
TOKEN = "5756091450:AAFE4mOPjH5hDB3YE084mslJGhLk-uq45CE"
app = Flask(__name__)
 
 
@app.route('/', methods=[ 'POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()
       
        print("message-->",message)
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)
        
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        payload = {
                    'chat_id': chat_id,
                    'text': txt
                    }
    
        requests.post(url,json=payload)
        
       
        return Response('ok', status=200)
    
 
if __name__ == '__main__':
   app.run(threaded=True)