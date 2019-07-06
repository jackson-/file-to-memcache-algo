from os.path import getsize
import hashlib
import json


CHUNK_SIZE = 1000000
MAX = 50000000

def store(name, infile, client):
  size = getsize(infile)
  if size > MAX:
    raise ValueError("That file is too large! Please try again with something that is less than 50 megabytes.")
  data_hash = hashlib.md5()
  data_file = open(infile, "rb")
  if(client.get('{}_0'.format(name))):
    raise ValueError("Sorry this file has already been entered. Please enter a different file")
  data = data_file.read(CHUNK_SIZE)
  step = 1
  while data:
    client.set('{}_{}'.format(name, step), data)
    data_hash.update(data)
    data = data_file.read(CHUNK_SIZE)
    step += 1
  client.set('{}_0'.format(name), {"size":size / float(CHUNK_SIZE), "hash": data_hash.hexdigest()})
  return True
  
  
def retrieve(name, client):
  b_string = client.get('{}_0'.format(name))
  if not b_string:
    raise KeyError("This data doesn't exist")
  b_string = b_string.replace(b"'",b'"')
  meta = None
  steps = None
  data_hash = None
  try:
    meta = json.loads( b_string )
  except Exception as e:
    raise ValueError("This data has unfortunately been corrupted")
  steps = meta['size']
  data_hash = meta['hash']
  compare_hash = hashlib.md5()
  current_step = 1
  data = client.get('{}_{}'.format(name, current_step))
  while(steps > 0):
    chunk = client.get('{}_{}'.format(name, current_step))
    if chunk == None:
      raise ValueError("This data has unfortunately been corrupted")
    compare_hash.update(chunk)
    data += chunk
    current_step += 1
    steps -= 1
  if compare_hash.hexdigest() == data_hash:
    return data
  raise ValueError("This data has unfortunately been corrupted")
