from lesson11.app import app
import lesson11.controllers as controllers
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

@app.route("/update/<int:from_currency>/<int:to_currency>")
@app.route("/update/all")
def update_xrates(from_currency=None, to_currency=None):
    return controllers.UpdateRates().call(from_currency, to_currency)

@app.route("/logs")
def view_logs():
    return controllers.ViewLogs().call()


