import argparse
from library.cache_master_flex import store as memstore, retrieve as memretrieve
from memcached.client import mem_client

def store(name, infile, client):
  memstore(name, infile, client)


def retrieve(name, client):
  data = memretrieve(name, client)
  return data


def main():
    """ Process Command Line Arguments """
    parser = argparse.ArgumentParser(description='Store and retrieve files in Memcached')
    parser.add_argument('action', help='Action to process (store, retrieve)')
    parser.add_argument('name', help='Name of the file')
    parser.add_argument('file', help='File for processing',nargs='?', default=None)

    args = parser.parse_args()
    if args.action == 'store':
        store(args.name, args.file, mem_client)
    elif args.action == 'retrieve':
        retrieve(args.name, mem_client)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()