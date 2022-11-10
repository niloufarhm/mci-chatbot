import os
from flask import Flask, request, abort, jsonify, send_from_directory, Response
import requests
import json
from vosk import Model, KaldiRecognizer
import wave
import json
from base64 import b64decode
import numpy as np
from scipy.io.wavfile import read 
import glob
import shutil

import io
#import ffmpeg
import soundfile as sf
#import IPython
import ast
import subprocess


wf = wave.open('my recording.wav', 'rb')
path='D:\hamrah_pro\\vosk-model-small-fa-0.5'
model=Model(path)
rec=KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)


TOKEN='5610108295:AAFho7IG_xe2DH63lbjrZMpF6jgJIpD9CyM'
app = Flask(__name__)
 
def asr(file_path):
    final_res=""
    wf = wave.open(file_path, 'rb')
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res=ast.literal_eval(rec.FinalResult())
            final_res=final_res+res["text"]
    return final_res

def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r

def tel_upload_file(file_id):
    url = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}'
    a = requests.post(url)
    json_resp = json.loads(a.content)
    print("a-->",a)
    print("json_resp-->",json_resp)
    file_pathh = json_resp['result']['file_path']

    #p=f'D:/hamrah_pro/voice/{user}'
    #if not os.path.exists(p):
     #   os.makedirs(p)
    #file_pathh=f"voice/{user}/{file_unique_id}.oga"
    print("file_path-->", file_pathh)
   
    url_1 = f'https://api.telegram.org/file/bot{TOKEN}/{file_pathh}'
    b = requests.get(url_1)
    file_content = b.content
    with open(file_pathh, "wb") as f:
        f.write(file_content)
    return file_pathh

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
            msg = request.get_json()
            print('msg------>',msg['message'])
            print('keys --->>',msg['message'].keys())
            if 'message'in msg.keys() :
                if 'voice' in msg['message'].keys():
            
                    #file_unique=msg['message']['voice']['file_unique_id']
                    print('msg------>',msg)
                    print()
                    print('voice---->>',msg['message']['voice'])
                    print()
                    file_id=msg['message']['voice']['file_id']
                    chat_id = msg['message']['chat']['id']
                    #user=msg['message']['from']['id']
                    src='D:/hamrah_pro/'+ tel_upload_file(file_id)
                    des = src[:-4]+".wav"
                    print("src",src)
                    print("type",type(src))
                    
                    #f = open(des, 'a+')  # open file in append mode

                    #f.close()
                    cmd=f'ffmpeg -i {src} -ar 16k {des}'
                    process=subprocess.run(cmd.split(' '), shell=True)

                    #process=subprocess.run(['ffmpeg', '-i', src, '-ar' ,'16k' ,des])

                    txt=asr(des)
                    print()
                    print("txt------->",txt)
                    print("type txt : ",type(txt))

                    print()
                    #tel_send_message(chat_id, txt)
                    if len(txt)<5:
                        rsp="ببخشید متوجه نشدم. مجدد تکرار کنید."
                        tel_send_message(chat_id,rsp )
                    else:
                        tel_send_message(chat_id, txt)

                
            return Response('ok', status=200)
            

if __name__ == '__main__':
   app.run(debug=True)