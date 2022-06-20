from ics import Calendar
import requests

from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def index():
    url = "https://urlab.be/events/urlab.ics"
    c = Calendar(requests.get(url).text)
    c.events = [x for x in c.events if "smartmonday" in x.name.lower()]
    return Response(c, mimetype="text/calendar")
