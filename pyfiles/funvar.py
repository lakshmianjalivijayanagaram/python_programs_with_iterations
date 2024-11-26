def out_display():
    a=10
    def in_display():
        nonlocal a
        print(a)
        a=a-4
    in_display()
    print(a)
out_display()

'''
a=10
def display():
    global a
    print(a)
    a=a-2
print(a)
display()
print(a)


def display():
    a=10
    print(a)
    a=a-4
    print(a)
display()
'''
