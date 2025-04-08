import sys
import random

# ユーザーに最小値と最大値を入力してもらう
sys.stdout.buffer.write(b'Please enter two numbers min and max: \n')
sys.stdout.flush()
while True:
    try:
        # ユーザーからの入力を受け取る
        two_numbers = sys.stdin.buffer.readline().decode().strip()
        first, last = map(int, two_numbers.split())
        if first >= last:
            raise ValueError("The first number must be less than the second number.")
        break
    except ValueError:
        sys.stdout.buffer.write(b'Invalid input. Please enter two numbers min and max:\n')
        sys.stdout.flush()

# ユーザーに入力された範囲を表示
sys.stdout.buffer.write(f"Your entered range is {first} to {last}\n".encode())
sys.stdout.flush()

# ランダムな正解の数字を生成
correct_answer_num = random.randint(first, last)

# ユーザーが正解を推測するまで繰り返す
sys.stdout.buffer.write(b'Guess the number: \n')
sys.stdout.flush()
while True:
    try:
        enter_number = int(sys.stdin.buffer.readline().decode().strip())
        if enter_number < correct_answer_num:
            sys.stdout.buffer.write(b'Too low! Try again:\n')
        elif enter_number > correct_answer_num:
            sys.stdout.buffer.write(b'Too high! Try again:\n')
        else:
            sys.stdout.buffer.write(b'Correct! You guessed the number!\n')
            break
        sys.stdout.flush()
    except ValueError:
        sys.stdout.buffer.write(b'Invalid input. Please enter an integer:\n')
        sys.stdout.flush()


