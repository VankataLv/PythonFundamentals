def inc_dec(lst: list, value: int) -> list:
    changed_lst = []
    for el in lst:
        if el <= value:
            el += value
        else:
            el -= value
        changed_lst.append(el)
    return changed_lst


distances = [int(el) for el in input().split(" ")]
sum_pokemon = 0
while len(distances) > 0:
    index = int(input())
    if index < 0:
        removed_el = distances.pop(0)
        distances.insert(0, distances[-1])
    elif index > len(distances) - 1:
        removed_el = distances.pop()
        distances.append(removed_el)
    else:
        removed_el = distances.pop(index)
    distances = inc_dec(distances, removed_el)
    sum_pokemon += removed_el
    removed_el = 0
print(sum_pokemon)
