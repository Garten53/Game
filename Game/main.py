import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    data_idx = 0
    num_tests = int(input_data[data_idx])
    data_idx += 1
    
    for _ in range(num_tests):
        board = []
        for r in range(19):
            row = []
            for c in range(19):
                row.append(int(input_data[data_idx]))
                data_idx += 1
            board.append(row)
        
        winner = 0
        win_pos = None

        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

        found = False
        for j in range(19):
            for i in range(19):
                if board[i][j] == 0:
                    continue
                
                color = board[i][j]
                
                for dr, dc in directions:
                    prev_r, prev_c = i - dr, j - dc
                    if 0 <= prev_r < 19 and 0 <= prev_c < 19:
                        if board[prev_r][prev_c] == color:
                            continue
                    
                    count = 1
                    curr_r, curr_c = i + dr, j + dc
                    
                    while 0 <= curr_r < 19 and 0 <= curr_c < 19 and board[curr_r][curr_c] == color:
                        count += 1
                        curr_r += dr
                        curr_c += dc
                    
                    if count == 5:
                        winner = color
                        win_pos = (i + 1, j + 1) 
                        found = True
                        break
                if found: break
            if found: break
        
        print(winner)
        if winner != 0:
            print(f"{win_pos[0]} {win_pos[1]}")

if __name__ == "__main__":
    solve()