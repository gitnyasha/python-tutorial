from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dayname = day[datetime.now().weekday()]
    return f'<h1>Hello, World! Happy {dayname}</h1>'
