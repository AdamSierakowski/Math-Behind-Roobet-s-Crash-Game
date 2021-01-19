import hashlib


def prev_hash(hash_code):
    return hashlib.sha256(hash_code.encode()).hexdigest()


def main():
    game_hash = 'cc4a75236ecbc038c37729aa5ced461e36155319e88fa375c\
994933b6a42a0c4'
    print(prev_hash(game_hash))


main()
