import subprocess

def run_job(cmd, inputs):
    try:
        process = subprocess.Popen(
            cmd.split(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        inputs_string = "\n".join(inputs)
        output, _ = process.communicate(inputs_string)

        return output

    except BrokenPipeError:
        print("\033[91m" + "The program can not be run, or does not intake inputs" + "\033[0m") # Red color
        return ""

if __name__ == "__main__":
    # Compile
    src_dir = 'src'  # Directory containing Main.java
    compile_command = f"javac {src_dir}/Main.java"
    compile_result = run_job(compile_command, [])
    if compile_result:
        print(f"Compilation error:\n{compile_result}")
    else:
        input_data = [
            "I hope they call me on a Mission!", "n",
        ]  # Inputs for the Java program
        run_command = f"java -cp {src_dir} Main"
        run_result = run_job(run_command, input_data)

        expected_output = """This program will ask the user to enter something and then print out a reversed version of the user's input.
Please enter something: I hope they call me on a Mission!
Using the for loop: The reverse of 'I hope they call me on a Mission!' is: !noissiM a no em llac yeht epoh I
Using the while loop: The reverse of 'I hope they call me on a Mission!' is: !noissiM a no em llac yeht epoh I
Would you like to play again? (Y/N): n"""

# Split the expected and actual outputs into words
expected_words = set(expected_output.split())
actual_words = run_result.split()

# Check if all actual words are in the expected words
missing_words = [word for word in actual_words if word not in expected_words]

if missing_words:
    print("Your code does not output the expected results.")
    print("Here are the actual words that were not found in the expected output:")
    for word in missing_words:
        print(word)
    exit(1)
else:
    print("Your code works!")
    exit(0)
