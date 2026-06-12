def add(a, b, c=0):
    try:
        return int(a) + int(b) + int(c)
    except Exception:
        return "error"
