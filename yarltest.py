from yarl import URL
from timeit import default_timer as timer

total = 0

with open('urls.txt') as f:
    for url in f:

        start = timer()

        a = URL(url)
        host = a.host
        scheme = a.scheme
        path = a.path
        query = a.query_string
        fragment = a.fragment

        end = timer()

        total += end - start

print("the total time is", total, "seconds")
