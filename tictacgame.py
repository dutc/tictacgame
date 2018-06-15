import argparse

parser = argparse.ArgumentParser(description="Tic Tac Toe game written in python.")
parser.add_argument("-x", action="store_true")
parser.add_argument("-o", action="store_true")
args = parser.parse_args()

if args.x and args.o or not args.x and not args.o:
    print("Please specifiy -o or -x as your side, but not both.")

