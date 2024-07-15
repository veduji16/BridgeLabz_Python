import random

def simulate_gambler(stake, goal, num_times):
    total_wins = 0
    total_bets = 0

    for _ in range(num_times):
        current_stake = stake
        bets = 0

        while 0 < current_stake < goal:
            bets += 1
            if random.random() < 0.5:
                current_stake += 1
            else:
                current_stake -= 1

        if current_stake == goal:
            total_wins += 1

        total_bets += bets

    avg_wins = total_wins / num_times
    avg_bets = total_bets / num_times

    return avg_wins, avg_bets

stake = int(input("Enter the initial stake ($): "))
goal = int(input("Enter the goal ($): "))
num_times = int(input("Enter the number of times to run the experiment: "))

avg_wins, avg_bets = simulate_gambler(stake, goal, num_times)

print(f"Average number of wins: {avg_wins:.2f}")
print(f"Average number of bets: {avg_bets:.2f}")
print(f"Percentage of wins: {avg_wins / num_times * 100:.2f}%")
print(f"Percentage of losses: {(1 - avg_wins / num_times) * 100:.2f}%")