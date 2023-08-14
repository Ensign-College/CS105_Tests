import os
import subprocess

def run_job(cmd, inputs):
    try:
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        # Write all inputs at once
        process_input = "\n".join(inputs) + "\n"
        stdout_data, _ = process.communicate(input=process_input)

        return stdout_data

    except BrokenPipeError:
        print("\033[91m" + "The program cannot be run, or does not intake inputs" + "\033[0m") # Red color
        return ""

def remove_class_files():
    for file in os.listdir('.'):
        if file.endswith('.class'):
            os.remove(file)

if __name__ == "__main__":
    # Compile
    src_dir = 'src'  # Directory containing Main.java
    compile_command = f"javac {src_dir}/Main.java"
    compile_result = run_job(compile_command, [])
    if compile_result:
        print(f"Compilation error:\n{compile_result}")
    else:
        input_data = ["I hope they call me on a Mission!", "n"]  # Inputs for the Java program
        # Inputs for the Java program
        run_command = f"java -cp {src_dir} Main"  # Running the Main class
        run_result = run_job(run_command, input_data)

        expected_output = """This program will ask the user to enter something and then print out a reversed version of the user's input.

Please enter something: I hope they call me on a Mission!
Using the for loop: The reverse of 'I hope they call me on a Mission!' is: !noissiM a no em llac yeht epoh I
Using the while loop: The reverse of 'I hope they call me on a Mission!' is: !noissiM a no em llac yeht epoh I

Would you like to play again? (Y/N): n"""

        # Check if expected output is within run_result
        expected_output_no_spaces = expected_output.replace(" ", "")
        run_result_no_spaces = run_result.replace(" ", "")

        if expected_output_no_spaces in run_result_no_spaces:
            print("Your code works")
        else:
            print("Please! Make sure that your program output matched the example output")
            print("Example output:")
            print(expected_output)
            print("Actual output:")
            print(run_result)
            # You may want to add more sophisticated comparison logic here

    # Remove .class files
    remove_class_files()