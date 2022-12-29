import json
from fastapi import FastAPI
from starlette import requests
from starlette.config import Config
from starlette.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
import requests
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], #http://localhost:3000
    allow_methods=['*'],
    allow_headers=['*']
)

FRONT_END_URL = 'http://127.0.0.1:3000/'
USER_SERVER_URL = 'http://127.0.0.1:8000'
BOOK_SERVER_URL = 'http://127.0.0.1:8001'
ORDER_SERVER_URL = 'http://127.0.0.1:8002'

HOST = '127.0.0.1'
PORT = 5000

GOOGLE_CLIENT_ID = "YOUR GOOGLE_CLIENT_ID"
GOOGLE_CLIENT_SECRET = "YOUR GOOGLE_CLIENT_SECRET"
app.add_middleware(SessionMiddleware, secret_key="!secret")

oauth = OAuth()

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@app.get('/')
async def homepage(request: Request):
    user = request.session.get('user')
    return HTMLResponse('<a href="/login">Click here to login with Google...</a>')


@app.get('/login')
async def login(request: Request):
    redirect_uri = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as error:
        return HTMLResponse(f'<h1>{error.error}</h1>')
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user) # email = user["email"]
        response = requests.post(USER_SERVER_URL + '/users/search-by-email', json=json.dumps(user))
        compare1 = response.json()
        print(compare1)
        if compare1 is None: # not find that person
            newUser = {"email": user["email"], "address": 'unknown'}
            addon = requests.post(USER_SERVER_URL + '/users/json', json=json.dumps(newUser))
            compare2 = addon.json()
            print(compare2)
            userid2 = compare2['user'][0]['user_id']
            print(userid2)
            target = FRONT_END_URL+str(userid2)
            return RedirectResponse(url=target)
        else:
            userid1 = compare1['user'][0]['user_id']
            print(userid1)
            target = FRONT_END_URL+str(userid1)
            return RedirectResponse(url=target)


if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT)