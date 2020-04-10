import argparse
import sys

parser = argparse.ArgumentParser(description = "Basahin ang file ng pabaliktad.")
parser.add_argument("filename", help = "Ang file na kailangan basahin")
parser.add_argument("-l", "--limit", type = int, help = "Bilang ng linyang kailangan basahin")

parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 1.0')

args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:
    with f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]

        for line in lines:
            print(line.strip()[::-1])