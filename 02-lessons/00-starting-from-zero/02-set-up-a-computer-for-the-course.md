# 00.02 · Set up a computer for the course

**Prerequisite:** lesson 00.01. Allow 45–90 minutes for installation. You will install a programming interpreter and learn where commands are entered. Nothing here creates paid infrastructure.

## Understand the tools

A terminal is a window for typing commands. A shell reads those commands and starts programs. A text editor saves plain text such as Python code and JSON configuration. Python is a programming language; its interpreter executes files written in that language. Git records changes to files. You do not need a special paid editor.

The course's first labs use the Python standard library: modules bundled with a normal Python installation. There is no `pip install` step. Later lessons introduce containers and clusters only after you understand the programs they run.

## Follow along: install and verify

1. Download a supported Python 3 release, version 3.10 or newer, from [python.org downloads](https://www.python.org/downloads/). Follow the installer for your operating system. On Windows, enable the installer's command-line/PATH option if offered. On macOS, keep the operating system's own Python installation separate; select the newly installed interpreter rather than replacing system files.
2. Open Terminal on macOS, a terminal application on Linux, or PowerShell on Windows. Type `python3 --version` and press Enter. On Windows, try `py -3 --version` if `python3` is unavailable. You should see `Python 3.x.y` with a version at least 3.10. Do not type the printed result as a second command.
3. Type `python3 -c "print('My computer can run Python')"`. Windows users may substitute `py -3`. The `-c` option means “execute the following short program.” The quotes group the program so the shell passes it as one argument.
4. Install Git from its [official installation guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Type `git --version`. A version number proves that the program can be found; it does not mean you have created a repository yet.
5. Download and extract this course. Locate the folder containing `00-INDEX.md`. This is the repository root: the starting folder for the commands in this course.
6. In your terminal, type `cd ` including the trailing space, then enter the full location of that extracted folder. Put the location in quotes when it contains spaces. Press Enter. Use `pwd` on macOS/Linux or `Get-Location` in PowerShell to see the current location.
7. Run `python3 06-tools/03-doctor.py`. It checks Python and reports other tools. Docker, kind and kubectl are not required yet; their absence should not stop the foundation lessons.

## Expected result and repair

The doctor must show the Python interpreter as supported. If the command is not found, close and reopen the terminal after installing, then verify PATH or use the installed interpreter's full location. If it says it cannot open the doctor file, you are probably outside the repository root. Locate `00-INDEX.md` again and change into that folder.

Do not copy a person's private machine location from a screenshot. Your installation path will differ. This course uses relative paths so its files can be placed in different locations.

## Checkpoint

Create `99-work/02-environment.md` using your editor. Record operating system, Python version, Git version and the doctor's result. This is your first environment record. The optional runtime tool checks may say “not found.”

[Python setup reference](https://docs.python.org/3/using/index.html).

[← Previous lesson](01-what-a-platform-engineer-actually-does.md) · [Next lesson →](03-read-commands-paths-and-error-messages.md)
