### Logic
##### Only the O(s) not connected to boundary will change. So traverse the boundary and mark all the connected O(s) by flag value. Finally traverse the array again converting values accordingly.

### Implementation (DFS)
Link - https://github.com/jasveen18/Python_Assignment/blob/main/python1.py

1. Take input from user regarding no. of *rows and columns*.
2. Call two `for loops` to take input row wise.
3. Call the dfs function on the four boundaries of the matrix.
4. Each call to `dfs` will check two things in the `or` condition -
    * If the current index is not inside the boundary
    * The value is not 'O'
    
    If any of the above satisfies the return <br>
    Else turn the value to flag value and call `dfs` on its neighbours.

5. After taking dfs on all four boundaries we simply traverse the matrix again, converting any O to X and any A to O.

**Time Complexity** - O(m\*n)<br>
**Space Complexity** - O(m\*n)<br>
<font size = "0.1"> *where m is row size and n is column size of matrix* </font>
