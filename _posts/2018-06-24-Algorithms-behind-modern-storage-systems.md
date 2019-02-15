---
title: "[Review] Algorithms Behind Modern Storage Systems"
excerpt: "ACM Queue March+April 2018. Technical article on the data structures and algorithms used in modern storage systems."
categories:
  - read
  - magazines
keynote: true
---
## Article
- [Algorithms Behind Modern Storage Systems (ACM Queue, Mar+Apr 2018)](https://dl.acm.org/citation.cfm?id=3220266)

- [On Disk IO, Part 1: Flavors of IO](https://medium.com/databasss/on-disk-io-part-1-flavours-of-io-8e1ace1de017)
- [On Disk IO, Part 2: More Flavors of IO](https://medium.com/databasss/on-disk-io-part-2-more-flavours-of-io-c945db3edb13)
- [On Disk IO, Part 3: LSM Trees](https://medium.com/databasss/on-disk-io-part-3-lsm-trees-8b2da218496f)
- [On Disk IO, Part 4: B-Trees and RUM Conjecture](https://medium.com/databasss/on-disk-storage-part-4-b-trees-30791060741)
- [On Disk IO, Part 5: Access Patterns in LSM Trees](https://medium.com/databasss/on-disk-io-access-patterns-in-lsm-trees-2ba8dffc05f9)

## Background Knowledge & Summary
This main article focuses on data structures and algorithms that are used in modern database systems. Through a concise overview of B-trees and LSM trees, the author extends the trade-offs of each data structure to the RUM conjecture, which suggests that you can try to balance the read/update/memory overheads, but there isn't a perfectly optimal structure.

For further information, refer to the following keynote presentation I've made. Explained here are the basics of I/O (including virtual memory, paging, and page swapping), B-Trees, LSM trees, Write Ahead Log and the RUM Conjecture.

<a class="embedly-card" data-card-controls="0" href="https://www.icloud.com/keynote/0dqsZt83Icufku4HPiRwe8dbQ">Keynote Presentation</a>
