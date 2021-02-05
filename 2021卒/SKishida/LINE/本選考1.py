# LINE コーディングテスト（本選考）
import math

def process_data(param_lists):

    dict_pair = {}

    numeric = int(param_lists.pop(-1))

    for param in param_lists:
        value, key = param.split(":")
        dict_pair[key] = int(value)

    return dict_pair, numeric


def play_FizzBuzz(dict_pair):

    word = ''

    for key, value in sorted(dict_pair.items(), key=lambda x: x[1]):
        if numeric % value == 0:
            word += key

    return word


def show_word(answer_word):
    if answer_word:
        print(answer_word)
    else:
        if isPrime(numeric):
            print("prime")
        else:
            print(numeric)


def isPrime(numeric):
    if numeric == 1:
        return False

    for divide_num in range(2, int(math.sqrt(numeric)) + 1):
        if numeric % divide_num == 0:
            return False

    return True


if __name__ == '__main__':
    param_lists = list(input().split())

    dict_pair, numeric = process_data(param_lists)

    answer_word = play_FizzBuzz(dict_pair)

    show_word(answer_word)

