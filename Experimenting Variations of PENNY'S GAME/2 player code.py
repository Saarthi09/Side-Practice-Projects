import random

def game(seq1, seq2):
    outcomes = ['H', 'T']
    series = []
    count = 0

    while True: 
        toss = random.choice(outcomes)
        series.append(toss)
        count += 1

        if len(series) >= 3:
            last_three = ''.join(series[-3:])
            if last_three == seq1: 
                return "Player 1", count, series
            elif last_three == seq2:
                return "Player 2", count, series
            

player1 = input("Enter a 3 toss sequence (eg: HTT/TTH/HTH): ").upper()
player2 = input("Enter a 3 toss sequence (eg: HTT/TTH/HTH): ").upper()

if player1 == player2:
    print("Choose different sequence")

else: 
    winner, tosses, series = game(player1, player2)
    print(f"\n {winner} Wins!")
    print(f"Total tosses: {tosses}")
    print(f"Player 1 sequence: {player1}")
    print(f"Player 2 sequence: {player2}")
    print("Toss history:", ' '.join(series))
