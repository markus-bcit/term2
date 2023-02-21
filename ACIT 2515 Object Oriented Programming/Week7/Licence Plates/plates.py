

def check_plate(plate_name):
    for character in plate_name:
        if character == 0:
            raise KeyError

        
def find_next_plate(plate_name, number=1):
    num1 =  plate_name[:2]
    letters = plate_name[3:5]
    num2 = int(plate_name[6:])
    
    num2 += 1
    if num2 > 100:
        letters = chr(ord(letters[1]) + 1)
        num2 = 11
    elif (num2 % 10) == 0:
        num2 +=1
    
    # Reassemble the new plate and return it
    return f"{num1}-{letters}-{num2}"

    
# check_plate('99-ZZ-z9')