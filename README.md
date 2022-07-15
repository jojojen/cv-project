# cv-project
computer vision

# before run on Mac

`cd cv-project`

`python3 -m venv venv`

`. venv/bin/activate`

`pip install -r requirements.txt`

# local run

1. flask run

`export FLASK_APP=app`

`export FLASK_ENV=development`

`flask run`

2. run with gunicorn

`gunicorn --bind 0.0.0.0:5000 app:app`

---

then go to http://localhost:5000/

# leave env

`deactivate`