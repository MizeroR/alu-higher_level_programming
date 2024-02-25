#!/usr/bin/python3
count = len(argv)
if count == 0:
   print("0 arguments.".format(count -1))
elif count == 1:
    print("1 argument:".format(count -1))
else:
    print("{} arguments:".format(count -1))
for i in range(count):
    print("{}: {}".format(i + 1, argv[i + 1]))
