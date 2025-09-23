import time
import json
import traceback
 
class RedisWorkerListener:
    def __init__(self, queue_name, dispatcher, redis_client):
        self.queue = queue_name
        self.dispatcher = dispatcher
        self.r = redis_client
 
    def run(self):
        print("[WorkerListener] ----- Worker listener started ----- ")
 
        while True:
            try:
                _, job_json = self.r.brpop(self.queue, timeout=0)
                job = json.loads(job_json)
 
                job_id = job["id"]
                task_type = job["type"]
                payload = job["payload"]
 
                print(f"[WorkerListener] ----- Job {job_id} [{task_type}] ----- ")
 
                self.r.set(f"status:{job_id}", "running")
 
                try:
                    result = self.dispatcher.dispatch(task_type, payload)
                    self.r.set(f"result:{job_id}", json.dumps({"success": True, "data": result}))
                    self.r.set(f"status:{job_id}", "done")
                    print(f"[WorkerListener] ----- Job {job_id} completed ----- ")
 
                except Exception as task_err:
                    self.r.set(f"result:{job_id}", json.dumps({"success": False, "error": str(task_err)}))
                    self.r.set(f"status:{job_id}", "failed")
                    print(f"[WorkerListener] !!!!! Job {job_id} failed: {task_err} !!!!!")
                    traceback.print_exc()
 
            except Exception as err:
                print(f"[WorkerListener] !!!!! Fatal error: {err} !!!!! ")
                traceback.print_exc()
                time.sleep(2)