from lesson7.api import cbr_api
import importlib

cbr_api_dynamic = importlib.import_module("lesson7.api.cbr_api")

print(cbr_api_dynamic)
print(cbr_api)

print(cbr_api is cbr_api_dynamic)