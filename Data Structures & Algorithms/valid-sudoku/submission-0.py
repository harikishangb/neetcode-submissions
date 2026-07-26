class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if num in row[i]:
                    print(f"Duplicate {num} found in row {i}")
                    return False
                if num in cols[j]:
                    print(f"Duplicate {num} found in column {j}")
                    return False
                if num in boxes[box_index]:
                    print(f"Duplicate {num} found in box {box_index}")
                    return False

                row[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True