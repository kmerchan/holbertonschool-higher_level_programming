#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return (fct(*args))
    except (IndexError, TypeError, ValueError,
            ZeroDivisionError, NameError) as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return (None)
