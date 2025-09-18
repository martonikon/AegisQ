from dotenv import load_dotenv
import os
import redis
 
from worker.listener import RedisWorkerListener
from worker.dispatcher import TaskDispatcher
 
load_dotenv()
 
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True
)
 
def main():
    listener = RedisWorkerListener(
        queue_name="job_queue",
        dispatcher=TaskDispatcher(),
        redis_client=r
    )
loop.run()
 
if __name__ == "__main__":
    main()