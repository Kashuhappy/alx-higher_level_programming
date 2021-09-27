#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        var = fct(*args)
        return var
    except exception as e:
        print("Exception: {}".format(e), filr=sys.stderr)
        return None
