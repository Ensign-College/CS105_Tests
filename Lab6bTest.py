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

        output = ""
        for input_line in inputs:
            line = process.stdout.readline().strip()
            output += line + "\n"
            process.stdin.write(input_line + "\n")
            process.stdin.flush()

        # Read the remaining output
        remaining_output = process.stdout.read()
        output += remaining_output

        return output

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
        input_data = [
            "ok... but when do you want me to enter it?", "5", "0", "Sure!!!", "y", "5", "1", "y", "5", "3", "n"
        ]  # Inputs for the Java program
        run_command = f"java -cp {src_dir} Main"  # Running the Main class
        run_result = run_job(run_command, input_data)

        expected_output = """Please enter the first number: Invalid Response: Please enter a whole number.
Please enter the first number: Please enter the second number: 5 raised to the power of 0 is: 1.
Would you like to play again? (Y/N): Invalid response: Please answer with a 'Y' or 'N'.
Would you like to play again? (Y/N): 
Please enter the first number: Please enter the second number: 5 raised to the power of 1 is: 5.
Would you like to play again? (Y/N): 
Please enter the first number: Please enter the second number: 5 raised to the power of 3 is: 125.
Would you like to play again? (Y/N): """

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
            print("\nDifferences:")
            for expected, actual in zip(expected_output_no_spaces, run_result_no_spaces):
                if expected != actual:
                    print("\033[91m" + "Expected: " + expected + "\033[0m") # Red color
                    print("\033[91m" + "Actual: " + actual + "\033[0m") # Red color
            exit(1)

    # Remove .class files
    remove_class_files()
