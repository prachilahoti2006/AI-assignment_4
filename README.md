### AI Assignment 4 – Constraint Satisfaction Problems (CSP)

This assignment demonstrates the application of Constraint Satisfaction Problem (CSP) techniques combined with backtracking to solve various artificial intelligence problems.

### 1. Australia Map Coloring

In this problem, each Australian region (WA, NT, Q, SA, NSW, V, T) is assigned one of three colors: Red, Green, or Blue. The objective is to ensure that no two neighboring regions have the same color. Regions act as variables, colors represent domains, and adjacency rules form the constraints. A backtracking algorithm is used to obtain a valid coloring arrangement.

### 2. Telangana Map Coloring

This problem applies CSP concepts to the 33 districts of Telangana. Each district is assigned one of four colors (Red, Green, Blue, Yellow) while ensuring adjacent districts receive different colors. The solution relies on adjacency relationships and backtracking search to satisfy all constraints.

### 3. Sudoku Solver

The Sudoku puzzle is represented as a CSP where every empty cell is treated as a variable with possible values from 1 to 9. Constraints ensure that each number appears only once in every row, column, and 3×3 subgrid. Backtracking systematically fills empty cells until a valid Sudoku solution is found.

### 4. Cryptarithmetic Problem

This task solves the famous puzzle:

**SEND + MORE = MONEY**

Each letter is assigned a unique digit between 0 and 9. Constraints include distinct digit assignments and non-zero leading digits. Backtracking explores possible assignments until the arithmetic equation is satisfied.

### Main Features

* Implementation based on CSP principles
* Uses backtracking search for solution generation
* Handles different types of AI problems
* Modular and easy-to-understand design
* Enforces problem-specific constraints effectively

### Drawbacks

* Relies only on basic backtracking
* Does not use optimization techniques such as MRV, Forward Checking, or AC-3
* Performance may decrease for larger and more complex CSPs

### Practical Applications

* Geographic map coloring
* Sudoku and logic puzzle solving
* Timetable scheduling
* Resource allocation problems
* Artificial intelligence decision-making systems

### Conclusion

This assignment highlights the effectiveness of CSP and backtracking techniques in solving both logical puzzles and real-world constraint-based problems. By systematically exploring valid assignments while enforcing constraints, these methods provide correct and efficient solutions for a wide range of AI applications.
