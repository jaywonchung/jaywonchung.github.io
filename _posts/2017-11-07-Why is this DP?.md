---
title: "Why is this DP?"
layout: single
categories:
  - study
  - algorithm
 excerpt: "Identifying a problem as a dynamic programming problem may be the most difficult part."
 ---
 
The three steps of solving a problem with DP:
1. Find important variables in the problem. The number of variables is the dimension of the array.
2. Set up a recursive formula for the problem. Optimize if possible.
3. Decide whether to go with bottom-up or top-down and start coding.

But unfortunately, there is one hidden step before step 1; arguably the hardest one.
0. Notice that this problem can be solved with DP. Thus, answering the question "Why is this DP?".

So in this post, let's take a look at some characteristics of problems that can be solved with DP. It's all about how to find a small problem which looks the same as the large problem.

# Continuity

Problems that show a flow of continuous action, a continuous placement of objects, or continuity in its problem material belong to this category. Try removing the last element(=```a[n-1]```) of the problem leaving the a[0]~a[n-2] part. If it still has the same structure, a[0]~a[n-2] can be viewed as a small problem with an optimal substructure. Then try to express the large problem with small problems and the cost.

- [1912번: 연속합](https://icpc.me/1912)

	You scan the array sequentially and pick up certain numbers to make its sum.
	
	```python
	d[i] = (largest continuous sum ending with a[i])
	d[i] = max(d[i-1], 0) + a[i]
	ans = max(d[i] for i in range(n))
	```
	
- [2156번: 포도주 시식](https://icpc.me/2156)
	
	Without the constraint(cannot drink 3 glasses in a row), continuously drinking every single glass gives the maximum. But with the constraint, you sequentially scan the glasses and choose which glass to drink like you did in #1912.
