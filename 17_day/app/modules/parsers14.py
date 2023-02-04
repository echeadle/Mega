def parse(feet_inches):
    """ Parse feet_inches and return feet and inches separately."""
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
