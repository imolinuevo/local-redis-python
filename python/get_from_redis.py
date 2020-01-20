import redis, json
try:
    r = redis.Redis()
    ret = json.loads(r.get("jsonorg_example").decode("utf-8"))
    print(ret)
except Exception as e:
    print("Exception: {}".format(e))