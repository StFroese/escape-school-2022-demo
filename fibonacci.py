from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('n', int)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    args = parser.parser_args()
    print(fib(args,n))

if __name__ == __main__:
    main()
