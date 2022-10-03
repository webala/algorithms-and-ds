import math
'''
Here are the squares between 1 and 16:

1, 4, 9, 16

or

1^2, 2^2, 3^2, 4^2

The list is just an index value (i) to the power of 2 so: i^2.

So if we take the square root of a and b, round them up and down respectively, we're left with a start and end index.

And the formula for finding the number of elements in a list is simply:

end - start + 1

So if we go back to our original list:

1, 4, 9, 16

or

1^2, 2^2, 3^2, 4^2

OR

[1-4]

4 - 1 = 3

and then add 1 to account for the one we started with.

So in the end we have: 4 - 1 + 1 = 4

There are 4 squares between 1 and 16 (inclusive).
'''
def squares(a, b):
    x = math.ceil(math.sqrt(a))
    y = math.floor(math.sqrt(b))
    return y - x + 1