
# A global variable total_visitors = 0.
# A function add_visitors(count) that takes an integer and 
# returns total_visitors + count — 
# it should not modify the global variable directly, and should not use the global keyword.
# Outside the function, call add_visitors(5) and add_visitors(10) separately, 
# each time unpacking-style assigning the result to a new variable and printing it.
# Finally, print total_visitors one more time, 
# to confirm the global variable itself was never changed by either call.

total_visitors = 0
def add_visitors(count):
    # total_visitors = total_visitors + count
    return count + total_visitors

res1= add_visitors(5)
res2 =add_visitors(10)
print(res1)
print(res2)
print(total_visitors)