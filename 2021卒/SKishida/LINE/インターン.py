# LINE コーディングテスト
import sys

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    y = int(argv[0])
    m = int(argv[1])
    w = int(argv[2])
    d = list(map(int, argv[3].split('-')))

    if ((d[0] - 1) * (y % m) + (y % m)) > m or y % m == 0:
        if y // m > 99 or m > 99 or m < d[2]:
            print(-1)
            return
        else:
            n = ((d[0] - 1) * y - (d[0] - 1) * (y % m) % m + (d[1] - 1) * m + d[2]) % w
            if n == 0:
                print(chr(ord('A') + w - 1))
            else:
                print(chr(ord('A') + n - 1))
    else:
        if y // m > 98 or m > 99 or m < d[2]:
            print(-1)
            return
        else:
            n = ((d[0] - 1) * y - (d[0] - 1) * (y % m) % m + (d[1] - 1) * m + d[2]) % w
            if n == 0:
                print(chr(ord('A') + w - 1))
            else:
                print(chr(ord('A') + n - 1))



if __name__ == '__main__':
    main(sys.argv[1:])

