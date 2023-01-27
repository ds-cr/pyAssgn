# pyAssgn

Used BFS approach to solve the problem
Basically all the O on the borderline of the squaure and the O which connect to them would not be transformed.
So basically I traverse the bordreline find the O, start a bfs on that.
For all the O's that would not transform I change them into P(chose randomly)
Then I traverse the full matrix and change all the remaining O to X and the P to O.

Proof
<img width="330" alt="image" src="https://user-images.githubusercontent.com/68206552/215169905-97076c43-3475-42de-8722-66a3b12937fa.png">
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/68206552/215169954-b73ea270-f042-4568-a368-3efb366a62e8.png">
