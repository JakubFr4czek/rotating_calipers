import rotating_calipers as rc

# Custom compare function must take two parameters
# which are two different edges of a rectangle and
# return one value which will be minimised by
# smallest_rectangle function
def custom_function(a, b):

    return abs(a - b)

# List of random points in form of (x, y)
Points = [(46.329418732694535, 67.31122022140417), (-27.361642198143272, 16.474320352552454), (-50.6131275129792, -67.09710610031078),
           (-31.9541609545835, -91.79358536721058), (-84.88249979057576, -89.6916456892084), (-38.587003398727894, 67.50995327921422),
           (77.03006536793899, 8.818852446564193), (86.74486674618328, 47.391081357087245), (77.93256557274128, -72.98399866280025)]

# Smallest_rectangle takes as an input:
#  - list of points
#  - function which output will be minimised
#
# In this case custom function declared above in passed
#
# Output of a function is a tuple (a, b) where:
#  - a is a minimal value returned by the compare function (here compare_perimeter)
#  - b is a list of desired rectangle vertices in form of (x, y)
result, vertices = rc.smallest_rectangle(Points, custom_function)

print("Minimal rectangle perimiter: ",result)
print("Rectangle vertices: ", vertices)

