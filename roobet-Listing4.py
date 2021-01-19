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


def get_multiplier_modified(hash_code):
    hash_hex = hmac_hash(hash_code)
    if (int(hash_hex, 16) % 20 == 0):
        return 20  # will not be shown
    h = int(hash_hex[:13], 16)
    e = 2 ** 52
    return (((100 * e - h) / (e - h)) // 1) / 100.0


def multiplayer_distribution():
    game_hash = 'cc4a75236ecbc038c37729aa5ced461e36155319e88fa375c9\
94933b6a42a0c4'  # the 1273935th game
    results = [get_multiplier_modified(game_hash)]
    for i in range(1273934):
        game_hash = prev_hash(game_hash)
        mult = get_multiplier_modified(game_hash)
        if mult < 20:
            results.append(mult)
    plt.hist(results, bins=20)
    plt.title('crash multiplayers from 95% of the games')
    plt.show()


def main():
    multiplayer_distribution()


main()
