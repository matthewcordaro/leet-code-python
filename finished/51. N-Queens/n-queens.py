class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    # Constraint Variables
    column = set()
    positive_diagonal = set()  # (r + c)
    negative_diagonal = set()  # (r - c)

    # All possible board layouts
    solutions = []

    # Empty Board to work with
    board = [["."] * n for i in range(n)]

    # Exploring by Row
    def explore(r):
      # Base Case:  Got to the end and found a solution!
      if r == n:
        # combine the row into one string to match the requested format
        copy = ["".join(row) for row in board]
        solutions.append(copy)
        return

      # Let's go through
      for c in range(n):
        # Check our constraints!
        # If anything fails, we've reached the end of this exploration; backtrack.
        if c in column \
            or (r + c) in positive_diagonal \
            or (r - c) in negative_diagonal:
          continue

        # Otherwise, since we are valid...
        # Let's add our newly constrained locations to their variables
        column.add(c)
        positive_diagonal.add(r + c)
        negative_diagonal.add(r - c)
        board[r][c] = "Q"

        # Time to explore forward!
        explore(r + 1)

        # Undo then placement and go up a row to try other ways...
        # Remove the queen we placed.
        column.remove(c)
        positive_diagonal.remove(r + c)
        negative_diagonal.remove(r - c)
        board[r][c] = "."

    # Execute our exploring (backtracking) algo and return solution.
    explore(0)
    return solutions