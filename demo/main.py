import user_pb2

user = user_pb2.User()
# user.id = 12
user.name = "eucyt"
user.num.extend([1, 10])
binary = user.SerializeToString()
print(" ".join([f'{x:08b}' for x in binary]))