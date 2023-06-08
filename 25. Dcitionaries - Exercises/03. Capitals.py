countries = input().split(", ")
capitals = input().split(", ")

atlas = {key: value for key, value in zip(countries, capitals)}
for key, value in atlas.items():
    print(f"{key} -> {value}")