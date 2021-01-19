import hmac
import hashlib


def hmac_hash(hash_code):
    key = "0000000000000000000fa3b65e43e4240d71762a5bf397d5304b259\
6d116859c"
    return hmac.new(hash_code.encode(), key.encode(),
                    digestmod=hashlib.sha256).hexdigest()


def get_multiplier(hash_code):
    hash_hex = hmac_hash(hash_code)
    if (int(hash_hex, 16) % 20 == 0):
        return 1
    h = int(hash_hex[:13], 16)
    e = 2 ** 52
    return (((100 * e - h) / (e - h)) // 1) / 100.0


def main():
    game_hash = 'cc4a75236ecbc038c37729aa5ced461e36155319e88fa375c\
994933b6a42a0c4'
    print(get_multiplier(game_hash))
    game_hash = 'fa0bd7818e238aa613426eba7422ca364369c0ec55767c8e0\
23ba6d3ba161aeb'
    print(get_multiplier(game_hash))


main()
