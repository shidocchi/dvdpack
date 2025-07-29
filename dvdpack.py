#!/usr/bin/env python
import sys
import csv
from itertools import chain, combinations
from argparse import ArgumentParser

__version__ = '0.1'

def get_args():
    parser = ArgumentParser()
    parser.add_argument('-a', '--all', help='all solution with bruteforce', action='store_true')
    parser.add_argument('-s', '--sort', help='sort input', action='store_true')
    parser.add_argument('-t', '--tee', help='print input', action='store_true')
    parser.add_argument('-c', '--cut', help='min itemsize', type=int, default=10)
    parser.add_argument('-m', '--min', help='min totalsize', type=int, default=4500000)
    parser.add_argument('-x', '--max', help='max totalsize', type=int, default=4587000)
    return parser.parse_args()

def brute_knapsack(items, args):
    result = []
    for r in range(2, len(items)):
        for c in combinations(range(len(items)), r):
            s = sum(items[x][0] for x in c)
            if args.min <= s <= args.max:
                result.append((s, c))
    return result

def sober_knapsack(items, args):
    from ortoolpy import knapsack
    return [knapsack([x[0] for x in items], [x[0] for x in items], args.max)]

if __name__ == '__main__':
    args = get_args()
    fields = (int, str)
    reader = csv.reader(sys.stdin, 'excel-tab')
    items = [tuple(f(v) for f,v in zip(fields,row)) for row in reader]
    items = [r for r in items if r[0] >= args.cut]

    if args.sort:
        items.sort(reverse=True)
    if args.tee:
        for f,v in items:
            print(f, v)
    if args.all:
        result = brute_knapsack(items, args)
    else:
        result = sober_knapsack(items, args)
    for r in result:
        print(int(r[0]), ' '.join(items[i][1] for i in r[1]))
