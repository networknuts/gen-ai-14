import redis

# REDIS CONNECTION
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

job_id = "71a83951-b860-4b32-9afb-043bb76c9e1d"

answer = redis_client.get(job_id)
print(answer)