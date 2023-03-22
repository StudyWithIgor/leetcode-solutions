# Abstract Analysis

## Concrete Examples [1]

Manually solve concrete instances of the problem and then build a general
solution. Problems that seem hard to solve in the abstract can become much more
tractable after solving concrete instances. The following types of input can
offer great insight:

- Small input: such as array or BST with 5 to 7 elements;
- Extreme or specialized input: such as binary values, non-overlapping
  intervals, sorted arrays, connected graphs etc;

Example: Five hundred closed doors along a corridor are numbered from 1 to 500.
A person walks through the corridor and opens each door. Another person walks
through the corridor and closes every alternate door. Continuing in this manner,
the i-th person comes and toggles the state (open or closed) of every i-th door
starting from Door i. You must determine exactly how many doors are open after
the 500-th person has walked through the corridor.

- Difficult to solve this problem using abstraction: boolean values for the
  state of each door and a state update function;
- Easier to solve with concrete examples: trying the same problem with 1, 2, 3,
  4, 10 and 20 doors, one can easily see that independent of the number of the
  doors, the ones that remain open are always 1, 4, 9, 16... , so the doors that
  remain open are the perfect squares. The proof for the general case should be
  trivial. The number of the doors that remain open is the square root of the
  total number of doors;

## Case analysis [1]

Split the input or execution into a number of cases and solve each case in
isolation. Problem is divided into a number of separate cases, and analyzing
each case solves the original problem. Cases don't have to be mutually
exclusive. However, they must be exhaustive, that is cover all possibilities.
Example: for all n, `n mod 3` is 0, 1 or 8. Considering the cases `n=3m`,
`n=3m+1` and `n=3m+2` is sufficient to solve the problem, because they are easy
to prove and exhaustive;

Example 2: given a set S of 25 integers and a CPU with the SORT5 instruction
(sort five integers in one cycle), identify the largest, second-largest and
third-largest element in S, minimizing the number of calls to SORT5;

- To find the largest integer, split the set into five disjoint sets and sort
  them individually. Then take the largest element in each set, forming a new
  set of five elements, and sort it to find the largest element. The total
  number of calls to SORT5 is six, but there is ambiguity about the second and
  third largest elements;
- A careful analysis eliminating all X from S for which there are at least three
  integers in S larger than X should be made. Only five integers remain, so one
  more call to SORT5 is enough to compute the result;

## Iterative refinement [1]

- Many problems can be solved correctly by a simple algorithm that has a high
  time or space complexity, which is called a brute-force, exhaustive search or
  generate-and-test. Find such solution and improve upon it;
- Often this brute-force can be refined to a faster one, but even if not, it
  offers hints about the nature of the problem;
- Example 1: write a function that takes an array A of n numbers, and rearranges
  A’s elements to get a new array B having the property that B[0] ≤ B[1] ≥ B[2]
  ≤ B[3] ≥ B[4] ≤ B[5]...
  - Approach 1: sort the array and interleave the bottom and the top halves.
    Alternatively, sorting and swapping the elements in pairs also works. Both
    are O(n\*log(n)) time solutions;
  - Approach 2: realize it is not necessary to sort the whole array. Rearranging
    the elements around the median and then performing the interleaving works.
    Median finding can be done linearly, so this solution is O(n) time;
  - Approach 3: notice the necessary order is very local, so finding the median
    is not necessary. The following approach works.
    - Swap A[i] and A[i+1] when:
      - i is even and A[i] > A[i+1]; OR
      - i is odd and A[i] < A[i+1];
    - This solution is O(n) time. However, as benefits it is much easier to
      implement and it never needs to store more than two elements in memory or
      read a previous element;
