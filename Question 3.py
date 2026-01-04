"""
ASSIGNMENT 2
GROUP NAME: DAN/EXT 22
GROUP MEMBER:
Nguyen Duy Quang Lai        -   s389980
Angel Chang                 -   s377501
Nicole Suzanne Sattler      -   s195029
Youssef Elkassaby           -   s392402
============================================================================
Question 3 Requirement:
- Draw a recursive geometric pattern using Python turtle graphics.
- Start with a regular polygon defined by user input.
- Each edge is recursively divided into four segments by replacing the
  middle third with an inward equilateral triangle indentation.
- Recursion depth controls how many times the pattern is applied.
"""

import turtle


def draw_recursive_edge(length, depth):
    """
    Recursively draws one edge with an inward indentation.
    Depth 0 draws a straight line; otherwise the edge is split into
    four segments of length/3 with an inward triangular notch.
    """
    if depth == 0:
        turtle.forward(length)
        return

    segment = length / 3.0

    # 1st third
    draw_recursive_edge(segment, depth - 1)

    # Indentation (triangle pointing inward)
    turtle.right(60)
    draw_recursive_edge(segment, depth - 1)

    turtle.left(120)
    draw_recursive_edge(segment, depth - 1)

    turtle.right(60)
    draw_recursive_edge(segment, depth - 1)


def draw_polygon(sides, side_length, depth):
    """
    Draws a regular polygon where each side is drawn recursively.
    The polygon is drawn clockwise so the indentation points inward.
    """
    exterior_angle = 360.0 / sides

    for _ in range(sides):
        draw_recursive_edge(side_length, depth)
        turtle.right(exterior_angle)  # clockwise


def get_int(prompt):
    """Read an integer from input (simple validation)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def get_float(prompt):
    """Read a float from input (simple validation)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Recursive Turtle Pattern (Question 3)")
    sides = get_int("Enter the number of sides: ")
    side_length = get_float("Enter the side length: ")
    depth = get_int("Enter the recursion depth: ")

    # Basic parameter checks
    if sides < 3:
        print("Number of sides must be at least 3.")
        return
    if side_length <= 0:
        print("Side length must be greater than 0.")
        return
    if depth < 0:
        print("Recursion depth must be 0 or greater.")
        return

    # Turtle setup
    turtle.title("Question 3 - Recursive Pattern")
    turtle.setup(width=900, height=700)

    turtle.speed(0)
    turtle.hideturtle()

    # Faster drawing for higher depths
    turtle.tracer(0, 0)

    # Move to a nicer start position (roughly center the drawing)
    turtle.penup()
    turtle.goto(-side_length / 2.0, side_length / 3.0)
    turtle.pendown()

    draw_polygon(sides, side_length, depth)

    turtle.update()
    turtle.done()


if __name__ == "__main__":
    main()
