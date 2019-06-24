import argparse
from cache_master_flex import store as memstore, retrieve as memretrieve

def store(name, infile):
  memstore(name, infile)


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