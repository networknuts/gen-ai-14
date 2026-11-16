import uuid
import redis 

# SETUP THE REDIS CONNECTION
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# GENERATE PAYLOAD AND SEND TO REDIS
def upload_payload(query):
    job_id = str(uuid.uuid4())
    payload = {
        "job_id": job_id,
        "query": query
    }
    queue_name = "rag:requests"
    redis_client.rpush(queue_name,str(payload))
    return job_id

# ASK FOR CUSTOMER QUERY
human_query = input("Human Query: ")

# SEND QUERY TO REDIS
job = upload_payload(human_query)
print("QUERY SENT TO REDIS SUCCESSFULLY")
print(job)
