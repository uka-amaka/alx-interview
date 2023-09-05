#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

def main():
    x = 5
    nums = [2, 5, 1, 4, 3]
    winner = isWinner(x, nums)
    print("Winner: {}".format(winner))

if __name__ == "__main__":
    main()
