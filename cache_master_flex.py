from pymemcache.client.base import Client
from os.path import getsize

client = Client(('localhost', 11211))


def store(name, infile):
  chunk_size=1000000
  size = getsize(infile)
  if size > 50000000:
    raise ValueError("That file is too large! Please try again with something that is less than 50 megabytes.")
  data_file = open(infile, "r")
  if(client.get('{}_0'.format(name))):
    raise ValueError("Sorry this file has already been entered. Please enter a different file")
  data = data_file.read(chunk_size)
  step = 1
  while data:
    if step == 1:
      client.set('{}_0'.format(name), size / 1000000)
    client.set('{}_{}'.format(name, step), data)
    data = data_file.read(chunk_size)
    step += 1
  return True
  
  
def retrieve(name, chunk_size=1000000):
  steps = int(client.get('{}_0'.format(name)))
  current_step = 1
  data = client.get('{}_{}'.format(name, current_step))
  while(steps > current_step):
    current_step += 1
    chunk = client.get('{}_{}'.format(name, current_step))
    if chunk == None:
      raise KeyError("This data has unfortunately been corrupted") 
    data += chunk
  return data
