import subprocess

# Path to your Java application
java_app_path = "YourJavaApp.jar"

# Define the expected inputs and outputs
inputs = ["Pizza\n", "Uno\n", "42\n"]
expected_outputs = [
    "Please enter a number: Error: Please enter a whole number.\n",
    "Please enter a number: Error: Please enter a whole number.\n",
    "Please enter a number: num1 = 42.\nnum2 = 1042.\nnum3 = 84.\n"
]

# Run the Java application
process = subprocess.Popen(['java', '-jar', java_app_path],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           text=True)

# Send the inputs and check the outputs
for input_str, expected_output in zip(inputs, expected_outputs):
    process.stdin.write(input_str)
    process.stdin.flush()
    output = process.stdout.readline()
    error_line = process.stdout.readline()
    output += error_line if "Error" in error_line else ""
    try:
        assert output == expected_output
    except AssertionError:
        print("Please! Make sure that your program output matched the example output")
        print("Example output:")
        print(expected_output)
        print("Actual output:")
        print(output)
        exit(1)

print("Test passed!")
