import sys
import csv
from sys import argv



def main():
    while True:
        if len(argv) != 3:
            print("Error!!")
            sys.exit(1)
        else:
            with open('databases/large.csv', newline='') as csvfile:
                file = csv.DictReader(csvfile)
                for row in file:
                    print([int(v) for v in list(row.values())[1:]])
                    print(row['name'])

if __name__ == "__main__":
    main()
