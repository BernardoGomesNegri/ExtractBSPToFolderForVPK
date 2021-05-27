import sys

def print_ex(e: Exception):
    print(e)
    type, value, traceback = sys.exc_info()
    print(str(type))
    print(str(value))
    print(str(traceback))

    # We can try to do more advanced stuff later
