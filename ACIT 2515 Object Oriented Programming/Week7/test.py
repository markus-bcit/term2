

# def main():
#     print('asdf')
    
# if __name__ == '__main__':
#     main()

def func(*args, **kwargs):
    return args, kwargs

my_dict = {"value": "1", "example": 10}
print(func(*my_dict, **my_dict))