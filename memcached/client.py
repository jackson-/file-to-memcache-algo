from pymemcache.client.base import Client

# We expose the Memcached client to access and manilpulate it
# anywhere in our code.
mem_client = Client(('localhost', 11211))
