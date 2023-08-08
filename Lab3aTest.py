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
    src_dir = os.getcwd()  # Assuming you are in the directory containing Main.java
    compile_command = "javac Main.java"
    compile_result = run_job(compile_command)
    if compile_result:
        print(f"Compilation error:\n{compile_result}")
    else:
        input_data = "41\n"  # Providing the input as 41
        run_command = "java -cp . Main"  # Running the Main class
        run_result = run_job(run_command, input_data=input_data)
        expected_output = "A customer with a chest measurement of 41 inches needs to order a size L.\n"
        if run_result.strip() == expected_output.strip():
            print("Your code works")
        else:
            print(f"Unexpected output:\n{run_result}")

    # Remove .class files
    remove_class_files()
