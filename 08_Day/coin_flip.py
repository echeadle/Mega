percent_heads = 0.0
num_heads = 0
num_tosses = 0
num_tails = 0
game_over = False
while not game_over:
    user_input = input("Throw the coin and enter head or tail here or exit to exit: ? ")
    with open("files/coin_toss.txt", 'r') as file:
        old_file = file.readlines()

    if user_input != 'exit':
        with open("files/coin_toss.txt", 'w') as file:
            file.writelines(old_file)
            file.write(user_input + "\n")

    num_tosses += 1
    match user_input:
        case  "head":
            num_heads += 1
        case 'tail':
            num_tails += 1
        case 'exit':
            break
    if num_heads != 0:
        percent_heads = (num_heads / num_tosses) * 100
        print(f"Heads: {num_heads}, Percent {round(percent_heads)}% Tails: {num_tails} Tosses {num_tosses} ")

