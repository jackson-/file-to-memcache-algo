import argparse
from os.path import getsize
import math
from cache_master_flex import store as memstore, retrieve as memretrieve

def store(name, infile):
  size = getsize(infile)
  if size > 50000000:
    raise ValueError("That file is too large! Please try again with something that is less than 50 megabytes.")
  f = open(infile, "r")
  memstore(name, f, size)


def retrieve(name, outfile):
  data = memretrieve(name)
  return data


def main():
    """ Process Command Line Arguments """
    parser = argparse.ArgumentParser(description='Store and retrieve files in Memcached')
    parser.add_argument('action', help='Action to process (store, retrieve)')
    parser.add_argument('name', help='Name of the file')
    parser.add_argument('file', help='File for processing')

    args = parser.parse_args()
    if args.action == 'store':
        store(args.name, args.file)
    elif args.action == 'retrieve':
        retrieve(args.name, args.file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()