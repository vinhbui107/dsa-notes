import collections


class Solution:
    """
    https://leetcode.com/problems/valid-sudoku

    >>> solution = Solution()
    >>> board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    >>> solution.isValidSudoku(board=board)
    True
    >>> solution.isValidSudoku_string(board=board)
    True
    """
    def isValidSudoku(self, board) -> bool:
        row_seen = collections.defaultdict(set)
        col_seen = collections.defaultdict(set)
        sub_seen = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                current_value = board[row][col]

                if current_value == ".":
                    continue

                if (
                    current_value in row_seen[row] or
                    current_value in col_seen[col] or
                    current_value in sub_seen[(row//3, col//3)]
                ):
                    return False

                row_seen[row].add(current_value)
                col_seen[col].add(current_value)
                sub_seen[(row//3, col//3)].add(current_value)

        return True

    # Using string to solve
    def isValidSudoku_string(self, board) -> bool:
        seen = set()

        for row in range(9):
            for col in range(9):
                current_value = board[row][col]

                if current_value == ".":
                    continue

                row_value = f"{current_value} in row {row}"
                col_value = f"{current_value} in col {col}"
                sub_value = f"{current_value} in sub {row//3}-{col//3}"

                if (
                    row_value in seen or
                    col_value in seen or
                    sub_value in seen
                ):
                    return False

                seen.add(row_value)
                seen.add(col_value)
                seen.add(sub_value)

        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
