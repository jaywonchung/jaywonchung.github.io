---
title: "Why is this DP?"
excerpt: "Identifying a problem as a dynamic programming problem may be the most difficult part."
categories:
  - study
  - algorithm
---
 
**The three steps of solving a problem with DP:**
1. Find important variables in the problem. The number of variables is the dimension of the array.
2. Set up a recursive formula for the problem. Optimize if possible.
3. Decide whether to go with bottom-up or top-down and start coding.

But unfortunately, there is one hidden step before step 1; arguably the hardest one.

**0. Notice that this problem can be solved with DP. Thus, answering the question "Why is this DP?".**

So in this post, let's take a look at some characteristics of problems that can be solved with DP. It's all about how to find a small problem which looks the same as the large problem.

# Continuity

Problems that show a flow of continuous action, a continuous placement of objects, or continuity in its problem material belong to this category. Try removing the last element(=```a[n-1]```) of the problem leaving the a[0]~a[n-2] part. If it still has the same structure, a[0]~a[n-2] can be viewed as a small problem with an optimal substructure. Then try to express the large problem with small problems and the cost.

- [1912번: 연속합](https://icpc.me/1912)

	You scan the array sequentially and pick up certain numbers to make its sum.
	
	problem formulation:
	```python
	d[i] = (largest continuous sum ending with a[i])
	d[i] = max(d[i-1], 0) + a[i]
	ans = max(d[i] for i in range(n))
	```
	
	code:
	```c++
	#include <cstdio>
	#include <algorithm>
	using namespace std;
	
	int a[100001];
	int d[100001];
	
	int main()
	{
		int n; scanf("%d", &n);
		for (int i=1; i<=n; ++i) {
			scanf("%d", a+i);
		}
		
		int ans = -1;
		for (int i=1; i<=n; ++i) {
			d[i] = max(d[i-1]+a[i], a[i]);
			if (ans < d[i]) ans = d[i];
		}
		
		printf("%d\n", ans);
		
		return 0;
	```
	
- [2156번: 포도주 시식](https://icpc.me/2156)
	
	Without the constraint(cannot drink 3 glasses in a row), continuously drinking every single glass gives the maximum. But with the constraint, you sequentially scan the glasses and choose which glass to drink like you did in #1912.
	
	problem formulation:
	```python
	d[i] = max amount until a[i]
	d[i] = max(d[i-1], d[i-2]+a[i], d[i-3]+a[i-1]+a[i])
	ans = d[n-1]
	```
	
	code:
	```c++
	#include <iostream>
	using namespace std;
	
	int a[10001];
	int d[10001];
	
	int main()
	{
		int n; scanf("%d", &n);
		for (int i=1; i<=n; ++i) {
			scanf("%d", a+i);
		}
		
		d[1] = a[1];
		d[2] = a[1]+a[2];
		for (int i=3; i<=n; ++i) {
			d[i] = max(max(d[i-1], d[i-2]+a[i]), d[i-3]+a[i-1]+a[i]);
		}
		
		printf("%d\n", d[n]);
		
		return 0;
	}
	```
	
- [11053번: 가장 긴 증가하는 부분수열](https://icpc.me/11053)

	'An increasing series' has continuity in its essence. Every next number in the series is larger than the previous.
	
	problem formulation:
	```python
	d[i] = length of the longest increasing series ending with a[i]
	d[i] = max(d[j] for j in range(i) if a[j]<a[i]) + 1
	ans = max(d)
	```
	
	code:
	```c++
	#include <cstdio>
	#include <algorithm>
	using namespace std;
	
	int a[1001];
	int d[1001];
	
	int main()
	{
		int n; scanf("%d", &n);
		for (int i=0; i<n; ++i) {
			scanf("%d", a+i);
		}
		
		int ans = 1;
		d[0] = 1;
		for (int i=1; i<n; ++i) {
			d[i] = 1;
			for (int j=0; j<i; ++j) {
				if (a[j]<a[i] && d[j]+1>d[i]) d[i] = d[j]+1;
			}
			if (ans < d[i]) ans = d[i];
		}
		
		printf("%d\n", ans);
		
		return 0;
	}
	```
	
# Splitting in the middle

For 'continuity' problems, it was better (or necessary) to scan the given data sequentially. But for some problems, the given data has no flow or direction. Try splitting the problem in the middle and see if the left and right maintain the same structure with the original problem. If it does, this means we can split the large problem into a sum of two small problems plus the cost.

Since we need to find the answer to the small problem, we will have to split the small problems again. We continue splitting until we meet unit problems whose length is usually 1. When implementing top-down, we can just return a recursive sum of the go() function. When implementing bottom-up, we loop from the smallest problems to the largest problem(our goal), finding answers to every problem with that length.

- [11066번: 파일 합치기](https://icpc.me/11066)

	Obviously, to create the final file we should add together two files. Here, we are splitting the data into two small problems(files). The cost of the large file is the sum of each cost of the small files plus the cost to add together the two small files.

	problem formulation:
	```python
	d[i][j] = minimum cost to add together files from a[i] to a[j]
	d[i][j] = min(d[i][k]+d[k+1][j] for k in range(i, j)) + sum(i, j)
	ans = d[0][n-1]
	```
	
	code:
	```c++
	#include <cstdio>

	int a[500];
	int s[500];
	int d[500][500];

	int sum(int a, int b) {
		if (a==0) return s[b];
		else return s[b]-s[a-1];
	}

	int main()
	{
		int T; scanf("%d", &T);
		while (T--) {
			int n; scanf("%d", &n);
			for (int i=0; i<n; ++i) {
				scanf("%d", a+i);
			}

			s[0] = a[0];
			for (int i=1; i<n; ++i) {
				s[i] = s[i-1]+a[i];
			}

			for (int i=0; i<n; ++i) {
				for (int j=0; j<n; ++j) {
					d[i][j] = 0;
				}
			}

			for (int i=0; i<n-1; ++i) {
				d[i][i+1] = a[i]+a[i+1];
			}

			for (int l=2; l<n; ++l) {
				for (int i=0; i<n-l; ++i) {
					for (int j=0; j<l; ++j) {
						if (d[i][i+l]==0 || d[i][i+l]>d[i][i+j]+d[i+j+1][i+l]+sum(i, i+l)) {
							d[i][i+l] = d[i][i+j]+d[i+j+1][i+l]+sum(i, i+l);
						}
					}
				}
			}

			printf("%d\n", d[0][n-1]);
	    	}

		return 0;
	}
	```

- [3948번: 홍준이의 친위대](https://icpc.me/3948)

	For some problems, we can find a pivot that we can use to split the problem. In #3948, the tallest soldier is the pivot. The position of the tallest soldier can be categorized as leftmost, rightmost, and in between. When the tallest soldier is in between, the left and right side of him becomes the small problem. One difference from the large problem is that on the left small problem, the rightmost soldier should be smaller than his left companion. This is exactly half of the whole problem. 

	problem formulation:
	```python
	d[i] = number of cases aligning i soldiers
	d[i] = sum((d[k]/2)*(d[n-k-1]/2)*combination(n-1, k) for k in range(i))
	ans = d[n]
	```
	
	code:
	```c++
	#include <cstdio>

	long long d[21];

	long long comb(int n, int k) {
		if (k>n) return 0;
		if (k*2>n) k = n-k;
		if (k==0) return 1;

		int ret = n;
		for (int i=2; i<=k; ++i) {
			ret *= (n-i+1);
			ret /= i;
		}
		return ret;
	}

	long long go(int n) {
		if (n<=2) return n;
		if (d[n]) return d[n];

		d[n] = go(n-1) + (n-1)*go(n-2);
		for (int i=2; i<n-2; ++i) {
			d[n] += comb(n-1, i)*(go(i)/2)*(go(n-i-1)/2);
		}

		return d[n];
	}

	int main()
	{
		int T; scanf("%d", &T);
		while (T--) {
			int n; scanf("%d", &n);
			printf("%lld\n", go(n));
		}

		return 0;
	}
	```
