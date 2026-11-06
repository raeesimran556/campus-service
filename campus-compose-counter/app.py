
import os
import time
from flask import Flask
from redis import Redis


app = Flask(__name__)


redis_client = Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

@app.get("/")
def home():
    for attempt in range(10):
        try:
            count = redis_client.incr("visits")
            return f"<h1>Campus Visits: {count}</h1><p>Flask + Redis via Compose</p>"
        except Exception:
            time.sleep(1)

    return "Redis is not ready; please refresh.", 503
