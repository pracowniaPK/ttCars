import time
import pickle
from os import listdir

from twitter_scraper import get_tweets

from stuff import h_list


def import_tweets(handle, n):
  tts = []
  t = time.time()
  for tweet in get_tweets(handle, n):
    tts.append(tweet)
  t2 = time.time()
  print('{2} - {0:.2f}s : {1:}'.format(t2-t, len(tts), handle))
  pickle.dump(tts, open('data\\{}'.format(handle), 'wb'))
  print('Saved to data\\{}'.format(handle))

def import_multiple(handles, n):
  for h in handles:
    print('importing {}...'.format(h))
    import_tweets(h, n)

def unpack_tweets(handle):
  data = pickle.load(open( 'data\\{}'.format(handle), 'rb' ))
  return data

def unpack_all(path):
  handles = listdir('data')
  res = {}
  for h in handles:
    res[h] = unpack_tweets(h)
  return res

if __name__ == "__main__":
  # import_multiple(['Tesla', 'fiat'], 1)
  # import_multiple(h_list, 20)
  # import_tweets('MazdaUSA', 20)

  data = unpack_all('data')
  print(data.keys())
  # print(data['Tesla'][0])
