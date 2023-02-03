### Logic
##### Only the O(s) not connected to boundary will change. So traverse the boundary and mark all the connected O(s) by flag value. Finally traverse the array again converting values accordingly.

### Implementation (BFS)
Link - https://github.com/praneeth-0501/Python_Assignment/blob/main/python_assignment.py

1. Call the `solve` *(bfs function)* by passing the matrix. Make empty *dequeue* and get the dimensions of matrix in two variables.
2. Traverse the boundaries and store the index of any O in the dequeue. The dequeue will be used to store the index of all boundary connected O(s). Also mark that O with flag value.
3. Now traverse the dequeue, every time popping an element exploring its neighbours. <br>
    If any of the neighbours are O change their value to flag value and push their indexes to the dequeue.
4. Continue this until the dequeue is empty.
5. Finally traverse the matrix again, converting every O to X and every K (flag value) to O.

**Time Complexity** - O(m\*n)<br>
**Space Complexity** - O(m\*n)<br>
<font size = "0.1"> *where m is row size and n is column size of matrix* </font>
