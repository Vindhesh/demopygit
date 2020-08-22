
import argparse
parser = argparse.ArgumentParser(description='This program displays the square of given numbers')
# parser = argparse.ArgumentParser()
# parser.add_argument("num", type=int, help= "Please input integer type number.")
# args = parser.parse_args()
# result = args.num**2
# print("Squre value = ", result)

parser.add_argument("n1", type=float, help= "Input first number")
parser.add_argument("n2", type=float, help= "Input second number")
# parser.add_argument('nums', nargs=2)
args = parser.parse_args()

result = float(args.n1) + float(args.n2)
print("sum of two = ", result)