number_of_snowballs = int(input())
high_weight = high_time = high_quality = highest_value = 0

for snowball_counter in range(1, number_of_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_value = (weight / time) ** quality
    if current_value > highest_value:
        high_weight = weight
        high_time = time
        high_quality = quality
        highest_value = current_value
    current_value = 0

print(f"{high_weight} : {high_time} = {highest_value:.0f} ({high_quality})")
