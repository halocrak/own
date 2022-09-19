from flask import (
    Flask
)
import requests
import json
app=Flask(__name__)
@app.route('/user=<string:username>')
def halo(username):
    hedi= str(requests.get(f"https://www.snapchat.com//add/{username}").status_code)
    mrx=(f"CODE : {hedi} USER : {username} CODE BY : i4m_mrx")
    return mrx
@app.route('/user/')
def halom():
    return "not found user"
if __name__ =='__main__':
    app.run(
        host='0.0.0.0',
        debug=False
    )
