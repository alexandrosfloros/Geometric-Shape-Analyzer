# Motivation

This project was originally made with the intention of challenging myself by attempting to solve a problem that, while easy to understand by one's intuition, it would require a lot of thought and effort to interpret using a computer algorithm. I came up with the idea of analysing points to obtain geometric shapes as a result of my interest surrounding such problems as well as the mathematical theory behind them. The project started out as a script with very basic features but, after a few revisions, it was expanded to a user-friendly application with multiple functionalities, accepting a variety of user inputs.

# Features

Main Features:

* Analysing input co-ordinates manually inserted
* Analysing input points drawn on the plane
* Analysing random co-ordinates
* Identifying 8 different geometric shapes

Shapes Supported:

* Parallelograms
* Rectangles
* Rhombi
* Squares
* Isosceles Trapezia
* Cyclic Quadrilaterals
* Right Triangles
* Isosceles Triangles

Other Features:

* Flexible adding and removal of points
* Robust to problematic inputs

# How to Use

## Execution

The file used to run the project is ``main.py``.

## Adding Points

Points can be manually added by inserting their co-ordinates and clicking on the "Add" button. Alternatively, random points may be added by clicking on the "Random" button and specifying their number. Once points are added on the plane, their co-ordinates appear on a table and a plot starts to display their position. Points can also be added by clicking on the grid, assuming that there is not a point already there. If the user clicks on an existing point, it is removed. Points may also be removed by clicking on the "Remove" button, which deletes any point with the specified co-ordinates. The entire list can be cleared by clicking on the "Clear" button.

## Generating Shapes

Once at least three points have been added, the "Find Shapes" button can be clicked to generate a list of all the shapes identified on the plane, if any. By clicking on any shape type on the list, the vertex co-ordinates of each shape are shown, which, when selected, are highlighted on the plot. For cyclic quadrilaterals, the circumcentre and circumcircle also become visible. Whenever new points are added or removed, the shape list is reset and the user is asked to update it by clicking on the "Find Shapes" button again.
