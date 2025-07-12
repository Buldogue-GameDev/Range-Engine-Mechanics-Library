import Range

def main():
    # Get the object whose speed we want to measure
    obj = Range.logic.getCurrentController().owner

    # Calculate the object's speed in meters per second (m/s)
    speed_ms = obj.worldLinearVelocity.magnitude

    # Format the speed value with 2 decimal places
    speed_text = f"Speed: {speed_ms:.2f} m/s"

    # Get the text object from the scene (named "SpeedTextMS")
    scene = Range.logic.getCurrentScene()
    text_obj = scene.objects["SpeedTextMS"]  # Replace with your actual text object name if different

    # Update the text with the calculated speed in m/s
    text_obj.text = speed_text

# Run the function
main()
