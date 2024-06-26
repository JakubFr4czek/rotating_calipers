# Rotating calipers module

Rotating calipers is python module implementing an algorithm with the same name.

## Rotating calipers algorithm

Algorithm was first invented by Michalel Shamos in 1978 and gained its name "rotating calipers"
thanks to Godfried Toussant who featured it in his paper in 1983.

The method is so named because the idea is analogous to rotating a spring-loaded vernier caliper around the outside of a convex polygon.
Every time one blade of the caliper lies flat against an edge of the polygon, it forms an antipodal pair with the point or edge touching
the opposite blade. The complete "rotation" of the caliper around the polygon detects all antipodal pairs; the set of all pairs, viewed
as a graph, forms a thrackle. The method of rotating calipers can be interpreted as the projective dual of a sweep line algorithm in which
the sweep is across slopes of lines rather than across x- or y-coordinates of points.

Above description was adapted from wikipedia page: https://en.wikipedia.org/wiki/Rotating_calipers

## Motivation

The "rotating calipers" algorithm was implemented by me for a university project. Suprisingly I went through a lot of trouble finding an efficient
solution in python. That is why I wanted to share it with everyone who needs fast "rotating calipers" implementation in python.

## Complexity

As rotating calipers runs in linear time it needs a convex hull on input wihch is calculated here using Graham's algorithm which runs in O(nlogn).
All in all algorihm's (Graham's algorithm + rotating calipers) time complexity is O(nlogn) + O(n) = O(nlogn)

## How to install

Linux:

1) Open terminal
2) Run: pip install rotating-calipers

## How to use

Example of use can be found [here](https://github.com/JakubFr4czek/rotating_calipers/tree/main/examples)
