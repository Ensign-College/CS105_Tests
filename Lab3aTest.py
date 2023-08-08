import os
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

def remove_class_files():
    for file in os.listdir('.'):
        if file.endswith('.class'):
            os.remove(file)

if __name__ == "__main__":
    # Compile
    src_dir = 'src'  # Directory containing Main.java
    compile_command = f"javac {src_dir}/Main.java"
    compile_result = run_job(compile_command)
    if compile_result:
        print(f"Compilation error:\n{compile_result}")
    else:
        input_data = "41\n"  # Providing the input as 41
        run_command = f"java -cp {src_dir} Main"  # Running the Main class
        run_result = run_job(run_command, input_data=input_data)
        expected_output = "A customer with a chest measurement of 41 inches needs to order a size L.\n"
        # Check if expected output is within run_result
        if expected_output.strip() in run_result.strip():
            print("Your code works")
        else:
            print("Please! Make sure that your program output matched the example output")
            print("Example output:")
            print(expected_output)
            print("Actual output:")
            print({run_result})
            exit(1)
    # Remove .class files
    remove_class_files()