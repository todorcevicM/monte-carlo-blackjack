import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import Table

if np.get_printoptions()['linewidth']: 
    np.set_printoptions(linewidth=160)

hit_win = np.full((10, 18), 1)
hit_play = np.full((10, 18), 1)
check_win = np.full((10, 18), 1)
check_play = np.full((10, 18), 1)

def simulate(iterations = 1000000):

    for _ in range(iterations):
        play = True
        table = Table.Table()
        x = table.dealer_sum - 2
        y = table.hand_sum - 4

        while play:
            if check_win[x, y] / check_play[x, y] > np.random.normal(0.5, 0.05):
                table.check()
            else: 
                table.hit()

            if (table.hand_sum > 21 or table.dealer_sum >= 17):
                play = False
                break
            
            y = table.hand_sum - 4

        if table.hand_sum == table.dealer_sum:
            pass
        elif table.hand_sum > 21: 
            hit_play[x, y] += 1
        elif (table.dealer_sum > 21 or table.dealer_sum < table.hand_sum):
            check_win[x, y] += 1
            check_play[x, y] += 1
        else:
            check_play[x, y] += 1

    print("Hit_Win matrix:")
    print(hit_win)
    print("\n")
    print("Hit_Play matrix:")
    print(hit_play)
    print("\n")
    print("Check_Win matrix:")
    print(check_win)
    print("\n")
    print("Check_Play matrix:")
    print(check_play)
    print("\n")


    print((hit_win / hit_play - check_win / check_play).round(2))
    print("\n")
    print("Win percentage when checking: ")
    print((check_win / check_play).round(2))

    df = pd.DataFrame((check_win / check_play).round(2), range(2, 12), range(4, 22))
    sns.heatmap(df)
    plt.show()
    df1 = df.ge(0.5).astype(int)
    print(df1)
    sns.heatmap(df1)
    plt.show()


simulate()