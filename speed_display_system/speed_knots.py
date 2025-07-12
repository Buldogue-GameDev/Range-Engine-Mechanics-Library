import Range

def main():
    # Get the object whose speed we want to measure
    obj = Range.logic.getCurrentController().owner

    # Calculate the object's speed in meters per second (m/s)
    speed_ms = obj.worldLinearVelocity.magnitude

    # Convert speed to knots
    speed_knots = speed_ms * 1.943844

    # Convert to integer (remove decimals)
    speed_knots_int = int(speed_knots)

    # Format the speed text
    speed_text = f"Speed: {speed_knots_int} knots"

    # Get the text object from the scene
    scene = Range.logic.getCurrentScene()
    text_obj = scene.objects["SpeedTextKnots"]  # Replace with your text object's name if needed

    # Update the text with the calculated speed
    text_obj.text = speed_text

# Run the function
main()
