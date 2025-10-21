    # write a programe to read a text from given file poem.txt and find out whether it contain the word twinkle

f = open("1_related_problem1.py")
content=f.read()

if("twinkle in content"):
    print("twinkle is present in content:")

else:
    print("twinkle is not present")

f.close()