# Advanced Patterns

## NP-hard Problems

- NP-hard Problems: set of problems whose polynomial solution is unknown:
  - Hamiltonian Cycle[1]: given an undirected complete graph (each vertex is
    connected through an edge), find the number of different Hamiltonian Cycles
    in the graph (closed walks where each vertex is visited only once, not
    necessarily using all the edges). I only found O(n!) (factorial) time
    solution so far;
  - Travelling Salesman[2]: given a set of cities and distance between every
    pair of cities, find the shortest possible route that visits every city only
    once and returns to the starting point. This means there is a graph with
    weighted edges and multiple Hamiltonian Cycles, and you must find the cycle
    with lowest possible sum. There is a brute force O(n!) (factorial) time
    solution, and other using dynamic programming which is O(n^3) time;
  - Subset Sum[3]: given a set of non-negative integers and a value given_sum,
    check if there is a subset whose elements sum to given_sum. There is a brute
    force O(n!) (factorial) time solution and a dynamic programming
    O(given_sum\*n) time solution;

## Heuristic [14]

Heuristic is a technique for solving a problem more quickly when classic methods
are too slow, or for finding an approximate solution when classic methods fail to
find any exact solution. This is achieved by trading optimality, completeness,
accuracy, or precision for speed. In a way, it can be considered a shortcut.

- Optimality: When several solutions exist for a given problem, does the heuristic
  guarantee that the best solution will be found? Is it actually necessary to find
  the best solution?
- Completeness: When several solutions exist for a given problem, can the heuristic
  find them all? Do we actually need all solutions? Many heuristics are only meant to
  find one solution;
- Accuracy and precision: Can the heuristic provide a confidence interval for the
  purported solution? Is the error bar on the solution unreasonably large?
- Execution time: Is this the best known heuristic for solving this type of problem?
  Some heuristics converge faster than others. Some heuristics are only marginally
  quicker than classic methods;

### Example: travelling salesman problem

The travelling salesman problem is "Given a list of cities and the distances between
each pair of cities, what is the shortest possible route that visits each city and
returns to the origin city?"TSP is known to be NP-Hard so an optimal solution for
even a moderate size problem is difficult to solve. Instead, the greedy algorithm
can be used to give a good but not optimal solution (it is an approximation to the
optimal answer) in a reasonably short amount of time. The greedy algorithm heuristic
says to pick whatever is currently the best next step regardless of whether that
prevents (or even makes impossible) good steps later. It is a heuristic in that
practice says it is a good enough solution, theory says there are better solutions
(and even can tell how much better in some cases).

## Shortest Path In Graph

- Dijkstra's Algorithm[5]: find the smallest cost path from one node to all
  others in a weighted directed graph, which may contain cycles. Negative edges
  are not allowed. It is a greedy algorithm:
  1. Create a representation of the graph that maps from a node to its neighbors
     with their associated edge cost, if not provided;
  2. Implement a system to deal with cycles, such as a `visited` set or maximum
     number of nodes seen;
  3. Create a min heap with comparison on total travel cost and accumulate the
     cost on insertion of neighbors in the heap;
  4. Terminate when either the destination is reached or the min heap is empty;
  - Identify: problems that involve finding the shortest or cheapest path
    between one or more source nodes and one or more destination nodes in a
    graph. E.g. Cheapest Flights Within K Stops, Shortest Path with Alternating
    Colors, Network Delay Time;
- Bellman-Ford Algorithm[6][11]: find the smallest cost path from one node to
  all others in a weighted directed graph, which may contain cycles. Negative
  edges are allowed, but negative cycles are not. Input should be a graph with
  directed weighted edges, a source node, the number of vertex in the graph, and
  a way how to iterate over the list of edges. It is not greedy:
  1. Initialize an array `dist`, where `dist[i]` represents the minimum distance
     to reach node `i` from the `source`;
  2. Iterate over the list of edges `num_vertex-1` times. Since the graph does
     not contain any cycles, the shortest path to any node contains at most
     `num_vertex-1` edges. All paths with more edges contain a cycle, therefore
     there is an edge that can be removed to make the path shorter;
  3. On each pass, check if the source node of this edge is "reachable". If yes,
     then check if adding this edge makes the path to destination of this edge
     shorter. If yes, then update the minimum distance path to destination of
     edge.
     - The reason is that it should work independent of the processing order of
       the edges relative to the source node;
  4. Make a final pass to the list of edges, identical to the ones before. If a
     path can get even shorter, there is a negative cycle in the graph, so throw
     an error;
