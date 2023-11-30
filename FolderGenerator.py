import os

for i in range(1, 26):
    os.makedirs("Day_" + str(i))
    for file in ["data.txt", "P1.py", "P2.py", "test.txt"]:
        os.popen(f'copy {file} "Day_{i}/{file}')