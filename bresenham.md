# Bresenham Line Drawing Algorithm

This algorithm is used to draw a line between two points on a grid. This is very optimized for the following reasons:
- It does not do floating point operation
- it does not do division or multiplication
- it do not round the values

### I wrote 2 algorithmic functions nammed:
- `bresenhams_line` (for `0 < slope  < 1`)
- `bresenhams_line_updated` (for all all slopes)

`bresenhams_line` failes for `slope > 1` because that algorithm will work for `0 < slope < 1` as it goes through x - axis and in slope < 1 the **x - axis** is dominent and we increase x axis by 1 in each increment.

## Adjustments for m > 1

`bresenhams_line_updated` will also work for `slope > 1` as it will goes through x - axis or y- axis depending on which one is more dominent. For example: for slope < 1 the **x - axis** is dominent and we increase x axis by 1 in each increment and for slope > 1 the **y - axis** is dominent and we increase y axis by 1 in each increment.

fixes For `slope > 1`:
- we can swap the `(x1, y1) with (y1, x1)` and `(x2, y2) with (y2, x2)`
- which will make the slope in the range `0 < slope < 1` 
- then we can use the above algorithm to get the points. 
- lastly we can reswap (x,y) with (y,x) to get the proper result.
