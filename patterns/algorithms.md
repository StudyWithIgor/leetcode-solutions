# Algorithms

# Common Algorithms in Coding Interview Problems

## Math

- Sieve of Eratosthenes [22]: algorithm to generate all prime numbers in a given
  range with time complexity less than quadratic (around O(n\*log(log(n))) time
  and O(n) space). Identify: problem requires generation of all prime numbers in
  a given range. E.g. Count Primes;
- Commutative Operations [29]: operation may be any manipulation of a data
  structure. Commutative operations are any two operations which lead to the
  same final state no matter the order they are performed. Realizing operations
  are commutative may reduce the time complexity from exponential to polynomial
  in some problems. E.g. Bulb Switcher IV, Minimum Number of Increments on
  Subarrays to Form a Target Array;
- Other[32][34]: adjacency matrix and graphs, discrete math, combinatorics and
  probability, base conversion (binary, decimal and hexadecimal), functions to
  understand Big-O analysis such as log and exponential;

## Sequence Algorithms (Array, String or Linked List)

- Prefix Sum (Kadane's algorithm): used to solve the maximum sum subarray
  problem in O(n) time. Steps:
  1. Initialize variables `best_sum` and `current_sum` both equals zero;
  2. Scan the array left to right. Always add `arr[i]` to `current_sum`, and
     reset it to zero if it becomes negative;
  3. Update `best_sum` with the maximum between itself and `current_sum`;
- Maximum sum submatrix: given a 2D array r\*c of integer, calculate the maximum
  sum of all possible submatrices in the grid;
  - for each row_start in range(grid_rows):
    - Initialize zeros array named partial, whose length is grid_cols;
    - for each row in range(row_start, grid_rows):
      - for each column in range(grid_cols):
        - Sum grid[row][column] to partial at position column;
      - Compute max_sum of partial with Kandanes's algorithm for each row;
      - Answer is the maximum among all max_sum for each row;
- Rotate matrix: given a square 2D array of integer, rotate it by 90 degrees
  clockwise. Key idea is to divide the grid in rectangular layers and rotate
  each one towards the center. Offset is always first minus i;
  - for each layer in range(zero, center):
    - first_layer equals layer;
    - last_layer equals n minus 1 minus layer;
    - for each i in range(first_layer, last_layer):
      - temp equals first and i;
      - first and i equals (last minus offset) and first;
      - (last minus offset) and first equals last and (last minus offset);
      - last and (last minus offset) equals i and last;
      - i and last equals temp;
  - Memorize: i to first to (last minus offset) to last to i;
- Prefix calculation: iterate forward or backward in a linear data structure and
  add/multiply each element to one or more total variables. Identify: needed to
  count subarrays with k sum or find total without one or more particular
  elements in linear time. E.g. Maximum Sum Circular Subarray, Product of Array
  Except Self;
- Sliding window[4]: used to perform an operation on a window of specific size,
  which might be fixed, increase or decrease during the iteration. Identify: the
  problem has a linear data structure and one must find the shortest or longest
  subarray/substring/sublist or an element with a certain property. E.g. Maximum
  sum subarray of size ‘K’, Longest substring with ‘K’ distinct characters,
  String anagrams;
- Two pointers/iterators[4]: iterate through a linear data structure using two
  pointers until one or both reach a certain condition. One pointer often works,
  but is less Big-O time efficient. Identify: the problem has a linear data
  structure and you must find a set of elements such as pair, triplet or
  subarray with a certain property. E.g. Squaring a sorted array, Triplets that
  sum to zero, Comparing strings that contain backspaces;
- Fast and slow pointers[4]: iterate through a linear data structure using two
  pointers, one moving faster than the other. By moving them at different
  speeds, the pointers are bound to meet if they are inside a loop. Also, in
  situations like a singly linked list, where it is not possible to go
  backwards, it is used to access the middle of the list. Identify: problems
  that deal with a loop in a linear data structure, check for palindrome or
  weave elements E.g. Linked List Cycle, Palindrome in Linked List, Cycle in a
  Circular Array.
- Frequency Count[1]: iterate over one or more strings/arrays/bit vectors and
  count the frequency of elements or check if they differ by one element.
  Usually made using hash table, array or bit vector to track frequencies.
  Identify: problem or subproblem requires to check for palindrome, permutation,
  edit distance or data compression. E.g. String Compression, One Away,
  Palindrome Permutation;
- In-place Linked List Reversal[4]: reverse the links of a linked list in
  place, using the existing structure and without extra memory.
  - Initialize cur equals to head of list and prev equals to None;
  - While cur is not None:
    - temp equals cur.next
    - cur.next equals prev
    - prev equals cur
    - cur equals temp
  - Identify: reverse linked list in place. E.g. Reverse a Sub-list, Reverse
    every K-element Sub-list.
- Arithmetic: perform arithmetic operation such as add, multiply, plus one etc.
  using one or more numbers whose digits are provided as a string, array or
  linked list. Handle edge cases such as carrying over one if the sum of two
  digits overflows, numbers with different digit lengths and null pointers.
  Usually solved iterating backwards or using two pointers iterating forward.
  E.g. Add Two Numbers II, Plus One to Linked List;
- Run-length Encoding[28]: algorithm used to perform compression of sequences by
  replacing the repeated elements with a single element and the frequency.
  Problems may involve compression or decompression with constraints. Two
  pointers, Dynamic Programming and Greedy patterns may be useful. E.g. String
  Compression (CtCI), String Compression II, Decompress Run-Length Encoded List;
- Backward iteration: problems may be solved faster by traversing the structure
  backwards to gain "prior knowledge" instead of trying every possibility. Also,
  using the return of recursive call might be equivalent to a backward
  traversal. Identify: problems involving chronological order or choices
  affecting future possibilities. E.g. The Masseausse, Avoid Flood in The City;
- Two Pointers and Frequency: usually implemented to find a subarray or
  substring, or even a subsequence with a particular property in a single pass
  with two pointers. The frequency count array validates the property. The
  `right` pointer performs operations on the frequency count, and the `left`
  pointer reverses the operations to look for the next occurrence. Identify:
  problem involves find a subarray, substring or subsequence in a linear
  structure. E.g. Find All Anagrams in a String, Longest Substring Without
  Repeating Characters, Minimum Window Substring;
- Suffix arrays[35]: efficient algorithm to process large strings, as long as
  the dataset is not duplicated, which would make runtime quadratic;
  - Keyword-in-context search: used to preprocess large text for fast substring
    search with return in a context.
    - Take the suffixes of the input string. Can be done in linear time since
      each one is a pointer to a position on the input string;
    - Sort the suffixes alphabetically in the array. Occurrences of a particular
      word will appear side by side;
    - Use binary search on the array if suffixes to find the desired word, scan
      until mismatch and use the index to print the context where it is present;
  - Longest repeated substring: given a string of N characters, find the longest
    repeated substring;
    - Brute force: try all possible pairs of indices for the substring and
      compute the longest common prefix for each pair. Takes O(D\*N^2) time,
      where D is the length of the longest match;
    - Optimal: use suffix sort: create the array of suffixes in linear time,
      sort it in O(n\*log(n)) time and compute the longest prefix between
      adjacent suffixes;

## Interval Algorithms

- Merge intervals[4]: algorithm to deal with problems involving intervals. Two
  intervals 'a' and 'b' can be related in three different ways: no overlap,
  overlapping with 'b' ending after 'a', overlapping with 'b' completely inside
  'a'. Merge may involve sorting intervals on start and use a priority queue
  based on their end. Identify: you have to produce a list with only mutually
  exclusive intervals, merge intervals, insert intervals or just hear
  "overlapping intervals". E.g. Intervals Intersection, Maximum CPU Load;
- Two intervals A and B overlap if A.start is less than B.end AND A.end is
  greater than B.start;

## Permutation Algorithms

- Permutations[1][16]: generate all possible ordering of elements in a group of
  fixed size. The permutations of a string/array of n characters can be
  generated by generating the permutations for n-1 elements and inserting the
  element in all possible positions of each permutation. A string of n
  characters has n! (factorial) permutations so generating them all takes at
  least O(n!) (factorial) time. Notice that even if the problem involves
  permutations, rarely it is necessary to generate all of them. Identify:
  problem mentions permutations or has a group of elements where all of them are
  present but the order changes. E.g. All Permutations of a String, Permutations
  with Duplicates.
- Anagrams[21]: re-arrangement of characters in a string to produce different
  strings, using the same characters from the original string. To determine if
  two strings are anagrams, it is possible to sort them (O(nlog(n)) time and
  O(log(n))space), map each character to a prime number, multiply them and prime
  factor decompose (O(n) time and O(n) space) or count the frequency of the
  characters (O(n) time and O(n) space). Identify: problem has the word anagram
  or deals with permutations of characters in string. E.g. Group Anagrams.

## Tree Algorithms

- Tree Traversals[2]:
  - In-order: visit left node, root and right node. In a binary search tree, the
    elements are printed in ascending order;
  - Pre-order: visit root, left node and right node;
  - Post-order: visit left node, right node and root;
- Tree BFS[4]: level by level traversal applying breadth-first search on a tree.
  The root is pushed to a queue, then popped, processed and its children are
  pushed to the queue, until the queue is empty. Identify: level by level
  traversal of a tree is required. E.g. Zigzag traversal.
- Tree DFS[4]: applying depth-first search on a tree. A stack or recursion is
  used to traverse a tree in-order, pre-order or post-order. Identify: necessary
  to traverse a tree in a particular order or searching for something where the
  node might be close to a leaf. E.g. Sum of Path Numbers, All Paths for a Sum;
- Tree Path: sequence of adjacent tree nodes, like a linked list. Also called a
  sequence, they can start and end at any node, or strictly go downwards from
  parent to child. For the case of any node in a binary tree, the path can be
  split in left and right branches. It may involve counting the paths, find the
  length of the longest path or pairs of nodes within a distance apart. Usually
  solved with post-order or pre-order tree traversal. E.g. Binary Tree Longest
  Consecutive Sequence II, Path Sum, Number of Good Leaf Nodes Pairs;

## Graph Algorithms

- Graph Searches[1][2]: used to find a node with a particular property or visit
  all nodes. Nodes already visited must be identified using a hash table, a set
  or a distance variable. Applicable to all graph representations (matrix,
  adjacency list or objects and pointers);
  - Depth-first Search: goes deep before going broad. One exhaustively explores
    a path before going back and choosing another path. DFS is often used to
    visit all nodes in the graph, since it might be simpler to write than BFS.
    It might take a very long time to find a path between two nodes, and the
    path found is probably not the shortest;
  - Breadth-first Search: goes broad before going deep. One exhaustively
    searches all the neighbors of the origin before going to the neighbors of
    the neighbors. It might involve using a queue to process nodes and keeping
    track of the number of nodes in each level. BFS finds the shortest path
    between two nodes;
  - Bi-directional Breadth-first Search: identical to BFS except for the fact
    that two searches happen simultaneously, both from the origin and the
    destination, and they meet half way. It is more efficient than regular BFS
    because, if k is the number of neighbors of each graph node and d is the
    distance between origin and destination, regular BFS will visit k^d nodes
    (O(k^d) time) until it finds the shortest path, while bi-directional BFS
    will visit 2k^(d/2) nodes (O(k^(d/2)) time) to find it.
- Union find [10][11]: algorithm that uses a disjoint set, which is a collection
  of elements in non-overlapping intervals, usually implemented with arrays
  `roots` and `sizes`. Most common operations are find the root of a subset for
  a particular element, check if two elements are in the same subset and union
  two subsets into a single subset. Identify: find if two nodes are in the same
  connected component of a graph, check if adding a new edge leads to a cycle,
  count the cycles in the graph or perform the maximum number of union
  operations possible. E.g. Product of minimum edge weight between all pairs of
  a Tree, Check if the given Binary Expressions are valid, Bricks Falling When
  Hit, Most Stones Removed with Same Row or Column;

## Set Algorithms

- Subsets[4]: use BFS approach to deal with finding combinations or permutations
  of a given set of numbers. Start a queue with an empty list. Level by level,
  for each number in the input set, go over all current lists in the queue,
  create a copy of each list, insert the current number and push it to the
  queue. All combinations of possibilities of deciding to add or not add each
  element in input set will be present in the queue;
  - Identify: find the combinations or permutations of a set of elements. E.g.
    Subsets With Duplicates, String Permutations by changing case;

## Heap Algorithms

- Two heaps[4]: divide a set of elements in two halves, keeping the largest in a
  min heap and the smallest in a max heap. The median of the set can be
  calculated from the two top elements of heaps. Identify: track the median of a
  set of elements that changes size E.g. Find the Median of a Number Stream.
- Top K elements[4]: used to find the largest, smallest or frequent 'K' elements
  among a given set without sorting, using a min heap or max heap.
  1. Initialize heap and insert the first 'K' elements;
  2. Iterate through set. If found an element larger than the top, replace it;
  3. Process heap if necessary, like constructing an array;
  - Identify: find the largest, smallest or frequent 'K' elements in a set or
    find an element with a particular property without sorting. E.g. Top 'K'
    Numbers, Top 'K' Frequent Numbers;
- K-way Merge[4]: efficiently make a sorted traversal all arrays from a list of
  sorted arrays using a heap.
  1. Initialize min-heap and insert the first element of each array in it;
  2. Remove the top element of the heap and add it to the "merged" array;
  3. Insert the next element from the array whose element left the the heap;
  4. Repeat until the heap is empty;
  - Identify: problems with sorted arrays, lists or matrix, where you need to
    merge them. E.g. Merge K sorted Lists, K Pairs with Largest Sums;

## Bit Manipulation

- Bit Manipulation[1][2]: requires the knowledge of bit operations (get, set,
  clear, flip) and operators (AND, OR, XOR, left bit shift and logical and
  arithmetic right bit shift) Identify: problems that deal directly with bits,
  utf-8 or hexadecimal, the representation of states of a collection of nodes or
  find one or more unique, repeated or with different frequency elements E.g.
  Pyramid Transition Matrix, Single Number II, Repeated DNA Sequences;
- XOR[23]: XOR an integer a with other integer b twice results in a, and XOR
  between zero and any integer a results in a. This can be used to identify one
  or more numbers with frequency different from others in an array. It might be
  necessary to make the operation to partition the array and repeat it on both
  halves. E.g. Single Number, Single Number III (leetcode);
- Add: while b is different from zero, assign carry to be a `AND` b, assign a to
  be a `XOR` b and assign b to be carry left shifted by one;
  ```
  carry=0000,0001,0010,0100,0000
  a=0101,0110,0100,0000,1000
  b=0011,0010,0100,1000,0000
  ```
- Subtract: while b is different from zero, assign borrow to be negated a `AND`
  b, assign a to be a `XOR` b and assign b to be borrow left shifted by one;
  ```
  borrow=0000,0010,0000
  a=0101,0110,0010
  b=0011,0100,0000
  ```
- Multiply: initialize variable total. While b is different from zero, if the
  first bit of b is one, add a to total. Left bit shift a by one and right bit
  shift b by one on each iteration.
  ```
  total=0000,0010,0110
  a=0010,0100,1000
  b=0011,0001,0000
  ```
- Divide: create sign variable equal to -1 if a and b have different signs else
  1. Initialize a variable quotient to zero. Using absolute values, while a is
     greater than or equal to be, use `subtract` to remove b from a and `add` to
     increment quotient on each iteration. Use `multiply` to return the product
     of quotient and sign.
  ```
  quotient=0000,0001,0010
  a=0110,0011,0000
  b=0011,0011,0011
  ```
- Square positive integer: in a recursive `squareNum` function, if n is negative
  flip its sign. Initialize variable x. If the first bit of n is one, return
  `(squareNum(self,x)<<2)+(x<<2)+1` else return `squareNum(self,x)<<2`;
  ```
  n=0001,0011
  x=0000,0001
  result=0001,1001
  ```
- X to the nth power: in a recursive approach, base case is if `n==0` return 1.
  If n is even, return `power(x,n/2)*power(x,n/2)`, otherwise return
  `x*power(x,n/2)*power(x,n/2)`;
- Square root of X: starting from 1, try all integers until `i*i>x`, return `i`;

## Sort Algorithms

- Cycle Sort[4]: iterates over an array of integers with one pointer and if the
  current element is not at the index equal to its value, the element is swapped
  with the element at that index. Used to sort an array in O(n^2) time and O(1)
  space. Identify: problems with an array of integers withina given range or
  find the missing, duplicate or smallest number in the array. E.g. Find the
  Missing Number, Find the Smallest Positive Missing Number;
- Topological Sort[4][24]: used to find a linear ordering of elements that have
  a dependency on each other. If event 'B' is dependent on event 'A', 'A' comes
  before 'B' in topological ordering. Source is any node with no incoming edges.
  Sink is any node with no outgoing edges. Only Directed Acyclic Graphs have a
  topological ordering. Iterative algorithm O(v+e) time and space where v is the
  number of vertex and e is the number of edges of graph. Alternatively, it can
  be built using DFS and traversing the graph to find the last node:
  1. Initialize a hashmap of sets (graph) and a hashmap of integers (indegree);
  2. Populate graph and indegree using the input;
  3. Find the source(s) (elements with indegree zero) and add it to a queue;
  4. Pop queue, append element to answer (array, string etc.) and decrement the
     indegree of all elements in its graph by one. If any of them reach indegree
     zero, append it to the queue (new source);
  5. Repeat previous step until the queue is empty;
  - Identify: asked to update all objects in a sorted order, find the ordering
    of objects that depend on one another or the class of objects follows a
    particular order. E.g. Task scheduling, Alien Dictionary, Minimum height of
    a tree;
- Merge Sort: an array of integers is divided into smaller arrays until they
  reach size one, which are considered sorted and returned. On the upper levels
  of the recursion tree, the sorted halves are merged in sorted order by copying
  the smaller element first. When the end of one array is reached, the remaining
  elements of the other are copied. The resulting array is returned.
- Quick Sort: A random element is chosen as a pivot. The array is traversed
  inwards with two pointers. If left pointer is greater than the pivot and right
  pointer is smaller than the pivot, the elements are swaped. The algorithm is
  repeated on both halves, until the array reaches size one.
- Bucket Sort[1][17]: used to sort a list of elements in linear time.
  1. Initialize buckets, an array with n empty arrays;
  2. For element arr[i] in the array, insert it into bucket[n\*array[i]];
  3. Sort individual buckets using insertion sort;
  4. Concatenate all sorted buckets;
  - Identify: the problem asks for sorting a list of elements in linear time,
    requires grouping of elements based on a certain property or calculate the
    best, minimum/maximum in linear time (faster than a heap) over a limited
    range of values. E.g. Group Anagrams, Campus Bikes;
- Radix Sort[1][31]: Iterate through the list of numbers and group elements from the
  least to the most significant bit or digit. Counting Sort or any stable
  sorting algorithm may be used for grouping. Complexity is O(nk) where n is the
  number of elements and k is the number of passes. Example:
  1. Initial state: [170, 45, 75, 90, 802, 24, 2, 66];
  2. Grouping by the first digit: [170, 90, 802, 2, 24, 45, 75, 66];
  3. Grouping by the second digit: [802, 2, 24, 45, 66, 170, 75, 90];
  4. Grouping by the third digit: [2, 24, 45, 66, 75, 90, 170, 802];

## Search Algorithms

- Linear Search[1]: usually searching for missing or duplicate element in an
  unsorted array. The problem usually involves memory limitations which should
  be balanced with Big-O time efficiency. Constraints make it essential to know
  the Powers of 2 Table and space usage (bits) for storage of integers and
  strings. Using a bit vector/array/list can be useful to store frequencies or
  elements seen. Identify: problem asks to find an element in an unsorted
  structure within memory usage constraint and specifying input size. E.g.
  Missing Int, Find Duplicates, Sort Big File;
- Binary Search[4]: efficiently find an element in a sorted or partially sorted
  structure, usually an array or binary tree.
  1. Initialize middle equals start+(end — start)/2, avoiding overflow;
  2. If the target is equal to element at middle, return True;
  3. If the middle element is too big, search on the left half;
  4. If the middle element is too small, search on the right half;
  5. Finish when searching section reaches size one. Return False if not found;
  - Identify: find an element in a sorted or partially sorted structure or try
    different values on a limited range. E.g. Order-agnostic Binary Search,
    Search in a Sorted Infinite Array, Split Array Largest Sum;
- Quick select[1][30]: used to find the kth smallest or largest element in an
  array in O(n) time, while the worst case is O(n^2) time. In some cases, it
  might be better than sorting in O(nlog(n)) time or using a heap in O(nlog(k))
  time;
  1. Pick a random element in the array and use it as pivot. Partition elements
     around the pivot, tracking the number of elements on the left side;
  2. If there are k elements on the left, return the biggest element from there;
  3. If the left side is bigger than k, repeat the algorithm on the left half;
  4. If the left side is smaller than k, repeat the algorithm on the right, but
     look for the element with rank `k - left_size`;

## Recursion and Iteration Algorithms

- Recursion[1]: there exists one or more base cases, a method that calls itself,
  and variables which after operations converge to the base cases. Try to
  reverse changes made on the variables instead of creating copies. Usually the
  code is easier to write than iteration. However, considering n recursive
  calls, the space complexity is at least O(n) and n<=10,000 due to stack
  overflow. Careful about the base and null cases;
- Iteration: the method does not call itself. Instead it iterates over the input
  (string, array, linked list etc.) and uses stack or queue if necessary for
  processing. The code might be more complicated to write and read, but it has
  the potential to reach the Best Conceivable Runtime and O(1) space, without
  memory limitations;
- Backtracking[6][7]: technique to solve problems usually using recursion, where
  solutions are built one step at a time and whenever a path can no longer lead
  to a valid solution, it is terminated (i.e. we backtrack). Identify: problems
  that might involve recursion where you can construct a partial solution, check
  if the partial solution is valid and verify if the solution is complete. E.g.
  N Queens Problem, Hamiltonian Cycle, Sudoku.

## Dynamic Programming

- Dynamic Programming[1][9][12]: used to improve Big-O efficiency in solutions
  to problems that can be divided into correlated subproblems and there are
  repeated recursive calls.
  - Top-down Dynamic Programming or Memoization: in a recursive solution with
    repeated calls with the same inputs, store the results of subproblems
    (usually in a hash table) and just return the cached results on future
    calls, avoiding re-computation. Reduces Big-O time from exponential to
    polynomial;
  - Bottom-up Dynamic Programming: convert the previous recursive solution into
    iterative solution by noticing that to compute the next subproblem you only
    need the solutions to the previous two or a few subproblems, which can be
    stored in additional variables. Reduces spaces usage from polynomial to
    constant while keeping Big-O time polynomial;
  - Identify: problems that can be divided into subproblems and solved with
    recursion. E.g. Fibonacci Numbers, Coin Change, Ways to Climb Staircase;
- Divide and Conquer[1][12]: divide the problem into independent subproblems of
  the same type, conquer recursively solving the subproblems and combine the
  answers. Ways to divide a problem into subproblems:
  - Top-down: divides the initial problem into N subproblems (which can be
    further divided), converging to a base case, and combines the solution to
    subproblems to solve the original problem. Careful about overlapping
    subproblems. E.g. recursive solution to Generate the Nth Fibonacci Number;
  - Bottom-up: computes the solution for base cases (one or two elements) and
    builds the solution to the next case out of one or more previous cases. E.g.
    iterative solution to Generate the Nth Fibonacci Number;
  - Half-and-half: Divide the initial data in two equal halves, which are
    further divided until they converge to a base case. The solution to the two
    halves can be combined to solve the original problem. E.g. Merge Sort;
- Greedy [8][12][25][26][27]: algorithm used to solve optimization problems that
  can be divided into subproblems with the following properties: there is always
  a valid choice that offers the gratest immediate benefit in the current state;
  the global optimal solution contains the optimal solutions to all subproblems.
  First, prove your algorithm generates a solution that obeys the constraints of
  the problem. Then, prove it maximizes or minimizes the appropriate quantity
  using:
  - Greedy stays ahead: according to some measure,the greedy algorithm always is
    at least as far ahead as the optimal solution during each iteration.
  - Exchange arguments: one can iteratively transform any optimal solution into
    the solution produced by the greedy algorithm without changing the cost of
    the optimal solution;
  - Identify: asked to optimize for certain quantity or there are multiple choices
    and the two properties above are present. E.g. Activity-Selection, Frog
    Jumping, Minimum path Dijkstra, Minimum Spanning Tree, Fractional Knapsack;
- N-ary Choice: problems that involve making a choice between two or more
  options which affect future choices. Examples of choices: include an element
  in the solution set, choose an element to perform an operation, flip a bit
  etc. Usually solved either making all possible choices and searching for a
  valid or optimal state, finding a general rule which allows for always making
  the "correct" choice or iterating backwards to gain future knowledge. E.g.
  Leetcode: Perfect Squares, Coin Change, Non-decreasing Array, Bulb Switcher
  IV, Maximum Length of a Concatenated String with Unique Characters, Avoid
  Flood in The City, Decode Ways, Get the Maximum Score, Subsets, House Robber;

## Knapsack

- Knapsack [36]: problems where there is a set of n items, where each item has
  an associated profit and a corresponding weight, and one must perform a series
  of binary decisions to select a subset of items such that the profit is
  maximized while the cost is kept within constraints. May be solved using
  Dynamic Programming or Greedy.
  - Bounded Knapsack Problem: each item is chosen only a finite amount of times.
    E.g. Partition Equal Subset Sum, Ones and Zeroes;
  - Unbounded Knapsack Problem: no limit on how many times an item is chosen.
    E.g. Coin Change 2;
  - Fractional Knapsack Problem: items can be chosen in partial quantities. Can
    be solved with a greedy approach instead of knapsack;

# References

[1] McDowell, Gayle L. - Cracking the Coding Interview, 6th Edition, 2019.

[2] Mir, Ali - Read this before you start solving problems on Leetcode (Prep
Work), 2019.
<https://medium.com/@alimirio/before-you-start-solving-problems-on-leetcode-prep-work-9d65fc964c6f>

[4] Fahim ul Haq - 14 Patterns to Ace Any Coding Interview Question, 2019.
<https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed>

[6] Geeks for Geeks - Practice For Cracking Any Coding Interview, 2018.
<https://www.geeksforgeeks.org/practice-for-cracking-any-coding-interview/#greedy>

[7] Daily Coding Problem - An Introduction To Backtracking, 2018.
<https://www.dailycodingproblem.com/blog/an-introduction-to-backtracking/>

[8] Li Yin - Greedy Algorithm Explained using LeetCode Problems, 2018.
<https://medium.com/algorithms-and-leetcode/greedy-algorithm-explained-using-leetcode-problems-80d6fee071c4>

[9] Geeks for Geeks - Dynamic Programming, 2018.
<https://www.geeksforgeeks.org/dynamic-programming/>

[10] Prateek Garg - Disjoint Set Union, 2014.
<https://www.hackerearth.com/pt-br/practice/notes/disjoint-set-union-union-find/>

[11] Geeks for Geeks - Disjoint Set (Or Union-Find), 2018.
<https://www.geeksforgeeks.org/union-find/>

[12] Narasimha Karumanchi - Data Structures and Algorithms Made Easy, 2017.
<https://www.docdroid.net/ZPfHmS5/data-structures-and-algorithms-narasimha-karumanchi.pdf>

[16] Ardent Dertat - Programming Interview Questions 11: All Permutations of
String, 2011.
<http://www.ardendertat.com/2011/10/28/programming-interview-questions-11-all-permutations-of-string/>

[17] Geeks for Geeks - Bucket Sort, 2016.
<https://www.geeksforgeeks.org/bucket-sort-2/>

[21] Yangshun Tay - The 30-minute guide to rocking your next coding interview, 2017.
<https://www.freecodecamp.org/news/coding-interviews-for-dummies-5e048933b82b/>

[22] Wikipedia - Sieve of Eratosthenes, 2020.
<https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>

[23] Emre Bolat - Coding Patterns: Bitwise XOR, 2019.
<https://emre.me/coding-patterns/bitwise-xor/>

[24] Emre Bolat - Coding Patterns: Topological Sort, 2019.
<https://emre.me/coding-patterns/topological-sort/>

[25] GeeksForGeeks - Activity Selection Problem.
<https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/>

[26] Tim Roughgarden - Guide to Greedy Algorithms, 2013.
<https://web.stanford.edu/class/archive/cs/cs161/cs161.1138/handouts/120%20Guide%20to%20Greedy%20Algorithms.pdf>

[27] Karleigh Moore - Greedy ALgorithms, 2020.
<https://brilliant.org/wiki/greedy-algorithm/>

[28] Wikipedia - Run-length encoding, 2020.
<https://en.wikipedia.org/wiki/Run-length_encoding>

[29] Wikipedia - Commutative property, 2020.
<https://en.wikipedia.org/wiki/Commutative_property>

[30] GeeksForGeeks - Quick Select Algorithm, 2020.
<https://www.geeksforgeeks.org/quickselect-algorithm/>

[31] GeeksForGeeks - Radix Sort Algorithm, 2020.
<https://www.geeksforgeeks.org/radix-sort/>

[32] jwasham - Coding Interview University, 2020.
<https://github.com/jwasham/coding-interview-university>

[34] John L. Miller - Computer Programming: What maths should I know to crack the Google interview?, 2016.
<https://www.quora.com/Computer-Programming-What-maths-should-I-know-to-crack-the-Google-interview>

[35] Robert Sedgewick - Algorithms, Part II - Radix Sorts, 2018.
<https://www.coursera.org/lecture/algorithms-part2/suffix-arrays-TH18W>

[36] Adam Garcia - Leet Code: Knapsack Problems | Coin Change, 2020.
<https://medium.com/@adameitangarcia/leet-code-knapsack-problems-coin-change-6968a03788c3>
