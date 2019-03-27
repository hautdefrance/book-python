from argparse import ArgumentParser


def avg(*args):
    return sum(args) / len(args)


parser = ArgumentParser()
parser.add_argument('--numbers', nargs='+', type=float)
args = parser.parse_args()

out = avg(*args.numbers)
print(out)
