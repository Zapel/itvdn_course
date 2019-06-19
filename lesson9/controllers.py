from flask import render_template, make_response
from lesson9.models import XRate

def gee_all_rates():
    try:
        xrates = XRate.select()
        return render_template("xrates.html", xrates=xrates)
    except Exception as ex:
        return make_response(str(ex), 500)

