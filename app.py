import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--var", help="increase output verbosity")

args = parser.parse_args()
print(args)
