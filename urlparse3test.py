import urlparse3
from timeit import default_timer as timer

total = 0

with open('urls.txt') as f:
    for url in f:

        start = timer()

        a = urlparse3.parse_url(url)
        host = a.domain
        scheme = a.scheme
        path = a.path
        query = a.query
        fragment = a.fragment

        end = timer()

        total += end - start

print("the total time is", total, "seconds")
