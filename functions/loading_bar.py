def bar_percents(num_of_percents):
    bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    if num_of_percents != 100:
        for n in range(int(num_of_percents/10)):
            bar[n] = "%"
        bar = "".join(bar)
        bar = f"[{bar}]"
        return f"{num_of_percents}% {bar}\nStill loading..."
    else:
        return f"100% Complete!\n[%%%%%%%%%%]"

num_of_percents = int(input())
print(bar_percents(num_of_percents))
