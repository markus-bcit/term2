```bash 
Who developed the Linux Kernel
Linus Sebastian
"Linus Torvalds"
Richard Stallman
Ken Thompson

Which operating system did both Linux and MacOS inherit from?
"Unix"
GNU
Minix
FreeBSD

VirtualBox is a…?
Type 1 Hypervisor
"Type 2 Hypervisor"

The three standard types of access, permissions, are…
"read, write and execute"
read, share and run
run, write and execute
write, run and list

If you wanted to delete a word in the shell which would you use?
ctrl + b
ctrl + u
"ctrl + w"
ctrl + c


The three standard Linux permission scopes, in order from narrow to wide, are…
Other, Group, User
Group, User, Everyone
"User, Group, Other"
User, Everyone, Group

Saved

Which utility would you use to change permissions on a file to allow anyone to execute the file?
chown
passwd
"chmod"
usermod

Programs interact with the Linux kernel through system calls.
"True"
False

Fill in the blank.  
In addition to regular users (humans) Linux also has ------ users
"system"

Linux is a single user operating system. Only one user can be logged-in and running programs.
True
"False"

The User "database" is stored in which file in most Linux operating systems?  
Write the full path -------:
"/etc/passwd"
 
Which virtualization tool runs as part of the Linux kernel
VMware
Qemu
Xen
"KVM"

Vagrant is a Virtualization tool, similar to VirtualBox.
True
"False"

man pages with the same name can exist in different sections. For example there could be a man page 'bob' in section 1 and section 5.
True
False

Which option can you use with the man utility to search for a man page?]
-s
-w
"-k"
-l


The two types of Access Control defined in the reading are...
...restrict access to resources based on the identity of the user...
Users can only access resources corresponding to a clearance level...

"Discretionary access control"
"Mandatory access control"
 

which of following would you use to search for a string inside of a man page?
\
|
"/"
:

A user with the UID of 1001 is a...
"Regular user"
The root user
System user
nobody

Which command below will print the shell that you are currently running commands from?
echo $1
"echo $0"
echo %

Which utility does man generally use to display man pages?
"less"
vim
emacs
man

Which month is the LTS version of Ubuntu typically released on?
October
January
There is no typical release schedule
April

In what year was the POSIX standard developed
1991
1983
"1985"
1975

Where will you find Linux OSs?
Question 23 options:
On smart appliances
On Mars
In cars
On servers hosting websites, applications, and services
"All of the other options"

Which man page section is games
1
2
3
4
5
"6"
7
8

Which of the bellow will repeat the previous command run?
!
&
ctrl + l
"!!"

cd is a shell builtin
"True"
False

Which shell are you running as your login shell in Ubuntu?
"bash"
powershell
fish
zsh
mksh

Match the numeric permissions with the symbolic permissions
r--rw---x 461
rwxr-xr-x 755
rw-r-x-wx 653

When you enter a command in Bash each sequence of non-blank characters is called a -----.
"token"

Each process in Linux has a PID automatically assigned by the ______ when the process is created.
"kernel"

Which command below will create the following directory structure. dir1/dir2
mkdir dir1 | mkdir dir2
mkdir dir1 && mkdir dir2
"mkdir -p dir1/dir2"
mkdir dir1 && dir2
```

```bash
vagrant@ubuntu2210:~$ sudo apt update
Hit:1 https://mirrors.edge.kernel.org/ubuntu kinetic InRelease
Hit:2 https://mirrors.edge.kernel.org/ubuntu kinetic-updates InRelease....

vagrant@ubuntu2210:~$ sudo apt upgrade

mkdir dir{1..2}

for dir in $(find . -mindepth 1 -type d); do
  touch $dir/f{1..4}.pyc $dir/p{1..4}.py
done

vagrant@ubuntu2210:~/midterm$ find dir1 dir2 -name *.pyc -exec rm {} +

vagrant@ubuntu2210:/$ sudo useradd assadfdf -u 1050
vagrant@ubuntu2210:/$ grep -E x:[1-9][0-9][0-9][0-9]: /etc/passwd
vagrant:x:1000:1000::/home/vagrant:/bin/bash
asdf:x:1001:1001::/home/asdf:/bin/sh
assadfdf:x:1050:1050::/home/assadfdf:/bin/sh

```

```bash 
$ ls -al
total 0
-rw-r--r--  1  mh9  devs  9  Apr 12 11:42  test
^           ^  ^    ^     ^  ^             ^
|           |  |    |     |  |             └──  filename
|           |  |    |     |  └──  last modified date
|           |  |    |     └──  filesize in bytes
|           |  |    └── group the file belongs to
|           |  └──  user the file belongs to
|           └──  number of hard links
└──  file mode (- indicates a regular file) and permissions g/u/o

root:x:0:0:root:/root:/bin/bash
|    | | | |    |     └──>  The Login Shell
|    | | | |    └──>  The users home directory
|    | | | └──>  users information, generally this is just name
|    | | └──> Group ID (GID)
|    | └──>  User ID (UID)
|    └──>  x indidcates that the user has an encryped password in the shadow file
└──>  The users name
```