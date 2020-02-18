 # Setting the condition that the user must meet if not it will keep asking until right input is given
def main():
    while True:
        dollar = float(input("Change: "))
        if dollar >= 0:
            break
    change = int(dollar * 100)
    calc(change)
## I wanted to make changes right away

def calc(change):
    number = 0
    coins = [25, 10, 5, 1]
    for coin in coins:
        if coin <= change:
            count = change // coin
            number += count
            change -= number * coin
    print(f"{number}\n")

main()
