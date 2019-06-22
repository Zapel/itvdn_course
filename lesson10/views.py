from lesson10.app import app
import lesson10.controllers as controllers
from flask import request

@app.route("/")
def hello():
    return "Hello everybody!"

@app.route("/xrates")
def view_rates():
    return controllers.ViewAllRates().call()

@app.route("/api/xrates/<fmt>")
def api_rates(fmt):
    return controllers.GetApiRates().call(fmt)

# @app.route("/api/xrates/<fmt>")
# def api_rates(fmt):
#     return f"Raets with format: {fmt}. Args: {request.args}"


