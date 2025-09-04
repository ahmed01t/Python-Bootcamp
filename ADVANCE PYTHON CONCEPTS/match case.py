def check(status):
    match status:
        case 200:
            return "ok"
        case 300:
            return "not found"
        case 400:
            return "error"
        case _:
            return "unknown status"
print(check(500))