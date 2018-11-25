# What is it?
- File Organise (FO) is supposed to clean up a messy folder and organise all the files in to folders.
- It has 2 modes the default mode is to clean up according to file extension if a new file extension is found it will ask the user what to do.
- The other mode is custom you write your own `.cfg` file and it will follow it. Although it does have its limitations.

# Who is it made for?

- People comfortable using the command line
- People who don't want to spend time organising files

# How to use `FO`?

- `-f`: Use this to give a custom configuration file
	- **Usage**: `-f <Name of config File.cfg>`
- `-dir`: This parameter must be given. This is the directory that will be sorted
	- **Usage**: `-dir <path to folder>`
- `-s`: will sleep the computer after sorting finishes default is false
	- **Usage**: `-s`

# Examples:

```sh

python3 FO.py -dir "/home/<UserName>/Music" -f Music.cfg -s # Custom confing File Music.cfg and -s for sleep
python3 FO.py -dir "/home/<UserName>/Music" -s				# Default sorting and -s for sleep
python3 FO.py -dir "/home/<UserName>/Music"					# just Default sorting

```
