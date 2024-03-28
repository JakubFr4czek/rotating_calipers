import rotating_calipers as rc

# List of random points in form of (x, y)
Points = [(46.329418732694535, 67.31122022140417), (-27.361642198143272, 16.474320352552454), (-50.6131275129792, -67.09710610031078),
           (-31.9541609545835, -91.79358536721058), (-84.88249979057576, -89.6916456892084), (-38.587003398727894, 67.50995327921422),
           (77.03006536793899, 8.818852446564193), (86.74486674618328, 47.391081357087245), (77.93256557274128, -72.98399866280025)]

# Smallest_rectangle takes as an input:
#  - list of points
#  - function which output will be minimised
#
# Compare_perimeter is a function shipped with rotating_calipers module
# it simply calculates rectangle perimiter based on two rectangle edges
#
# Output of a function is a tuple (a, b) where:
#  - a is a minimal value returned by the compare function (here compare_perimeter)
#  - b is a list of desired rectangle vertices in form of (x, y)
result, vertices = rc.smallest_rectangle(Points, rc.compare_perimeter)

print("Minimal rectangle perimiter: ",result)
print("Rectangle vertices: ", vertices)

