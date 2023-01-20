def triangle(size):
    """ This function must print a triangle using the # character on the screen.

    Example:
    >>> triangle(5)
    #
    ##
    ###
    ####
    #####

    """
    for i in range(1, size):    
        print('#'*i)
    print()


def rectangle(width, height):
    """ This function must print a rectangle with the correct dimensions on the screen with #.

    !!! The rectangle is not filled with # !!!

    Examples:
    >>> rectangle(0, 0)
    
    >>> rectangle(1, 1)
    #
    
    >>> rectangle(3, 1)
    ###
    
    >>> rectangle(10, 3)
    ##########
    #        #
    ##########

    """
    print('#'*width)
    for i in range(0, height-2):
        print('#',' '*(width - 4),'#')
    if height > 1:
        print('#'*width)
    print()

if __name__ == "__main__":
    triangle(0)
    triangle(10)

    rectangle(4, 4)
    rectangle(-1, -1)
