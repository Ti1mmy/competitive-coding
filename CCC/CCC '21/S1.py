from sys import stdin, stdout

n = int(stdin.readline())
height_measurements = [int(num) for num in stdin.readline().split(" ")]
width_measurements = [int(num) for num in stdin.readline().split(" ")]


def fence_area(heights, widths):
    area = 0
    for i in range(n):
        if heights[i] > heights[i+1]:
            area += heights[i+1] * widths[i]
            area += ((heights[i] - heights[i+1]) * widths[i] / 2)
        else:
            area += heights[i] * widths[i]
            area += ((heights[i+1] - heights[i]) * widths[i] / 2)
    return area


stdout.write(str(fence_area(height_measurements, width_measurements)))