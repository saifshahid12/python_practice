
    # write a programe to find which line is python present in question 6

with open("log.txt") as f:
    lines=f.readlines()


lineno = 1
for line in lines:
    if ("python" in line):
        print(f"yes:{lineno}")
        break
    lineno += 1

else:
      print("no")