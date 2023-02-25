# Linux Command

- `chmod` make our program “executable”
  - `+x` add an “executable” attribute to the file
```bash
chmod +x hello.py # +x will add an “executable” attribute to the file

#  Now can run the program like
./hello.py
```

- `echo` to print

```bash
echo $USER
# quannguyen
echo $HOME
# /Users/quannguyen
```

- `env` is the env program will tell you about your “environment.”
  - If you run `env` on your computer, you should see your login name and your home directory.
  - use the `env <program_name>` command to find and run programs, say if we type`env python3`, the env program is looking for python3 in the environment. If Python has not been installed, it won’t be able to find it, but it’s also possible that Python has been installed more than once.
- `which` to see where the program is installed

```bash
which env
# /usr/bin/env
which python3
# /usr/local/bin/python3
```
