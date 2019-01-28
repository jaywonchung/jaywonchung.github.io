---
title: "C++ tips for algorithm problem-solving"
excerpt: "Tools, tricks, and snippets for efficiently implementing algorithms."
categories: 
  - study
  - algorithm
---
Tools, tricks, and snippets are introduced for implementing algorithms. Some may be inappropriate in terms of good coding practice because these snippets are optimized for efficiency during competitive problem-solving.

# Arrays

Arrays are an important tool for storing sequential data. Also, a lot of problems are solved with dynamic programming, where arrays are a core tool. 

## Initializing an array with a single value

1. For loop

    ```c++
    for (int i=0; i<n; ++i) {
        d[i] = 0;
    }
    ```

    A standard $$O(n)$$ algorithm that fills array ```d``` with ```0```.

2. Using  ```memset(void* ptr, int value, size_t num)```

    ```c++
    memset(d, 0, sizeof(d)); // #include <cstring>
    ```
    Note that the ```value``` parameter  should be either  ```0``` or ```-1```. This is because ```memset``` was originally designed for filling every **byte** of a string with the same value. Specifically, since ```value``` is interpreted as an ```unsigned char```of size 1 byte, setting ```value``` to ```1``` fills every byte of the array with ```0x01```. Thus accessing a 4 byte integer gives ```0x01010101 == 16843009```. On the contrary, setting ```value``` to ```-1``` fills every byte with ```0xff```, where in this case grouping these bytes into 4 byte integers retains the 2's complement representation of ```-1```, which is ```0xffffffff```.

3. Declaring as a global variable

    ```c++
    #include <cstdio>
    int d[10];
    int main() {
        printf("%d", d[0]);
        return 0;
    }
    ```
	Variables delcared as a global variable are intialized to zero automatically.
	
4. Instead using ```std::vector```

	```c++
	vector<int> v(n, -1); // #include <vector>
	```
	Using vectors is a preferable in many cases, especially when the size of the array varies. For instance, it is a good idea to initialize graphs with ```vector<vector<int>> graph(n);``` as an adjacency list. This done, you can easily traverse adjacent nodes with the following range-based for loop:
	```c++
	for (int adj_node : graph[curr_node])
	```

## Array Indexing

1. Single dimensional array

	```c++
	int a[50];
	for (int i=0; i<50; ++i) {
		scanf("%d", a+i);
	}
	```
	The pointer of an array element can be written simpler.
	```c++
	for (int i=0; i<n; ++i) {
		printf("%c%d%c", " ["[i==0], a[i], ",]"[i==n-1]);
	}
	```
	This snippet prints array ```a``` python-style: ```[0, 1, 2, 3, 4]```

2. Two dimensional array

	```c++
	printf("%d\n", *max_element(d[0], d[0]+n));	// #include <algorithm>
	```
	The element of a two dimensional array is a pointer to a single dimensional array. Thus the same trick can be applied.

# Standard Input and Output
## Avoid using ```cin``` and ```cout```
For algorithm problems, small time can make a difference. Especially if you're reading somthing like $$n^2$$ integers from standard input, using ```cin``` can give you a TLE(Time Limit Exceeded). Use ```scanf``` for inputs and ```printf``` for outputs.

## Use text files for standard input
Typing in the same sample inputs every time you run your code is apparently inefficient. When compiling and running your code, you can provide "input.txt" as a standard input using the above shell command. You can read data with your ordinary standard i/o functions.
```bash
g++ -O2 -std=c++14 main.cpp -o main && ./main < input.txt
```
