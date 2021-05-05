#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    x = None
    try:
        x = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: " + str(e) + "\n")
    return x
