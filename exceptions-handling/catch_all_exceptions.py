class IsNoneException(Exception):
    pass

class IsEmptyException(Exception):
    pass

def throw_when_null_or_empty(data):
    if data is None:
        raise IsNoneException()
    
    if len(data) == 0:
        raise IsEmptyException()
    
try:
    throw_when_null_or_empty(None)
except Exception as e:
    print("Error happened " + e.__class__.__name__)