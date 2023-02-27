
-   What is the difference between single and double quotes
	- Double quotes allow for the expansion of variables and special characters, single quotes treat everything as a literal string.
-   How would you print the number of possitional parameters, or items in an array
	- the special parameter `$#`. For example, `echo $#` will print the number of positional parameters.
-   How would you print all of the possitional parameters, or items in an array
	- To print all of the positional parameters, use the special parameter `$@` or `$*`. For example, `echo "$@"` will print all of the positional parameters. Similarly, to print all the
-   How would you display the exit status of a command
	- Use the special parameter `$?`. For example, if you run the command `ls`, the exit status is stored in `$?`. You can display it by running `echo $?`.
-   What is a file test
	- File tests in Linux are used to check various properties of a file, such as whether it exists, its type, permissions, and ownership. They are often used in Bash scripts to make decisions based on the state of a file.
-   How would you test if a directory exists
	- Use the `-d` option with the `test` command or its equivalent, the `[` command. For example, to test if the directory `/home/user` exists, run `test -d /home/user` or `[ -d /home/user ]`.
-   What is command substitution
	- Command substitution is a feature in Bash that allows you to run a command and use its output as an argument to another command. It is done by enclosing the command in either `$()` or `````` backticks. For example, to assign the output of the `date` command to a variable `today`, you can run `today=$(date)`.
-   What is a here document
	- A here document is a way to redirect input to a command or script from within the shell script itself. It allows you to specify a block of text that will be treated as standard input. It is denoted by `<<` followed by a delimiter, which can be any word of your choice. For example, to pass a here document to the `cat` command, you can run:

[How Linux Works, 3rd Edition](https://learning.oreilly.com/library/view/how-linux-works/9781098128913/c11.xhtml)
