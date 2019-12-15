# udacity-algorithms

### Problem 1: Square Root of an Integer

The basic approach to solve this problem would be a linear scan checking `n * n` for every `n` from 1 to input value. This would run in O(n) time, so I think we can do better.

The problem can be solved using a binary search. An upper and lower bound (L and R) are constrained, reducing the problem space by 1/2 at each iteration.

Time complexity: O(log(n)) there are a constant number of operations per iteration, and the problem space is reduced by 1/2 in each iteration.

Space complexity: O(1)

### Problem 2: Search in a Rotated Sorted List

Once again, the basic approach would be to scan the entire list from start to finish, looking for the target element. It is guaranteed to work but would take O(n) time, and does not take advantage of the sorted property. 

Instead we can split the list into two halves at each iteration. One of the two halves must be in continuous order (will not contain the break from rotation). We can make a definite statement about whether the target number is contained within the continuous half. Focusing on this half, we can proceed like a normal binary search, cutting search space in half with each iteration. This gives us desired O(log(n)) complexity.

Time complexity: O(log(n))

Space complexity: O(1)

### Problem 3: Rearrange Array Digits

A naïve solution would scan the whole array for the largest value, remove it, and add it to digits in number A, then scan for the next largest value, remove it, and add it to digits in B, then repeat the process until the array is empty. This would take `n² / 2` steps giving O(n²) time. 

This problem is made much easier if we first sort the list using mergesort. Then all that is remaining is to separate the even and odd elements of the array to two numbers.

Time complexity: O(n(log(n)) the time complexity is dominated by mergesort.

Space complexity: O(n) the space complexity is linear since we create a copy during the mergesort. We could achieve O(1) space complexity if we did an in-place sort.

### Problem 4: Dutch National Flag

The basic solution would be to sort the array using any conventional sort algorithm (mergesort, quicksort, etc.). This would give O(nlog(n)) time complexity. It does not take advantage of the fact that there are only 3 unique values in the array.

It is possible to sort the numbers in one pass. The array can be thought of as a stack that grows inward from both ends. Left end is a stack of `0` growing forward, right end is a stack of `2` growing backward. We have to maintain a pointer to the top of each stack, then scan through the array, pushing all `0` on the left stack and all `2` on the right stack.

Time complexity: O(n)

Space complexity: O(1) we use a constant amount of extra space to store the pointers and swap numbers.

### Problem 5: Autocomplete with Tries

The search trie is implemented with a tree of `TrieNode`s. The root node represents an empty string. In each `TrieNode`, child nodes are stored in a dictionary that maps from characters to child `TrieNode`s. 

Time complexity: 

- Insert: O(n) where n is total length of all words in word list
- Find: O(m) where m is length of search string. To traverse the trie looking for a match, each step from one node to the next is constant time dictionary lookup.

Space complexity: 

O(n) where n is total number of nodes in the trie. In order to say more, I think we have to know statistical properties of the input. Basically, we expect the trie space to grow linearly with number of input words at the start, but then slow down as each new word is more likely to overlap with nodes that are already in the tree.

### Problem 6: Unsorted Integer Array

The solution does a linear scan, keeping track of the minimum and maximum of everything seen.

Time complexity: O(n)

Space complexity: O(1)

### Problem 7: Request Routing

The architecture is the same as Problem 5, except with each node representing a path segment ("part") instead of a character. 

Time complexity: 

- Insert: O(n) where n is total path length of all routes.
- Find: O(m) where m is length of path requested. 

Space complexity:

O(n); same as Problem 5.
