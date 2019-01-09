def function_to_call(x):
    numbers = []
    i = 0
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

#You can put whatever number you want as x really.
function_to_call(8)

