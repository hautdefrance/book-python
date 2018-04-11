import timeit


timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# 0.3018611848820001

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# 0.2727368790656328

timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# 0.23702679807320237