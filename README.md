################
CS:APP Shell Lab
################

Files:

Makefile	# Compiles your shell program and runs the tests
README		# This file
tsh.c		# The shell program that you will write and hand in
tshref		# The reference shell binary.

### The remaining files are used to test your shell
sdriver.pl	# The trace-driven shell driver
trace*.txt	# The 15 trace files that control the shell driver
tshref.out 	# Example output of the reference shell on all 15 traces

### Little C programs that are called by the trace files
myspin.c	# Takes argument <n> and spins for <n> seconds
mysplit.c	# Forks a child that spins for <n> seconds
mystop.c        # Spins for <n> seconds and sends SIGTSTP to itself
myint.c         # Spins for <n> seconds and sends SIGINT to itself

# Shell Lab: Writing Your Own Unix Shell


### Course Information
**Course**: System Programming (430.658.004) : Fall 2023  
**Assignment**: Shell Lab - Writing Your Own Unix Shell  


### Introduction
The purpose of this assignment is to familiarize yourself with process control and signaling concepts by writing a simple Unix shell program that supports job control.

### Logistics
- **Individual Work**: This assignment must be completed individually.
- **Collaboration**: Discussing ideas with classmates is allowed, but all code must be written independently.
- **Plagiarism**: The code will be checked for plagiarism. Any violations will result in a failing grade and notification to the student committee.

### Getting Started
1. **Setup**:
   - Copy the file `shlab-handout.tar` to your lab directory.
   - Run `tar xvf shlab-handout.tar` to expand the tar file.
   - Run `make` to compile and link the test routines.

2. **Code Overview**:
   - The `tsh.c` file contains the skeleton of a simple Unix shell.
   - Implement the following functions:
     - `eval`: Parses and interprets the command line [~70 lines]
     - `builtin_cmd`: Recognizes and interprets built-in commands (`quit`, `fg`, `bg`, `jobs`) [~25 lines]
     - `do_bgfg`: Implements the `bg` and `fg` commands [~50 lines]
     - `waitfg`: Waits for a foreground job to complete [~20 lines]
     - `sigchld_handler`: Catches `SIGCHLD` signals [~80 lines]
     - `sigint_handler`: Catches `SIGINT` signals [~15 lines]
     - `sigtstp_handler`: Catches `SIGTSTP` signals [~15 lines]

3. **Compiling**:
   - Each time you modify `tsh.c`, run `make` to recompile.
   - Run your shell with `./tsh`.

### Unix Shells Overview
A Unix shell is an interactive command-line interpreter. It prints a prompt, waits for a command line, and executes commands. Commands can be built-in or executable programs. Job control allows managing foreground and background jobs, with signals like `SIGINT` (Ctrl-C) and `SIGTSTP` (Ctrl-Z) used to control job states.

### Shell Specification (`tsh`)
- **Prompt**: `tsh> `
- **Commands**:
  - Built-in commands (`quit`, `jobs`, `bg`, `fg`) are handled immediately.
  - Executable files are loaded and run in child processes.
- **Job Control**:
  - Foreground jobs are indicated by not ending commands with `&`.
  - Background jobs end with `&`.
  - Supports job IDs (JID) with `%` prefix and process IDs (PID).
- **Built-in Commands**:
  - `quit`: Terminates the shell.
  - `jobs`: Lists background jobs.
  - `bg <job>`: Sends `SIGCONT` to a job and runs it in the background.
  - `fg <job>`: Sends `SIGCONT` to a job and runs it in the foreground.
- **Signal Handling**:
  - `SIGINT` (Ctrl-C) sends a signal to the foreground job to terminate it.
  - `SIGTSTP` (Ctrl-Z) sends a signal to stop the foreground job.
- **Zombie Reaping**: `tsh` should properly handle terminated child processes.

### Testing
- **Reference Solution**: The `tshref` executable is provided as a reference.
- **Shell Driver**: The `sdriver.pl` script tests your shell using trace files.
  - Usage: `./sdriver.pl -h`
  - Example: `./sdriver.pl -t trace01.txt -s ./tsh -a "-p"`
  - To compare results: `./sdriver.pl -t trace01.txt -s ./tshref -a "-p"`
- **Make Targets**:
  - `make test01` runs your shell with `trace01.txt`.
  - `make rtest01` runs the reference shell with `trace01.txt`.
