import redis, json
r = redis.Redis()
ret = json.loads(r.get("jsonorg_example").decode("utf-8"))
print(ret)