- Floyd-Warshal Algorithm[7]: find the smallest cost path between all pairs of
  vertices in a weighted directed graph, which may contain cycles. Negative
  edges are allowed, but negative cycles are not.
  1. Initialize an nXn 2D array dist where dist[i][j] is the minimum distance
     from node i to node j, initially with infinity;
  2. Fill in the main diagonal with zeros (distance from a node to itself);
  3. Loop over the edges (i,j) and place their values at dist[i][j];
  4. In a triple for loop over vertex with i,j,k, if dist[i][j] is greater than
     dist[i][k]+dist[k][j], replace it with the calculated value;
  5. O(e+v^3) time and O(v^2) space;

## Minimum Spanning Tree

- Minimum spanning tree: subset of the edges of a connected, edge-weighted
  undirected graph that connects all the vertices together, without any cycles
  and with the minimum possible total edge weight.
- Kruskal's algorithm[8]: finds the Minimum Spanning Tree in O(e\*log(e)) time,
  limited by sorting the edges. Only works if the Minimum Spanning Tree exists;
  1. Obtain a list of all edges in the graph, with source, destination and
     weight. Sort it in ascending order by weight;
  2. Iterate over list of edges left to right. Check if including the current
     edge would lead to a cycle using Disjoint Set Union. If it does not lead to
     a cycle, include this edge in the Minimum Spanning Tree;
  3. Format the Minimum Spanning Tree output from the selected edges;
- Prim's algorithm[9]: finding the minimum spanning tree complexity depends on
  implementation:
  - Adjacency matrix and searching: O(v^2) time;
  - Binary head and adjacency list: O((v+e)\*log(v)) time;

## Fenwick Tree [4]

- Common implementation of the sum of elements between indices in an array is
  O(n) time and O(1) space. Common implementation of increment by `x` an element
  in any index of an array is O(1) time and O(1) space. Fenwick Tree is a data
  structure represented by a tree and implemented with a array that makes both
  of these operations O(log(n)) time and O(1) space;
- The array used for the tree is one unit larger than the original array, and
  initialization usually takes O(n) time. It is used when there will be many
  updates on the elements of an array and fast computation of sum over range
  indexes is required;
- Example

arr=[1,-7,15,9,4,2,0,10]

8+1=9 blocks => 4 bits

Each level uses a number of bits equal to its value

To go from child to parent in indices values of the tree, remove the rightmost
set bit: `parent_i = i - (i & -i)`

```
Tree of indices

  ______0_______
 /     /  \     \
1    10   100  1000
    /     / \
   11    101 110
              /
            111
```

1. Accumulatively sum the array and insert in the tree
   running=[1,-6,9,18,22,24,24,34]

```
  ______0_______
 /     /  \     \
1    -6   18    34
    /     / \
    9    22 24
            /
           24
```

2. Using the formula to access the parent, subtract the value of the parent from
   each node

```
  ______0_______
 /     /  \     \
1    -6   18    34
    /     / \
   15    4   6
            /
           0
```

3. To get the sum of all values between 0 and 6, for example, sum all node
   values in the tree until you reach index 7: 0->18->6->0 = 24

- Below there is a simple implementation of a Fenwick Tree;

```
class NumArray(object):
    def __init__(self, nums):
        self.nums=nums
        self.fw=[0 for _ in range(len(nums)+1)]

        if not nums:
            return

        self.fw[1]=nums[0]

        for i in range(len(nums)):
            self.fw[i+1]=self.fw[i]+nums[i]

        for i in range(len(nums),0,-1):
            parent=i-(i&-i)
            if parent >=0:
                self.fw[i]-=self.fw[parent]
        return

    def sumStart(self,i):
        total=0
        while i:
            total+=self.fw[i]
            i=i-(i&-i)
        return total

    def increment(self,i,val):
        i+=1
        while i<=len(self.nums):
            self.fw[i]+=val
            i=i+(i&-i)
        return

    def update(self,i,val):
        extra=val-self.nums[i]
        self.nums[i]=val
        self.increment(i,extra)

    def sumRange(self,i,j):
        return self.sumStart(j+1)-self.sumStart(i)
```

## Tail Recursion [15]

Special type of recursive function where no other operations are performed after
the recursive call. In languages that offer tail recursion optimization, code is
compiled such that the current stack frame is reused, so recursion does not
consume any stack space and it prevents overflow. Python does not offer this
optimization, and it should be used with care, code reliability should not rely
on a compiler optimization;

