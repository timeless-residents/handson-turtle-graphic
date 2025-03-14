import turtle
import os

# Print the current working directory
print("Current working directory:", os.getcwd())

# Print the help for register_shape
print("\nHelp for register_shape:")
print(turtle.register_shape.__doc__)

# Try to register a shape with a GIF file (which is known to work with turtle)
try:
    # Create a simple turtle screen
    screen = turtle.Screen()

    # Get the absolute path to the image
    turtle_image = "/Users/studio/work/github/handson-turtle-graphic/turtle.png"
    print("\nTrying to register shape with:", turtle_image)
    print("File exists:", os.path.exists(turtle_image))

    # Try different approaches
    print("\nApproach 1: Using Screen.register_shape")
    screen.register_shape(turtle_image)
    print("Success!")

    print("\nApproach 2: Using turtle.register_shape")
    turtle.register_shape(turtle_image)
    print("Success!")

except Exception as e:
    print("Error:", e)

# Keep the window open
turtle.done()
