import csv
import sys
from sys import argv

def main():
    with open('1.txt', newline='') as dna_seq:
        file2 = dna_seq.read()
        writer = csv.writer(file2)
        writer.writerow((AGATC))
        for row in file2:
            row = {
                'AGATC': 0,
                'TTTTTTCT': 0,
                'AATG': 0,
                'TCTAG': 0,
                'GATA': 0,
                'TATC': 0,
                'GAAA': 0,
                'TCTG': 0
                }

            AGATC = 0
            for AGATC in file2:
                AGATC += 1
                
                print(f"{writer['AGATC']}")


if __name__ == "__main__":
    main()
