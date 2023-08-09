import subprocess


def run_job(cmd, input_data=None):
    ret = subprocess.run(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        input=input_data,
        text=True,
    )
    return ret.stdout


if __name__ == "__main__":
    # Compile and Run
    src_dir = 'src'  # Directory containing the Java program
    compile_command = f"javac {src_dir}/Main.java"
    compile_result = run_job(compile_command)

    if compile_result:
        print(f"Compilation error:\n{compile_result}")
    else:
        # Providing inputs in the sequence specified
        input_data = "three\n3\n9\n2\nn\n"
        run_command = f"java -cp {src_dir} Main"  # Running the Lab5c class
        run_result = run_job(run_command, input_data=input_data)

        expected_output = """
        This program will ask the user for three numbers:
            * A starting number
            * An ending number
            * A multiplier
        The program will multiply each number between the starting number and ending number by the multiplier.
        Please enter the starting number: Invalid response: Please enter a whole number.
        Please enter the starting number: Please enter the ending number: Please enter the multiplier: 
        Multiplying 3 by 2 results in: 6
        Multiplying 4 by 2 results in: 8
        Multiplying 5 by 2 results in: 10
        Multiplying 6 by 2 results in: 12
        Multiplying 7 by 2 results in: 14
        Multiplying 8 by 2 results in: 16
        Multiplying 9 by 2 results in: 18
        Would you like to play again? (Y/N): 
        """

        # Check if expected output is within run_result, ignoring whitespace differences
        if expected_output.replace(" ", "").strip() in run_result.replace(" ", "").strip():
            print("Your code works")
        else:
            print("Please! Make sure that your program output matched the example output")
            print("Example output:")
            print(expected_output)
            print("Actual output:")
            print(run_result)
            exit(1)
