import time
import itertools
import numpy as np

# lst is a list of sets (or empty)
# As we bring in original and rotated_values, we have to add them to a set
# and append to the lst
# If the rotated_value is inside the set, we skip, since we don't want to readd
# Otherwise, add it to the set.
def add_to_list(lst, original, rotated_value):
    found = False
    for i in lst:
        if rotated_value in i:
            found = True
            break
        if original in i:
            found = True
            i.append(rotated_value)
    if not found:
        lst.append([original, rotated_value])
        print(lst)
    return lst
# https://www.whitman.edu/Documents/Academics/Mathematics/Huisinga.pdf
# Burnside's lemma

if __name__ == '__main__':
    size = 4
    six_by_six = np.asarray(list(range(size ** 2)))
    six_by_six.shape = (size,size)

    # Set everything to 1 indexed.
    six_by_six = six_by_six + 1

    # np.rot90 rotates 90 degrees CCW
    # Generate list for rotations
    lst = []
    for ii in range(4):
        k = np.rot90(six_by_six)
        for i in range(size ** 2):
            query = i + 1
            idx = np.where(k==query)
            x = idx[0][0]
            y = idx[1][0]
            original = six_by_six[x][y]
            # print(f"Query {query} was found at position {x},{y}. Original was {original}.\n")
            lst = add_to_list(lst, six_by_six[x][y], query)
    rotation_lst = []
    for i in lst:
        rotation_lst.append(tuple(i))
    
    for i in rotation_lst:
        print(i)
    print(six_by_six)

    # Generate list of reflections
    lst = []
    k = np.fliplr(six_by_six)
    for i in range(size ** 2):
        query = i + 1
        idx = np.where(k==query)
        x = idx[0][0]
        y = idx[1][0]
        original = six_by_six[x][y]
        # print(f"Query {query} was found at position {x},{y}. Original was {original}.\n")
        lst = add_to_list(lst, six_by_six[x][y], query)
    
    flip_lst = []
    for i in lst:
        flip_lst.append(tuple(i))
    print(f'[{rotation_lst},{flip_lst}]')


    
        

# j = 0
# current = time.time()
# for i in itertools.product('CN', repeat=36):
#     j += 1
#     print(i)

# print(time.time() - current)
# print(j)

# # Generate a <number> x <number> board with sentinel values
# def generateBoard(number):
#     row = [-1] * number
#     board = []
#     for i in range(number):
#         board.append(row)
#     return board

# # Fill the board with all possible configurations of 1,0
# def fillBinaryBoard(board, i, j):
#     for i in range(len(board)):
#         for j in range(len(board)):






