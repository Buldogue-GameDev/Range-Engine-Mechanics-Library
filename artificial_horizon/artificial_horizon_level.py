import Range
import mathutils

def artificial_horizon_level():
    # Get the current controller and the Cube object
    cont = Range.logic.getCurrentController()
    cube = cont.owner
    
    # Get the Ball-1 object parented to the Cube
    ball = cube.children.get("Ball-1")
    
    # Level the Ball so it stays aligned with the global horizon (no tilt)
    if ball:
        euler = cube.worldOrientation.to_euler()
        ball.worldOrientation = mathutils.Euler((0, 0, euler.z), 'XYZ').to_matrix()

# Run the artificial_horizon_level function
artificial_horizon_level()
