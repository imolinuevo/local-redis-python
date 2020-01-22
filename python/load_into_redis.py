from rejson import Client, Path
import json

try:
    rj = Client(host='localhost', port=6379, decode_responses=True)
    with open('jsonorg-example.json') as data_file:
        data = json.load(data_file)
    print(str(type(data)))
    ret = rj.jsonset('jsonorg_example', Path.rootPath(), data)
    print(str(ret))
except Exception as e:
    print("Exception: {}".format(e))