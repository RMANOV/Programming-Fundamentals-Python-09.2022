

initial_version = input().split(".")
initial_version = [int(x) for x in initial_version]

initial_version[2] += 1

if initial_version[2] > 9:
    initial_version[2] = 0
    initial_version[1] += 1
    if initial_version[1] > 9:
        initial_version[1] = 0
        initial_version[0] += 1
print(".".join([str(x) for x in initial_version]))