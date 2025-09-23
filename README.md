# 🛡️ AegisQ – Asynchronous Python Job Queue with Redis

## 💡 What is AegisQ?

AegisQ is a lightweight, FastAPI-powered asynchronous job queue system written in Python, designed for real-world microservices. It allows you to submit time consuming and blocking jobs as background jobs (like text cleaning, resizing,file operations, some AI tasks, etc.), track their progress, and fetch results when they're ready.

✅ Modular  
✅ Dockerized  
✅ Redis-backed  
✅ Realistic architecture for cloud-native workloads

---

## 🧠 Why AegisQ?

In real systems, you don’t want to block your API waiting for a long task (like ML inference, data cleaning or file operations). AegisQ separates job submission from processing with:

- A FastAPI interface (for submitting jobs and checking results)
- A Redis-backed queue
- A decoupled Python worker that pulls from Redis
- Docker & Compose to simulate real deployments

---

## 🏗️ Architecture

```
[Client] --> [FastAPI (api)] --> [Redis Queue] <-- [Python Worker]
```

- `api/`: FastAPI routes to submit, track, and fetch job results  
- `worker/`: Background service that listens to Redis, executes tasks  
- `tasks/`: Collection of real-world task modules (cleaning, resizing, etc.)  
- `docker-compose.yml`: Container orchestration  
- `.env`: Centralized config (REDIS_HOST, PORT, etc.)  

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/martonikon/AegisQ.git
cd AegisQ

# 2. Copy example env
cp .env.example .env

# 3. Start all services
docker compose up --build

# 4. Access FastAPI docs
http://localhost:8000/docs
```

---

## 🧪 Sample Request

### POST `/submit_job`

```json
{
  "task_type": "clean_text",
  "payload": {
    "text": "  <h1>Hello World!</h1> Clean me up!   "
  }
}
```

### GET `/status/{job_id}`  
Check status: `queued`, `processing`, or `completed`

### GET `/result/{job_id}`  
Returns result (e.g. cleaned text)

---

## 🧩 Supported Task Types

| Task        | Description                       |
|-------------|-----------------------------------|
| `clean_text`| HTML tag removal + text cleaning |


---

## 📦 Project Structure

```
AegisQ/
├── api/               # FastAPI app
├── tasks/             # Task definitions
├── worker/            # Worker + dispatcher
├── docker-compose.yml
├── Dockerfile.api
├── Dockerfile.worker
├── .env / .env.example
└── README.md
```

---

## 🤖 How It Works (Internals)

1. You submit a job → It gets a UUID  
2. The job is added to Redis (status: `queued`)  
3. A Python worker listens → pulls from Redis  
4. Worker executes it → updates Redis (`completed`)  
5. You fetch the result by job ID  

---

## 🛠️ Tech Stack

- Python 3.12  
- FastAPI  
- Redis  
- Docker  
- Docker Compose

---

## 👤 Author

- [martonikon](https://github.com/martonikon)  

---

## 📜 License

MIT License