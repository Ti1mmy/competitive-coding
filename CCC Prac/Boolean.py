a = input()
a = a.split()
if len(a) == 1:
    print(a[0])
else:
    if a.count("not") % 2 == 0:
        print(a[-1])
    else:
        if a[-1] == "False":
            print("True")
        else:
            print("False")