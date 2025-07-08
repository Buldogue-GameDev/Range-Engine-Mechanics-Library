import Range
import math
import mathutils

def main():
    # Script configuration
    fixed_angle_deg = 90                # Fixed angle for the fixed needle (degrees)
    show_text = True                    # Toggle for displaying text on screen
    target_property = 'target_property' # Name of the required object property
    reference_name = 'ReferenceObject'  # Name of the reference object
    compass_needle_name = 'CompassNeedle'  # Name of the compass needle
    fixed_needle_name = 'FixedNeedle'      # Name of the fixed needle
    target_needle_name = 'TargetNeedle'    # Name of the needle pointing to nearest object
    compass_text_name = 'CompassText'      # Name of the text object

    # Get controller and scene
    controller = Range.logic.getCurrentController()
    scene = controller.owner.scene

    # Retrieve required objects
    reference_obj = scene.objects.get(reference_name)
    compass_needle = scene.objects.get(compass_needle_name)
    fixed_needle = scene.objects.get(fixed_needle_name)
    target_needle = scene.objects.get(target_needle_name)
    compass_text = scene.objects.get(compass_text_name)

    # Validate object existence
    if not all([reference_obj, compass_needle, fixed_needle, target_needle, compass_text]):
        print("Error: One or more required objects were not found in the scene.")
        return

    # Get reference object rotation on Z axis (radians)
    reference_rotation_z = reference_obj.worldOrientation.to_euler().z

    # Convert to degrees and normalize to [0, 360]
    compass_angle = (math.degrees(reference_rotation_z) % 360)

    # Update text display if enabled
    if show_text:
        compass_text.text = f"Angle: {compass_angle:.2f}°"

    # Set compass needle rotation
    compass_rot = mathutils.Euler((0, 0, reference_rotation_z), 'XYZ')
    compass_needle.worldOrientation = compass_rot.to_matrix()

    # Set fixed needle rotation
    fixed_angle_rad = math.radians(fixed_angle_deg)
    fixed_rot = mathutils.Euler((0, 0, fixed_angle_rad), 'XYZ')
    fixed_needle.worldOrientation = fixed_rot.to_matrix()

    # Find nearest object with the target property
    nearest_obj = None
    shortest_distance = float('inf')

    for obj in scene.objects:
        if target_property in obj:
            distance = (obj.worldPosition - reference_obj.worldPosition).length
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_obj = obj

    # Update target needle to point at nearest object if found
    if nearest_obj:
        direction = nearest_obj.worldPosition - reference_obj.worldPosition
        angle_to_target = math.atan2(direction.y, direction.x)
        angle_to_target -= math.pi / 2  # Adjust to align with compass convention

        target_rot = mathutils.Euler((0, 0, angle_to_target), 'XYZ')
        target_needle.worldOrientation = target_rot.to_matrix()

# Run main function
main()
