import os
import redis
from dotenv import load_dotenv

load_dotenv()

redis_plug = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)
