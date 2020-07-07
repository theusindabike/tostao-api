# Tostão API
- Python 3.8

## Install
```console
git clone git@github.com:theusindabike/tostao-api.git
cd tostao-api
python -m venv .tostao-api
source .tostao-api/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test 
```

## Deploy
For an **new** Heroky app
```console
heroku create newinstance
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku confit:set DEBUG=False
#config email
git push heroku master
```

For an **existing** Heroku app
```console
heroku login
heroku git:remote -a tostao-api
```