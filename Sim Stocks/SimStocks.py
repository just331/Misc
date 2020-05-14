# Python program to simulate trades under various conditions


import numpy as np
import matplotlib.pyplot as plt


def simulate(account_size, total_trade, risk_per_trade, win_rate, risk_reward):
    account = account_size
    accounts = [account]
    profits = []
    loss = []
    wins = []
    total_win = 0
    max_con_1 = 0
    max_con_w = 0
    con_1 = 0
    con_w = 0
    pre = 0
    rnd = list(np.round(np.random.uniform(1, 101, total_trade), 2))
    for i in range(len(rnd)):
        r = rnd[i]
        win = r <= win_rate
        risk = -np.round(account * risk_per_trade / 100, 2)
        profit_per_trade = abs(risk) * risk_reward
        profit = profit_per_trade if win else risk
        profits.append(profit)
        account += profit
        accounts.append(account)
        if profit > 0:
            total_win += 1
            wins.append(profit)
            con_1 = 0
            if pre == 1:
                con_w += 1
                if con_w > max_con_w:
                    max_con_w = con_w
            pre = 1
        else:
            loss.append(abs(profit))
            con_w = 0
            if pre == -1:
                con_1 += 1
                if con_1 > max_con_1:
                    max_con_1 = con_1
            pre = -1
    avg_win = np.mean(wins)
    avg_loss = np.mean(loss)
    max_win = np.max(wins)
    max_loss = np.max(loss)
    win_r = np.round(total_win / total_trade * 100, 2)
    rrr = np.round(avg_win / avg_loss, 2)
    profit_factor = np.round(np.sum(wins) / np.sum(loss), 2)
    net_profits = np.cumsum(profits)
    gain = np.round(accounts[-1] - account_size, 2)
    growth_rate = np.round((accounts[-1] - account_size) / account_size * 100, 2)
    print("--- Trading Results ---\n")
    print("Total Trades         : {}".format(total_trade))
    print("Wins                 : {} / {}%".format(total_win, win_r))
    print("Average Wins         : {}".format(np.round(avg_win, 2)))
    print("Average Loss         : {}".format(np.round(avg_loss, 2)))
    print("Max Win              : {}".format(np.round(max_win, 2)))
    print("Max Loss             : {}".format(np.round(max_loss, 2)))
    print("Max Cons. Wins       : {}".format(max_con_w))
    print("Max Cons. Loss       : {}".format(max_con_1))
    print("Risk Reward Ratio    : {}".format(rrr))
    print("Profit Factor        : {}".format(profit_factor))
    print("Risk per trade       : {}%".format(risk_per_trade))
    print("---")
    print("Initial Account      : {}".format(account_size))
    print("Profit               : {} / {}%".format(gain, growth_rate))
    print("Final Account        : {}".format(np.round(account, 2)))
    print()
    print("Results are compounded. Spread and commissions are not calculated.")
    fig, ax = plt.subplots(2, 1, figsize=(16, 10))
    ax[0].plot(net_profits)
    ax[1].plot(accounts)
    ax[1].axhline(account_size, color="#000000", ls="-.", linewidth=0.5)
    ax[0].set_title("Equirty Curve")
    ax[1].set_title("Account Growth")
    plt.show()


def main():
    account_size = 10000
    total_trades = 200
    risk_per_trade = 2
    win_rate = 70
    risk_reward = 2
    simulate(account_size, total_trades, risk_per_trade, win_rate, risk_reward)


main()
