def throw_if_true(param):
    try:
        if param:
            raise OSError("test exception")
    except OSError:
        print("except")
    else:
        print("else")


throw_if_true(True)
throw_if_true(False)
