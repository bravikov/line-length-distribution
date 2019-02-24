import sys
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

arguments_parser = argparse.ArgumentParser(
    description='Plots distribution of line lengths of text files.')

arguments_parser.add_argument('--min', type=int, help='minimum line length')
arguments_parser.add_argument('--max', type=int, help='maximum line length')
arguments_parser.add_argument('file_paths', metavar='FILE', type=str, nargs='+',
                              help='text file')

args = arguments_parser.parse_args()

file_path_list = []

for file_path in args.file_paths:
    file_path_list.append(file_path)


class FileInfo:
    def __init__(self, path: str):
        self.path = path
        self.line_length = []


files_info = []

for file_path in file_path_list:
    file_info = FileInfo(file_path)
    with open(file_path) as file:
        for line in file:
            line = line.rstrip()
            length = len(line)
            if args.min is not None and length < args.min:
                continue
            if args.max is not None and length > args.max:
                continue
            file_info.line_length.append(length)
    files_info.append(file_info)

lengths = []

for file_info in files_info:
    for length in file_info.line_length:
        lengths.append(length)

sns.set(color_codes=True)
axes = sns.distplot(lengths, kde=False)

min_limit = args.min if args.min is not None else 0
max_limit = args.max if args.max is not None else min_limit + 200
axes.set_xlim(min_limit, max_limit)

plt.show()
