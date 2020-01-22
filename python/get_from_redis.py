from rejson import Client, Path
try:
    rj = Client(host='localhost', port=6379, decode_responses=True)
    ret = rj.jsonget('jsonorg_example', Path('.glossary'))
    print(ret)
except Exception as e:
    print("Exception: {}".format(e))