- Example 2: given two strings s (search string) and t (text), find all
  occurrences of s in t. (For Big-O, n and m are the lengths of s and t)
  - Approach 1: test for a match at every offset. O(n\*m) time solution;
  - Approach 2: working with examples show a few ways to improve it. If the
    character t[i] is not present in s you can advance the matching by n
    characters. Also, skipping works better if we match the search string from
    its end and work backwards. It makes the algorithm linear time on random
    strings, but the worst case is still O(n\*m) time;
  - Approach 3: make the additional observation that a partial match of s that
    does not result in a full match implies other offsets that cannot lead to
    full matches.
    - If s="abdabcabc" and if, starting backwards, we have a partial match up to
      "abcabc" that does not result in a full match, we know that the next
      possible matching offset has to be at least three positions ahead (where
      we can match the second "abc" from the partial match);
    - Together with the other optimizations, one can derive the Boyer-Moore
      string search algorithm, which is O(n+m) time worse case;
- Example 3: compute the maximum subarray sum for an integer array of length n;
  - Approach 1: compute the sum of all subarrays. O(n^3) time;
  - Approach 2: precompute the sum of the prefixes of the array. O(n^2) time;
  - Approach 3: the natural divide-and-conquer algorithm is O(n log n) time;
  - Approach 4: observe that a maximum subarray must end at one of n indices,
    and the maximum subarray sum for a subarray ending at index i can be
    computed from previous maximum subarray sums. O(n) time solution;

## Reduction [1]

- Use a well-known solution to some other problem as a subroutine;
- Usually, try to reduce the given problem to an easier problem;
- Sometimes it is necessary to reduce the given problem to a problem known to be
  difficult. This justifies heuristics and approximate solutions;
- Example: determine if one string is a rotation of the other, e.g.,“car” and
  “arc” are rotations of each other;
  - Approach 1: rotate the first string by every possible offset and then
    compare it with the second string. O(n^2) time solution;
  - Approach 2: notice that this problem is quite similar to string search,
    which can be done in linear time, albeit using a somewhat complex algorithm;
    - If we concatenate the second string with itself and search for the first
      string in the resulting string, we will find a match if the two original
      strings are rotations of each other. O(n) time solution;

## Graph modelling [1]

- Drawing pictures is great to brainstorm solutions;
- If the relationships in a problem can be represented as a graph, often the
  problem can be reduced to a well-known graph problem;
- Example: given a set of exchange rates among currencies, determine if an
  arbitrage exists, in other words, there is a way by which you can start with
  one unit of some currency C and perform a series of barters which results in
  having more than one unit of C.

```
Exchange rates for seven major currencies.
Symbol USD EUR GBP JPY CHF CAD AUD
USD 1 0.8148 0.6404 78.125 0.9784 0.9924 0.9465
EUR 1.2275 1 0.7860 96.55 1.2010 1.2182 1.1616
GBP 1.5617 1.2724 1 122.83 1.5280 1.5498 1.4778
JPY 0.0128 0.0104 0.0081 1 1.2442 0.0126 0.0120
CHF 1.0219 0.8327 0.6546 80.39 1 1.0142 0.9672
CAD 1.0076 0.8206 0.6453 79.26 0.9859 1 0.9535
AUD 1.0567 0.8609 0.6767 83.12 1.0339 1.0487 1
```

- An arbitrage is possible for this set of exchange rates: 1 USD → 1 × 0.8123 =
  0.8123 EUR → 0.8123 × 1.2010 = 0.9755723 CHF → 0.9755723 × 80.39 =
  78.426257197 JPY → 78.426257197 × 0.0128 = 1.00385609212 USD;
- Approach: model the problem with a graph.
  - Currencies correspond to vertices, exchanges corresponding to edges and edge
    weight as the logarithm of the exchange rate;
  - If the graqph contains a cycle with positive weight, we found such series of
    exchanges. This can be solved using the Bellman-Ford Algorithm;
- Painting boolean matrix and string trasnformation are examples of problems
  that can be modelled with graphs;

# Reference

[1] Adnan Aziz - Elements of Programming Interviews, 2014.
