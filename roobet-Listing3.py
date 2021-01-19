import hmac
import hashlib
import matplotlib.pyplot as plt


def prev_hash(hash_code):
    return hashlib.sha256(hash_code.encode()).hexdigest()


def hmac_hash(hash_code):
    key = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b259\
6d116859c"
    return hmac.new(hash_code.encode(), key.encode(),
                    digestmod=hashlib.sha256).hexdigest()


def get_h(hash_code):
    return int(hmac_hash(hash_code)[:13], 16)


def h_distribution():
    game_hash = 'cc4a75236ecbc038c37729aa5ced461e36155319e88fa375c9\
94933b6a42a0c4'  # the 1273934th game
    results = [get_h(game_hash)]
    for i in range(1273934):
        game_hash = prev_hash(game_hash)
        results.append(get_h(game_hash))
    plt.hist(results, bins=100)
    plt.title('h-values for 1.273.935 Crash Games')
    plt.show()


def main():
    h_distribution()


main()
