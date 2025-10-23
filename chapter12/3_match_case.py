
   # match case :

def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal servar erroe"
        case _:
            return "not found "

print(http_status(1000))