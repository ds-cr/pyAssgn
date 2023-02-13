# pyAssgn

### Approach
Mark all the O(s) that are connected to boundary *(directly or indirectly)*. Then traverse the matrix and convert all the non-marked Os.

### Implementation (BFS)
Basically all the O on the borderline of the squaure and the O which connect to them would not be transformed.
1. Take input from user using `iter` and `input`.
2. Make an object of `Solution` class. Call its `solve` function.
3. Inside the solve function to make an empty array named `searchArray`. This will serve the purpose of storing the indexes of unfit Os.
4. Then traverse all the columns and rows. For each index if the value is 'O' append it to array and call the `callBFS` function on it.
5. The function marks the cell. It then traverses the `searchArray` and for each index it checks its neighbours, marks them if they are O and appends them to the array.
6. Finally traverse the matrix again. Convert all the Os to X and all the Ps to O.

**Time Complexity** - O(m\*n)<br>
**Space Complexity** - O(m\*n)<br>
<font size = "0.1"> *where m is row size and n is column size of matrix* </font>

Proof

<img width="330" alt="image" src="https://user-images.githubusercontent.com/68206552/215169905-97076c43-3475-42de-8722-66a3b12937fa.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/68206552/215169954-b73ea270-f042-4568-a368-3efb366a62e8.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/124337721/218432092-ce46193f-3771-4f8f-9273-7226e6c96845.png">
