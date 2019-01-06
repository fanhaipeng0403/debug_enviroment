from service import Message_pb2


def do_something():
    foo = Message_pb2.WSMessage()
    foo.id = '121321'
    foo.content = '44142'
    foo.sender = '5523'
    foo.time = '555'


do_something()
