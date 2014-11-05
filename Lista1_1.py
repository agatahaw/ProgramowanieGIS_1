def fizzBuzz (n):
    for i in xrange(1,n+1):
        if i%5 == 0 and i%3 == 0:
            print "Fizz Buzz"
        elif i%5 == 0:
            print "Buzz"
        elif i%3 == 0:
            print "Fizz"
        else:
            print i

            
print fizzBuzz(19)