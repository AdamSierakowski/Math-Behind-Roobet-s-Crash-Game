import hmac
import hashlib
# import numpy
import matplotlib.pyplot as plt


def prev_hash(hash_code):
    return hashlib.sha256(hash_code.encode()).hexdigest()


def hmac_hash(hash_code):
    key = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b259\
6d116859c"
    return hmac.new(hash_code.encode(), key.encode(),
                    digestmod=hashlib.sha256).hexdigest()


def get_multiplier(hash_code):
    hash_hex = hmac_hash(hash_code)
    if (int(hash_hex, 16) % 20 == 0):
        return 1.00
    h = int(hash_hex[:13], 16)
    e = 2 ** 52
    return (((100 * e - h) / (e - h)) // 1) / 100.0


def average_return(your_multiplyer):
    game_hash = 'cc4a75236ecbc038c37729aa5ced461e36155319e88fa375c9\
94933b6a42a0c4'  # the 1273934th game
    results = [get_multiplier(game_hash)]
    for i in range(1273934):
        game_hash = prev_hash(game_hash)
        results.append(get_multiplier(game_hash))
    return (sum(your_multiplyer < crash_multiplayer for crash_multiplayer
                in results) / len(results) * your_multiplyer)


def main():
    print(average_return(2))
    li = [[x, average_return(x)] for x in range(2, 50)]
    plt.scatter(*zip(*li))
    plt.show()


main()
