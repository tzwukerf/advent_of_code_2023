
with open("input.txt", "r") as f:
    final_sum = 0;
    lines = f.readlines();
    for line in lines:
        for i, c in enumerate(line):
            if c.isdigit():
                final_sum += int(c) * 10
                break
        reverse = line[::-1]
        for i, c in enumerate(reverse):
            if c.isdigit():
                final_sum += int(c)
                break

    print(final_sum)
    f.close()






