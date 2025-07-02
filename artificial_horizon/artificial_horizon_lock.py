import Range
import mathutils

def artificial_horizon_lock():
    # Get the current controller and the Cube object
    cont = Range.logic.getCurrentController()
    cube = cont.owner
    
    # Look for the Ball-2 object parented to the Cube
    ball = cube.children.get("Ball-2")
    
    # Lock the Ball's orientation to prevent any rotation
    if ball:
        ball.worldOrientation = mathutils.Matrix.Identity(3)

# Run the artificial_horizon_lock function
artificial_horizon_lock()
