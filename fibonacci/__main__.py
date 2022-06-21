from argparse import ArgumentParser
from . import fib

parser = ArgumentParser()
parser.add_argument('n', type=int)

def main():
    args = parser.parse_args()
    print(fib(args.n))


if __name__ == '__main__':
    main()
