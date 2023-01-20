

def count_people(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for line in f :
            count += 1
    return count

def count_unique_people(file_name):
    names = set()
    with open(file_name, 'r') as f:
        for name in f :
            names.add(name)
    return len(names)



def main():
    file_name = 'data01.txt'
    print(count_unique_people(file_name))

if __name__ == '__main__':
    main()