import Range

def main():
    # Get the object whose speed we want to measure
    obj = Range.logic.getCurrentController().owner

    # Calculate the object's speed in meters per second (m/s)
    speed_ms = obj.worldLinearVelocity.magnitude

    # Convert speed to kilometers per hour (km/h)
    speed_kmh = speed_ms * 3.6

    # Convert to integer (no decimals)
    speed_kmh_int = int(speed_kmh)

    # Format the speed text
    speed_text = f"{speed_kmh_int} km/h"

    # Get the text object from the scene
    scene = Range.logic.getCurrentScene()
    text_obj = scene.objects["SpeedTextKmh"]  # Replace with your text object's name if different

    # Update the text with the calculated speed
    text_obj.text = speed_text

# Run the function
main()
