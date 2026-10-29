# 00.03 · Read commands, paths and error messages

**Prerequisite:** a working Python interpreter from 00.02. You will learn how to read command examples without guessing. Allow 45–60 minutes.

## The pieces of a command

Consider `python3 06-tools/03-doctor.py`. `python3` is the program. `06-tools/03-doctor.py` is an argument: a location that tells Python which file to execute. The slash separates a directory from a file. The `.py` ending identifies Python source by convention. The number is part of this course's filename and must be included.

A relative path starts at the current working directory. An absolute path starts at a filesystem root or drive. `.` means the current directory and `..` means its parent. This is why the same relative command can work from the repository root and fail from a different folder.

When a lesson shows a code block labeled `sh`, type each command line in your terminal. When it shows a block labeled `python`, save the code in the instructed file. A block labeled `text` is expected output: read it, but do not execute it. Prompts such as `$` are not part of the commands in this course.

## Follow along

1. From the repository root, run `python3 -c "from pathlib import Path; print(Path.cwd().name)"`. It prints your current folder's name. The exact folder name can vary with how you downloaded the course.
2. Run `python3 -c "from pathlib import Path; print(Path('00-INDEX.md').is_file())"`. Expect `True`.
3. Run `python3 06-tools/03-doctor.py` and compare its output with lesson 00.02.
4. Deliberately run `python3 06-tools/99-missing.py`. It must fail because the file does not exist. Read the message from left to right: which program reported the error, which path was requested, and what prevented it from proceeding?
5. Re-run the correct doctor command. Repair means changing the wrong input, not reinstalling every tool.
6. Run `python3 -c "import sys; sys.exit(7)"`. This prints nothing but exits with status 7. In macOS/Linux shells, immediately run `echo $?`; in PowerShell run `$LASTEXITCODE`. Expect 7. Commands can fail even when they print no error text.

## Why exit codes matter

A program's exit code is a small status number returned to its caller. Zero conventionally means success. Nonzero means another outcome, defined by the program. The local platform tool uses 1 for a contract rejection and 2 for input or usage errors. CI uses these codes to decide whether to stop. Reading only printed text can miss the actual status.

## Troubleshooting practice

If the index check prints `False`, inspect the current directory before changing code. If the missing-file command succeeds, check that you actually typed the missing name. If you check the exit code after another successful command, you see that newer command's code. Observe immediately after the command you are investigating.

## Checkpoint

Write `99-work/03-command-notes.md` containing one successful command, one deliberate failure, their exit codes and your repair. Explain relative path and current directory using those observations. These are skills you will reuse in every later lab.

[Primary reference: Python command-line options](https://docs.python.org/3/using/cmdline.html).

[← Previous lesson](02-set-up-a-computer-for-the-course.md) · [Next lesson →](../01-terminal-and-operating-systems/01-create-inspect-and-copy-files.md)
