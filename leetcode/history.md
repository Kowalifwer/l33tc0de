## 21.12.2023 Thursday

* [ ] [155. Min Stack](https://leetcode.com/problems/min-stack/)
* [ ] [150. Evaluate Reverse Polish Notat](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
* [ ] [167. Two Sum II - Input Array Is Sor](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) [2 pointer]
* [ ] [704. Binary Search](https://leetcode.com/problems/binary-search/) [binary search, with mid = (l + r)//2 OR better l+ (r - l) // 2))]
* [ ] [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) [binary search, but pretend array is flattened, and carefuly find correct indecies]
* [ ] [153. Find Minimum in Rotated Sort](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) [TRICKY - check if half of array is sorted in order to find pivot, arr is guaranteed to be in at most two sorted subarrays ]
* [ ] [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) [understood the iterative, not the recursive]
* [ ] [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) [Dummy node concept helps]
* [ ] 143 [Reorder List](https://leetcode.com/problems/reorder-list/submissions/1125409026/) - slow,fast to find middle -> make copy for RHS, and cut original link -> reverse all after middle. Then iterate down both lists.
* [ ] 19 [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) -> dummy node + fast/slow. fast must advance n forward, then both fast and slow go until fast reaches end. slow is therefore one before the deletion marker.

# 22.12.2023 Friday

* [ ] [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) - 1 run make map from old to new, 2 run update new nodes w old data
* [ ] [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) - simple left-right switch into recursion for all nodes
* [ ] [104. Maximum Depth of Binary Tre](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - 3 ways, recursive (1 + max(left, right)), BFS w queue, iterativeDFS
* [ ] [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) - similar  to height, get max of each subtree but -1 on base case. max(2 + left + right) for diameter stuff
* [ ] [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) - max height at l,r and make sure l > r not by 1
* [ ] [100. Same Tree](https://leetcode.com/problems/same-tree/) - done with generator - prolly better elsehow. check next for is_same proper
* [ ] [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) - use is_same (recurse to every node, false if different) -> then use on all nodes
* [ ] [102. Binary Tree Level Order Trave](https://leetcode.com/problems/binary-tree-level-order-traversal/) - basic DFS tree traversal - then print or return all from current queue level
* [ ] [46. Permutations](https://leetcode.com/problems/permutations/) - DFS backtrack memes, I looped over all and ignore existing with i== check
* [ ] [78. Subsets](https://leetcode.com/problems/subsets/) - DFS backtrack, 2 paths - 1 adds next item, 1 does not add - eventually branch to all options
* [ ] [39. Combination Sum](https://leetcode.com/problems/combination-sum/) - check all possitibilites, and return em
* [ ] [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) - go over all rows, all colls, all 9 subsquares and make sure conditions hold

# 23.12.2023 Saturday

* [ ] [235. Lowest Common Ancestor of](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) - only move down next root (left or right) IF left is < root and right is > root. IF IT SPLITS - means we are at the LCA.
* [ ] [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) - BFS and return rightmost item
* [ ] [1448. Count Good Nodes in Binary](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) - update thereshold/allowedMin after each node, to max of current val and existing limit. make this local to each search (left and right) -
* [ ] [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) - FIRST, make sure next child nodes are correct (easy part) -> NEXT, make sure ANY following node, follows the boundaries between min < node.val < max. Update these as you go, depending which side we branch into.
* [ ] [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) - do the left print right search, k-- until k=0, then return the minimum.
* [ ] [701. Insert into a Binary Search Tre](https://leetcode.com/problems/insert-into-a-binary-search-tree/) - iteratively easy, just check each time whether to go left or right, if none - insert.
* [ ] [90. Subsets II](https://leetcode.com/problems/subsets-ii/) - not complete.

# 24.12.2023 Sunday

* [ ] [79. Word Search](https://leetcode.com/problems/word-search/) - juicy backtrack, not bad, more about 2d array manipulation with visited state management.
* [ ] [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) - min heap HEAPQ stuff
* [ ] [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - backtracking silinness - manage state of n_open and n_closed brackers
* [ ] [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) - chill heapq. uses python comparison property to our advantage here!
* [ ] [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/) - filler, to relax
* [ ] [705. Design HashSet](https://leetcode.com/problems/design-hashset/) - filler to relax, but use chain pointers with dummy node
* [ ] [1721. Swapping Nodes in a Linked](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) - move left pointer to k. set exhaust pointer to left. move right until exhaust pointer reaches the end. that way you get k and -k -> swap values.
* [ ]
