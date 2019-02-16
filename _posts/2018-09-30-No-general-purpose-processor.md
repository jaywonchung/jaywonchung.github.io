---
title: "[Review] There's No Such Thing as a General-Purpose Processor"
excerpt: "ACM Queue, October 2018. There were, are, and will be no general purpose processors, according to the author."
categories:
  - read
  - magazines
keynote: true
---
## Article
[There's No Such Thing as a General-Purpose Processor (ACM Queue, October 2018)](https://dl.acm.org/citation.cfm?id=2687011)

## Background Knowledge & Summary

What is it to be a 'general-purpose' processor? It should be able to run any given algorithm, thus turing complete. However, considering only the turing complete condition neglects the performance aspect that has been driving the whole industry of processor development. In other words, a general-purpose processor should be able to run all programs efficiently.

The article examines past and recent processors and their trends in many aspects, including memory virtualization and management of the operating system, how they predict branching and how much they rely on the compiler to generate efficient code, the use of cache memory that may bias performance in favor of specific algorithms, and how various models of parallelism makes it difficult for generalization. Through such investigation, the author attempts to conclude that no such processor was ever general-purpose, and no processor will and should be either.

For details on the comparison and examination made in each boundary, refer to the following keynote presentation I've made:

<a class="embedly-card" data-card-controls="0" href="https://www.icloud.com/keynote/0sKLzLALYEPL4VKW9HVfRcUZQ">Keynote Presentation</a>
