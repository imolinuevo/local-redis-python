import redis, json
try:
    r = redis.Redis()
    with open('jsonorg-example.json') as data_file:
        data = json.load(data_file)
    ret = r.set('jsonorg_example', json.dumps(data))
    print(str(ret))
except Exception as e:
    print("Exception: {}".format(e))