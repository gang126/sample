

def add(x):
    for i in range(0,10):
        yield i+x

y=add(3)

print y.next()
print "--------------"

for y1 in y:
    print y1        