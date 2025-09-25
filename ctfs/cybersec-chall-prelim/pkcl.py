import pickle
import base64

txt = 1

s = pickle.dumps(txt)

print(base64.b64encode(s).decode('utf-8'))
