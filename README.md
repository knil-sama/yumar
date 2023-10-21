# yumar
Yumar is a way to find delicious (or not) food in a restaurant near you

# Run program

## Local run

Install it following [this tutorial](./backend/README.md)

You can then start it with this command
```bash
./search latitude=48.8319929 longitude=2.3245488 radius=100
```

## Docker run

```bash
docker build . --tag yumar
docker run --rm -t -v $PWD/data:/workspace/data yumar ./search latitude=48.8319929 longitude=2.3245488 radius=100
```

# Question

Your service works and is becoming very popular. Your team wants to extend it beyond
Paris and the list of resturants is now about 15 millions. At the same time, your service
=> Load data part is mostly reading the json part
currently we timeit around ~350ms for ~6k so 15 is 2500 time that so assuming linear time 875000ms = 875s = 15min
so this part we already switch from json library to msgspec that yield a small perf boost of ~20%, so one solution would be to rewrite input file by removing 5 first and 2 last line so we transform it to a multilines json that allow us to parralelize reading either writing code ourself or using something like Dask/Spark

is expected to reach a peak of charge of 10,000 requests per second.
What would you change to your solution to make it scale =>
move it to a database that would properly index it like postgresql or mongodb or implement a proper data structure to query spatial data as Rtree, k-d trees.
