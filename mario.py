

#take user input
def main():

    while True:
        print("Height")
        height = int(input())
        if height <= 0 and height > 8:
            break
        
mario(height)

main()





def mario(n):
    for x in range(n):
        print('  '*(n-x-1)+'#'*(2*x+1))


