from flask import Flask

app = Flask(__name__)
print("app=", app)

import lesson9.views