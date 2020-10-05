import heapq
import math
def kth_closest_points(points, k):
    h = []
    for point in points:
        x, y = point
        distance = math.sqrt(x**2 + y**2)
        heapq.heappush(h, [distance, [x, y]])

    output = []
    i = 0
    while i < k:
        distance, coordinates = heapq.heappop(h)
        output.append(coordinates)
        i += 1
    return output

print(kth_closest_points([[1,1],[2,2],[3,3]],2))
