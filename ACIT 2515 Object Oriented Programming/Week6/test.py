

def func(value, *args, quiz=None, **kwargs):
    return f"{len(args)} - {kwargs["example"]}"

# my_dict = {"value": "1", "example": 10}
# print(func(**my_dict))


# my_list = ["value", "quiz"]
# my_dict = {"example": 10}
# print(func(*my_list, **my_dict))


# my_dict = {"value": "1", "quiz": True}
# print(func(**my_dict, example=10))


# # my_dict = {"value": "1", [], "example": 10}
# # func(**my_dict)

# def func(value, *args, quiz=None, **kwargs):
#     return f"{len(args)} - {kwargs["example"]}"

# my_list = ["example", [1, 2, 3, 4], {"quiz": True}]

# def func(value, *args):
#     return args[0][2]

# print(func(*my_list))

def func(value, **kwargs):
  return kwargs["value"]

my_dict = {"value": "quiz", "value": "quiz2", "example": 10}
answer = func(**my_dict)