old_version = input().split(".")
old_version = "".join(old_version)
old_version = int(old_version)
old_version += 1
old_version = str(old_version)
print(f"{old_version[0]}.{old_version[1]}.{old_version[2]}")
