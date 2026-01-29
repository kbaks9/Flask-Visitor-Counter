from flask import Flask, render_template
import redis
import os

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/count')
def count():
    visitor_count = r.incr('visits')  # define visitor_count variable
    return render_template('count.html', count=visitor_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)