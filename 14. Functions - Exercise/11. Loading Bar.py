load_percent = int(input())


def load_bar(n: int):
    if n == 100:
        return "100% Complete! \n[%%%%%%%%%%]"
    else:
        loaded = n // 10
        unloaded = 10 - loaded
        return f"{n}% " + "[" + (loaded * "%") + (unloaded * ".") + "] \nStill loading..."


print(load_bar(load_percent))
