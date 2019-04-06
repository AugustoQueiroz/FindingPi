# Finding Pi

This repo was created inspired by [Matt Parker's](https://www.youtube.com/channel/UCSju5G2aFaWMqn-_0YBtq5A) weird and awesome passion for finding pi in interesting creative ways.

## Ways of finding Pi

### 1. Co-prime Random Numbers

This first method is taken directly from [one of Matt's videos](https://www.youtube.com/watch?v=RZBhSi_PwHU). Basically the idea is to find pi experimentally through the probability that given two random numbers they'll be co-prime. This can be proven to be 6/(pi^2). You can see the proof given by Matt on his video.

### 2. Monte Carlo

Imagine you have a square with a side of length *l*, and imagine that you have a circle inscribed in that square (therefore of radis *l/2*). What is the chance that a randomly chosen point inside that square is also inside the circle? pi/4. To find pi we can experimentally approximate that probability and then multiply it by 4.

### 2. Buffon's Needle

If you throw many needles at a ruled paper, you can try and estimate PI by counting how many of those needles crossed a line. The needle's length must be no more than the length between the lines of the paper.