## Leetcode Notes by kamyu104 [10]

### Sequence (Array, String, Linked List)

- Sliding Window
- Two Pointers
- String (Rearrange Words in a Sentence)
- de Bruijn sequences
- Regex (Find Users With Valid E-Mails, Patients With a Condition)
- LinkedHashSet

### Stack and Queue

- Deque
- Mono Deque
- Mono Stack

### Bit Manipulation

- Bit Manipulation
- Lyndon word

### Tree

- BST
- MST
- Heap
- Trie
- Morris Traversal
- Suffix Tree
- Segment Tree
- Fenwick Tree
- Ukkonen's Algorithm
- Pruning

### Graph

- DFS
- BFS
- 0-1 BFS
- Union Find
- Dijkstra's Algorithm
- Floyd-Warshall Algorithm
- Kruskal's Algorithm
- A\* Search Algorithm
- Tarjan's Algorithm
- Bridge Finding Algorithm
- Hopcroft-Karp Bipartite Matching
- Hungarian Bipartite Matching

### Search

- Binary Search
- Binary Jump
- Quick Select
- Boyer–Moore Majority Vote Algorithm
- Rabin-Karp Algorithm
- Aho-Corasick Algorithm
- KMP Algorithm
- Manacher's Algorithm

### Sort

- Merge Sort
- Quick Sort
- Counting Sort
- Bucket Sort
- Topological Sort

### Dynamic Programming

- DP
- Memoization
- Greedy
- Divide and Conquer
- Backtracking
- Minimax or Saddle Point

### Math

- Matrix Exponentiation
- Fast Wavelet Transform (FWT) (Triples with Bitwise AND Equal To Zero)
- Zeller Formula
- Bézout's identity
- Cantor Ordering
- Math (Maximum Average Subarray I, Path In Zigzag Labelled Binary Tree, 4 Keys
  Keyboard, Minimum Knight Moves, Count Numbers with Unique Digits,Allocate
  Mailboxes, Integer Replacement)
- Catalan Number
- Binomial Coefficients
- Inclusion-Exclusion Principle

### Geometry

- Convex Hull
- Monotone Chain
- Geometric Median
- Gradient Descent
- Weiszfeld's Algorithm

### Other

- Tricky
- Line Sweep
- OrderedDict
- Hash
- Iterator
- Automata (Valid Number)
- Reservoir Sampling
- Generating Function
- Tri Partition
- Precompute (Stepping Numbers)
- Simulation (Contain Virus, Check if There is a Valid Path in a Grid)

# Discrete Mathematics [12]

- Theoretical Computer Science;
  - Computability;
  - Automata theory;
  - Petry nets and process algebras;
  - Computational geometry;
- Information theory;
  - Coding theory;
  - Analog signals, coding and encryption;
- Logic;
  - Inference, consistency, soundness and completeness;
  - Truth table;
  - Logic formulas and directed acyclic graphs;
  - Fuzzy and Infinitary logic;
- Set theory;
  - Countable and partially ordered sets;
  - Gerog Cantor;
  - Descriptive set theory;
- Combinatorics;
  - Enumerative combinatorics: permutations, combinations and partitions;
  - Analytic combinatorics: complex analysis and probability theory;
  - Design theory and partition theory;
- Graph theory;
  - Graphs and networks;
  - Topology and knoth theory;
  - Algebraic graph theory;
  - Continuous graphs;
- Probability;
  - Count observations;
  - Discrete probability distributions;
  - Enumerative combinatorics;
- Number theory;
  - Geometry of numbers;
  - Analytic number theory;
  - Transcendental numbers, diophantine approximation, p-adic analysis and function fields;
- Algebraic structures or abstract algebra;
  - Boolean algebra: logic gates and programming;
  - Relational algebra: databases;
  - Algebraic coding theory: discrete and finite versions of groups, rings and fields;
  - Theory of formal languages: discrete semigroups and monoids;
- Calculus of finite differences, discrete calculus or discrete analysis
  - Sequence: function defined on an interval of the integers;
  - Recurrence relation and difference equation;
  - Discrete transforms;
  - Finite metric and topological spaces;
- Geometry;
  - Discrete geometry;
  - Computational geometry;
- Topology;
  - Topological invariants;
  - Combinatorial topology, topological graph theory, topological combinatorics,
    computational topology, discrete and finite topological space;
- Operations research;
  - Linear programming;
  - Optimization, queuing theory, scheduling theory, and network theory;
  - Continuous-time Markov process, continuous-time martingales, process optimization
