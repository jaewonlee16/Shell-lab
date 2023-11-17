import subprocess
import re

def run_shell(shell, trace):
    """Run the shell with the specified trace file and capture the output."""
    command = f"./sdriver.pl -t {trace} -s {shell} -a \"-p\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def compare_outputs(output1, output2):
    """Compare the outputs line by line, ignoring differences in PIDs."""
    pattern = re.compile(r"\(\d+\)")  # Pattern to match PIDs
    output1 = re.sub(pattern, "(PID)", output1)
    output2 = re.sub(pattern, "(PID)", output2)

    for i, (line1, line2) in enumerate(zip(output1.split('\n'), output2.split('\n')), start=1):
        if line1 != line2:
            return False, i, line1, line2
    return True, None, None, None

def main():
    trace_files = [f"trace{str(i).zfill(2)}.txt" for i in range(1, 17)]
    for trace in trace_files:
        my_shell_output = run_shell("./tsh", trace)
        ref_shell_output = run_shell("./tshref", trace)
        is_same, line_number, line1, line2 = compare_outputs(my_shell_output, ref_shell_output)
        
        if is_same:
            print(f"Trace {trace}: PASS")
        else:
            print(f"Trace {trace}: FAIL - Difference at line {line_number}")
            print(f"Your shell output: {line1}")
            print(f"Reference output: {line2}")

if __name__ == "__main__":
    main()

