from lesson9.app import app
import lesson9.controllers


@app.route("/")
def hello():
    return "Hello everybody!"

@app.route("/xrates")
def view_rates():
    return lesson9.controllers.gee_all_rates()
