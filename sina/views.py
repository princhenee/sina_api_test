# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponseRedirect
from weibo import APIClient

APP_KEY = '1653219711'            # app key
APP_SECRET = 'd14fa62faf80867d2dfe2375c153acd5'      # app secret
CALLBACK_URL = 'http://127.0.0.1:8000/api/callback/'  # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)

def home(request):
    sina_auth = client.get_authorize_url()    # redirect the user to `url'
    return render(request, 'home.html', locals())

def api(request):
    usertimeline = client.statuses.user_timeline.get()
    return render(request, 'api.html', locals())

def callback(request):
    code = request.GET.get('code')
    r = client.request_access_token(code)
    access_token = r.access_token  # access token，e.g., abc123xyz456
    expires_in = r.expires_in      # token expires in
    client.set_access_token(access_token, expires_in)
    return HttpResponseRedirect('/')

def cancel(request):
    pass

def post_status(request, message):
    pass
