#size input for square pattern
while True :
    square_size = int(input ("Enter the size of the pattern:"))
    if square_size < 0 :
        print(" Only positive values allowed")
    else :
        row=0
        while  row < square_size:
            for n in range(square_size):
                print("*", end="")
            print()
            row+=1
        break