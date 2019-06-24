from pymemcache.client.base import Client

client = Client(('localhost', 11211))

result = client.get('some_key')

def store(name, data_file, size=None, chunk_size=1000000):
  data = data_file.read(chunk_size)
  step = 1
  while data:
    if step == 1:
      client.set('{}_0'.format(name), size / 1000000)
    client.set('{}_{}'.format(name, step), data)
    data = data_file.read(chunk_size)
    step += 1  
  
  
def retrieve(name, chunk_size=1000000):
  steps = int(client.get('{}_0'.format(name)))
  current_step = 1
  data = client.get('{}_{}'.format(name, current_step))
  while(steps > current_step):
    current_step += 1
    data += client.get('{}_{}'.format(name, current_step))
  return data
