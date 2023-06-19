waiting_people = int(input())
lifts = list(map(int, input().split(" ")))
free_slots = 0
for lift_num in range(len(lifts)):
    if lifts[lift_num] == 4:
        continue
    else:
        free_slots = 4 - lifts[lift_num]
        if free_slots <= waiting_people:
            waiting_people -= free_slots
            lifts[lift_num] += free_slots
            if waiting_people == 0:
                break
        else:
            lifts[lift_num] += waiting_people
            waiting_people = 0
            break

empty_lift = False
for lift in lifts:
    if lift == 4:
        continue
    else:
        empty_lift = True
        break
lifts = [str(lift) for lift in lifts]

if waiting_people == 0 and empty_lift:
    print("The lift has empty spots!")
    print(" ".join(lifts))
elif waiting_people > 0 and not empty_lift:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(" ".join(lifts))
elif waiting_people == 0 and not empty_lift:
    print(" ".join(lifts))