- Game theory, decision theory, utility theory, social choice theory;
- Discretization;
  - Numerical analysis;
- Discrete analogues of continuous mathematics;
- Hybrid discrete and continuous mathematics;

# Intractability [13]

- Often real-life problems can be solved with efficient algorithms such as
  binary search and shortest path, or meta-algorithms like DP. May be hard to
  identify because the algorithmic core is hidden by the details;
- Sometimes the problem is intractable, i.e. there is no efficient algorithmic
  solution. Intractability can be proven by picking a known intractable problem
  and transforming it into the problem given;
- Approaches to solve intractable problems:
  - brute-force or dynamic programming solutions with exponential complexity;
  - search algorithms like backtracking, branch-and-bound and hill-climbing;
  - heuristics based on insight, common case analysis, and careful tuning;
  - parallel algorithms, with a large number of computers that can work on
    subparts simultaneously;
- Don’t forget it may be possible to dramatically change the problem formulation
  while still achieving the higher level goal;

# Alphabet Terminology [16]

## Pangram

A phrase or sentence containing all 26 letters of the alphabet (ideally repeating as few letters as possible). You may remember this one from typing class: "The quick brown fox jumped over the lazy sleeping dog," but Willard Espy came up with a shorter and more interesting one: "Bawds jog, flick quartz, vex nymphs." An abundance of pangrams, using some very obscure words or initials can be found here.

## Palindrome

A word, sentence, or longer written work that reads the same backwards. Example: A declaration facetiously attributed to Napoleon, "Able was I ere I saw Elba." Weird Al Yankovic's song "Bob" spoofs Bob Dylan's "Subterranean Homesick Blues" using a slew of palindromes. Need more palindromes? Find a huge stash here.

## Anagram

A word or phrase formed by rearranging the letters of another word or phrase. The English word anagram goes back to 1589. Grambs uses the word transposal in this general sense, and anagram more narrowly to mean a transposal of letters resulting in synonymous term. Others call these particularly apt anagrams "aptigrams." For example: Villainousness is an anagram of "an evil soul's sin."

# References

[1] Geeks for Geeks - Number of Hamiltonian cycle, 2018.
<https://www.geeksforgeeks.org/number-of-hamiltonian-cycle/>

[2] Geeks for Geeks - Travelling Salesman Problem, 2018.
<https://www.geeksforgeeks.org/travelling-salesman-problem-set-1/>

[3] Geeks for Geeks - Subset Sum Problem, 2018.
<https://www.geeksforgeeks.org/subset-sum-problem-dp-25/>

[4] Nideesh Terapalli - Fenwick Tree and Leetcode 307 Range Sum Query - Mutable, 2020.
<https://www.youtube.com/watch?v=GURRzAKL1lY>

[5] McDowell, Gayle L. - Cracking the Coding Interview, 6th Edition, 2019.

[6] Michael Sambol - Bellman-Ford in 4 minutes — Theory, 2015.
<https://www.youtube.com/watch?v=9PHkk0UavIM>

[7] Michael Sambol - Floyd-Warshal in 4 minutes, 2016.
<https://www.youtube.com/watch?v=4OQeCuLYj-4>

[8] Michael Sambol - Kruskal's algorithm in 2 minutes — Review and example, 2012.
<https://www.youtube.com/watch?v=71UQH7Pr9kU>

[9] Michael Sambol - Prim's algorithm in 2 minutes — Review and example, 2012.
<https://www.youtube.com/watch?v=cplfcGZmX7I>

[10] kamyu104 - Leetcode Solutions, 2020.
<https://github.com/kamyu104/LeetCode-Solutions>

[11] Himanshu Garg - Bellman–Ford Algorithm | DP-23, 2020.
<https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/>

[12] Wikipedia - Discrete Mathematics, 2020.
<https://en.wikipedia.org/wiki/Discrete_mathematics>

[13] Adnan Aziz - Elements of Programming Interviews, 2014.

[14] Wikipedia - Heuristic (computer science), 2020.
<https://en.wikipedia.org/wiki/Heuristic_(computer_science)>

[15] Tikhon Jelvis - What is tail recursion? Why is it so bad?, 2017.
<https://www.quora.com/What-is-tail-recursion-Why-is-it-so-bad>

[16] Judith B. Herman - Palindromes, anagrams, and 9 other names for alphabetical antics, 2013.
<https://theweek.com/articles/464433/palindromes-anagrams-9-other-names-alphabetical-antics>
