import os
import redis
from flask import request, abort

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')
username = os.getenv('REDIS_USERNAME')
password = os.getenv('REDIS_PASSWORD')

# Connect to remote Redis instance
redis_client = redis.Redis(
  host=host,
  port=port,
  username=username,
  password=password)

RATE_LIMIT = 30  # 60 requests per minute
RATE_LIMIT_WINDOW = 60  # 1 minute window


def enforce_rate_limit():
    ip_address = request.remote_addr

    rate_limit_key = f"rate_limit:{ip_address}"
    redis_client.incr(rate_limit_key)
    redis_client.expire(rate_limit_key, RATE_LIMIT_WINDOW)
    request_count = int(redis_client.get(rate_limit_key) or 0)

    if request_count > RATE_LIMIT:
        abort(429, "Rate limit exceeded")
