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
     print("\033[91m" + "The program can not be run, or does not intake inputs" + "\033[0m")  # Red color


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
        input_data = ["a lot!", "250.50", "3.75", "18", "n"]  # Inputs for the Java program
        run_command = f"java -cp {src_dir} Main"  # Running the Main class
        run_result = run_job(run_command, input_data)

        expected_output = """Month              Balance
Month 1:         $251.28
Month 2:         $503.35
Month 3:         $756.21
Month 4:         $1,009.85
Month 5:         $1,264.29
Month 6:         $1,519.52
Month 7:         $1,775.56
Month 8:         $2,032.39
Month 9:         $2,290.02
Month 10:      $2,548.46
Month 11:      $2,807.71
Month 12:      $3,067.76
Month 13:      $3,328.63
Month 14:     $3,590.32
Month 15:     $3,852.82
Month 16:     $4,116.14
Month 17:     $4,380.29
Month 18:     $4,645.26"""

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
