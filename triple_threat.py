
"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Evan Schmidt - November 2024
"""

import random

def main() -> None:

    cost: int = 1
    prize: int = 10
    profit: int = 0
    totalout: int = 0
    totalin: int = 0 
    totalprofit: int = 0
    gamesplayed: int = random.randint(1000,5000)
	
    for _ in range(gamesplayed):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)

        if d1 == d2 and d2 == d3 and d3 == d1:
            prize = 10 * d1
        else:
            prize = 0
        
        if d1 == 6 and d2 == 6 and d3 == 6:
            prize = d1 * 10

        totalout += prize
        totalin += cost
        profit = cost - prize
        totalprofit += profit
        """
        print(f"Casino collects: ${cost}")
        print(f"Player rolls: {d1}-{d2}-{d3}")
        print(f"Casino pays out: ${prize}")
        print(f"Profit: ${profit}")
        """
    print("Games Played, Total Collected, Total Paid Out, Total Profit")
    print(f"{gamesplayed}, {totalin}, {totalout}, {totalprofit}")


if __name__ == "__main__":
    main()
