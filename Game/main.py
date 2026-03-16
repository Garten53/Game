import sys

BOARD_SIZE = 19
WIN_STREAK = 5

def parse_board(input_data, start_idx):
    
    board = []
    current_idx = start_idx
    for row_idx in range(BOARD_SIZE):
        row = []
        for col_idx in range(BOARD_SIZE):
            try:
                val = int(input_data[current_idx])
            except (ValueError, IndexError):
                raise ValueError(f"На позиції {current_idx} знайдено не число або дані закінчилися.")
            
            
            if val not in (0, 1, 2):
                raise ValueError(f"Некоректне значення {val} на ({row_idx}, {col_idx}). Очікується 0, 1 або 2.")
                
            row.append(val)
            current_idx += 1
        board.append(row)
    return board, current_idx

def check_winner(board):
   
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE):
            if board[row][col] == 0:
                continue
            
            current_color = board[row][col]
            for row_delta, col_delta in directions:
                
                prev_row, prev_col = row - row_delta, col - col_delta
                if 0 <= prev_row < BOARD_SIZE and 0 <= prev_col < BOARD_SIZE:
                    if board[prev_row][prev_col] == current_color:
                        continue
                
                count = 1
                curr_row, curr_col = row + row_delta, col + col_delta
                
                while 0 <= curr_row < BOARD_SIZE and 0 <= curr_col < BOARD_SIZE and \
                      board[curr_row][curr_col] == current_color:
                    count += 1
                    curr_row += row_delta
                    curr_col += col_delta
                
            
                if count == WIN_STREAK:
                    return current_color, (row + 1, col + 1)
                    
    return 0, None

def solve():

    try:
        with open('input.txt', 'r') as f:
            input_data = f.read().split()
    except FileNotFoundError:
        print("Помилка: Файл 'input.txt' не знайдено!")
        return

    if not input_data:
        return
    
    try:
        num_tests = int(input_data[0])
    except (ValueError, IndexError):
        print("Помилка: Перше значення у файлі має бути числом (кількість тестів).")
        return

    data_idx = 1
    for test_no in range(num_tests):
        try:
            board, data_idx = parse_board(input_data, data_idx)
            winner, win_pos = check_winner(board)
            
            print(winner)
            if winner != 0:
                print(f"{win_pos[0]} {win_pos[1]}")
        except ValueError as e:
            print(f"Тест {test_no + 1} пропущено через помилку: {e}")
        except IndexError:
            print(f"Помилка: Не вистачає даних для тесту {test_no + 1}.")
            break

if __name__ == "__main__":
    solve()
