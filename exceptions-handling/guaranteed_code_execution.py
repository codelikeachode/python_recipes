def throw_if_true(param):
    try:
        if param:
            raise OSError("test exception")
    except OSError:
        print("except")
    finally:
        print("finally")

throw_if_true(True)
# printed: "except" and "finally"
throw_if_true(False)
# printed: "finally"