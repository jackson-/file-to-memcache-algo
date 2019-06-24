from pymemcache.client.base import Client

client = Client(('localhost', 11211))

result = client.get('some_key')

def store(name, step, data, size=None):
  # if step == 1:
  #   client.set('{}_0'.format(name), size / 1000000)
