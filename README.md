# Features

Main Features:

* Analyzing input coordinates inserted manually
* Analyzing input points drawn on the plane
* Analyzing random coordinates
* Identifying 8 different geometric shapes

Shapes Supported:

* Parallelograms
* Rectangles
* Rhombi
* Squares
* Isosceles Trapezoids
* Cyclic Quadrilaterals
* Right Triangles
* Isosceles Triangles

# How to Use

## Execution

The file used to run the project is ``main.py``.

## Adding Points

Points can be added by inserting their coordinates manually and clicking on the "Add" button. Alternatively, a number of random points may be added by clicking on the "Random" button and specifying their count. Once points are added on the plane, their coordinates appear on a table, and a plot starts to display their position. Points can also be added by placing them on the grid, assuming that there is not a point already there. Existing points are removed by clicking on them. They may also be removed with the "Remove" button, which deletes any point with specified coordinates. The entire list can be cleared by clicking on the "Clear" button.

## Generating Shapes

Once at least three points have been added, the "Find Shapes" button can be clicked to generate a list of all the shapes identified on the plane. By clicking on any shape type on the list, the vertex coordinates of each shape are shown, which, when selected, are highlighted on the plot. For cyclic quadrilaterals, the circumcenter and circumcircle also become visible. Whenever new points are added or removed, the shape list is reset, and the user is asked to update it by clicking on the "Find Shapes" button again.
