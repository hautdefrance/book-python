import argparse
import statistics


parser = argparse.ArgumentParser()
parser.add_argument('--numbers', metavar='int', type=int, nargs='+', help='an integer in the range 0..9')

args = parser.parse_args()
print(statistics.mean(args.numbers))