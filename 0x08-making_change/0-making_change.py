#!/usr/bin/python3
""" make change module """


def makeChange(coins, total):
    """ find least number of coins """
    if total <= 0 or type(total) != int:
        return 0

    denomination = [float('inf')] * (total + 1)
    denomination[0] = 0

    for coin in coins:
        for amt in range(coin, total + 1):
            denomination[amt] = min(
                denomination[amt], denomination[amt - coin] + 1)

    if denomination[total] == float('inf'):
        return -1

    return denomination[total]
