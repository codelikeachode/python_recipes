def method_with_exception():
    try:
        raise Exception("test exception")
    except Exception as ex:
        raise ex


try:
    method_with_exception()
except Exception as e:
    print(e.args[0])
