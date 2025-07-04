import Range
import math
import mathutils

def laser_rangefinder(self):
    """
    Measures the aircraft's altitude using a raycast on the negative Z axis
    and updates the altitude display and needle rotation.
    """
    # Configuration
    MAX_DISTANCE = 10000      # Maximum laser distance (meters)
    ROTATION_SCALE = 1000     # One full rotation per 1000 meters
    LASER_COLOR = [0, 1, 0]   # Laser color (green)
    ALTITUDE_FORMAT = "{:04d}" # Altitude text format (4 digits, zero-padded)

    # Raycast setup
    position_start = self.owner.worldPosition
    direction = self.owner.worldOrientation.col[2] * -MAX_DISTANCE
    position_end = position_start + direction

    # Perform raycast
    hit_object, hit_point, _ = self.owner.rayCast(position_end, position_start, MAX_DISTANCE)

    # Altitude display and needle update
    text_obj = self.owner.scene.objects["AltitudeDisplay"]
    needle_obj = self.owner.scene.objects["AltitudeNeedle"]

    if hit_object:
        altitude = int((hit_point - position_start).length)
        formatted_altitude = ALTITUDE_FORMAT.format(altitude)

        # Draw laser line
        Range.render.drawLine(position_start, hit_point, LASER_COLOR)

        # Update text
        text_obj.text = f"Altitude: {formatted_altitude}"

        # Update needle rotation
        angle = -math.radians((altitude / ROTATION_SCALE) * 360)
        needle_obj.worldOrientation = mathutils.Euler((0, 0, angle), 'XYZ').to_matrix()

    else:
        text_obj.text = "Altitude: ----"
        needle_obj.worldOrientation = mathutils.Euler((0, 0, 0), 'XYZ').to_matrix()
