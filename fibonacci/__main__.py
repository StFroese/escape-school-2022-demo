from argparse import ArgumentParser
from . import fib

parser = ArgumentParser()
parser.add_argument('n', type=int)
parser.add_argument('-l', '--list', action='store_true')

def main():
    args = parser.parse_args()
    if args.list:
        for i in range(args.n + 1):
            print(fib(i))
    else:
        print(fib(args.n))


if __name__ == '__main__':
    main()
