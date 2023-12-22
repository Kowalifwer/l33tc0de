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
* [ ] [100. Same Tree](https://leetcode.com/problems/same-tree/) - done with generator - prolly better elsehow.
* [ ] [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) -
