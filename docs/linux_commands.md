# Linux Command

## Special Variables

### `$PATH` variable

- Windows, macOS, and Linux all have a `$PATH` variable, which is a list of directories the OS will look in to find a program (using the `env` program)
  - The `$PATH` variable is a way of telling your computer to only look in places where executable programs can be found.
  - The directories are separated by colons (`:`). Notice that the directory where **python3** lives is the first one in `$PATH`
  - The `$PATH`  is located at `~/.bashrc` user's file or or `~/.zshrc`

```bash
 echo $PATH
/Users/quannguyen/repos/tiny_python_projects/venv/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin:/Applications/Visual Studio Code.app/Contents/Resources/app/bin:/Applications/Visual Studio Code.app/Contents/Resources/app/bin
```

#### Altering your `$PATH`

- Simply add the path where your program (script) is located to $PATH, You should now be able to execute the script anywhere on your system by just typing in its name, without having to include the full path as you type it.

```bash
$ mkdir ~/bin                      # Use the mkdir (“make directory”) command to create ~/bin.
$ cp 01_hello/hello.py ~/bin       # Use the cp command to copy the 01_hello/hello.py program to the ~/bin directory.
$ PATH=~/bin:$PATH                 # Put the ~/bin directory first in $PATH.
$ PATH=$PATH:~/bin                 # Put the ~/bin directory last in $PATH.
$ which hello.py                   # /home/quannguyen/bin/hello.py

```

## Common Linux Commands
###  `chmod`
- `chmod` make our program “executable”
  - `+x` add an “executable” attribute to the file

```bash
chmod +x hello.py # +x will add an “executable” attribute to the file

#  Now can run the program like
./hello.py
```
###  `echo`
- `echo` to print

```bash
echo $USER
# quannguyen
echo $HOME
# /Users/quannguyen
```
###  `env`
- `env` is the env program will tell you about your “environment.”

  - If you run `env` on your computer, you should see your login name and your home directory.
  - use the `env <program_name>` command to find and run programs, say if we type`env python3`, the env program is looking for python3 in the environment. If Python has not been installed, it won’t be able to find it, but it’s also possible that Python has been installed more than once.
```bash
➜  ~ env python3
Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
###  `which`
- `which` to see where the program is installed

```bash
which env
# /usr/bin/env
which python3
# /usr/local/bin/python3
```
## Daily Knowledge
### Day 1

- `du -sh` to find the size of the current folder
