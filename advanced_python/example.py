# errors and exception handling

try:
    print(10+10)
except TypeError:
    print(" TypeError: You are using the wrong data types!")
except IOError:
    print("You have an input output error")
else:
    print("else block ran if n error")
finally:
    print("this always runs")
