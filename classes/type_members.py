class ClassProperty(property):
    def __get__(self, cls, owner):
        return self.fget.__get__(None, owner)()
    
class Config:
    __port = 1

    host = "10.0.0.1"

    def get_port(cls):
        return cls.__port
    
    get_port = classmethod(get_port)

    def set_port(cls, value):
        cls.__port = value

    set_port = classmethod(set_port)
    port = ClassProperty(get_port, set_port)

    @classmethod
    def get_connection(cls):
        return f"{cls.host}:{cls.port}"
    
Config.port = 52
connection1 = Config.get_connection()

Config.host = "10.0.0.3"
connection2 = Config.get_connection()

print(connection1)
print(connection2)