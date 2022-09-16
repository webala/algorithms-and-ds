def countingValleys(steps, path):
    # Write your code here
    step_vector = valleys = 0

    for step in path:
        if step == "U":
            step_vector += 1
        elif step == "D":
            step_vector -= 1

        if step == "U" and step_vector == 0:
            valleys += 1

    return valleys


print(countingValleys(12, "DDUUDDUDUUUD"))
