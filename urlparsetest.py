from urllib.parse import urlparse
from timeit import default_timer as timer

total = 0

with open('chromiumUrls.txt') as f:
    for url in f:

        start = timer()

        a = urlparse(url)

        end = timer()

        total += end - start

print("the total time is", total, "seconds")
