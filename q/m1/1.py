def squares(length, width, square_side):
    squarehor =  length // square_side
    squarever = width // square_side
    total_squares = squarehor * squarever

    return total_squares

length = 647
width = 170
square_side = 30

total_squares = squares(length, width, square_side)
print("The total number of squares that can fit in the rectangle:", total_squares)