logins_map = {"Kseniia": "ksu18", "Alexey": "alex74"}

name = "Kseniia"
login = logins_map[name]
print(login)

name = "Vitaly"
# login = logins_map[name]

login = logins_map.get(name, "Undefinet")
print(login)

# login = logins_map(name, name)
# print(login)

def get_from_dict(name):
    if name in logins_map:
        return logins_map[name]
    else:
        return "default value"
print(get_from_dict("Kseniia"))
print(get_from_dict("Vitaly"))



