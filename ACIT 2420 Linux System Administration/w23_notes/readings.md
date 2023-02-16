**

COMMANDS:

  

$ apropos who:

  

at.allow (5)       - determine who can submit jobs via at or batch

  

jwhois (1)         - client for the whois service

  

w (1)              - Show who is logged on and what they are doing.

  

who (1)            - show who is logged on

  

who (1p)           - display who is on the system

  

whoami (1)         - print effective userid

  

whois (1)          - client for the whois service

  

whois.jwhois (1)   - client for the whois service

  

$ cat → reads from file

  

$ echo $0

-bash

Or the local system might display output like this:

$ echo $0

/bin/bash

  

$ stty → set terminal

$ stty ek → deletes a line in textual editor

  

$ ls → list directories

  

$ rm → removes a file

  

$ rm -i toollist

rm: remove regular file 'toollist'? Y

  

$ cp → copies a file

  

$ mv → changes name of a file

  

$ lpr → prints a file

  

$ head → displays beginning of file

  

![](https://lh3.googleusercontent.com/U52tI08sKpJFcysBGRMNshsUYgdYaVNi-5Amex-8anSYYPOeJsxLmfymyBWLkZ9kanBfXEZL2iQ882vq2p_NiokxImWpJ7y9-OFlJ_zOZPCzl7ME04w-uHcpqili8EfJAn87ygPKaBqVlFRC4V3WrVo)

  

The tail utility is similar to head but by default displays the last ten lines of a file. Depending on how you invoke it, this utility can display fewer or more than ten lines.

  

$sort → The sort utility is useful for putting lists in order. The –u option generates a sorted list in which each line is unique (no duplicates). The –n option puts a list of numbers in numerical order. Refer to page 969 for more information on sort.

  

The pipe character | will "pipe" output from one command into another command. Like filtering the man page search above.

The double ampersand && sudo apt update && sudo apt upgrade. This command is actually two commands, the second will run only if the first succeeds. If the first returns an error the second command won't run.

mkdir this will make a directory mkdir new-dir mkdir -p new-dir/other-new-dir. What do you think the second command does?

  

“Processes”

  

Process is ANY command you execute in Linux

  

fork() → spawns another child process, similar to a fork in the road

  

exec() → if this is called and it is an executable, it will succeed, this is like c programs etc, if == script, it fails. 

  

You can also use pstree (or ps ––forest, with or without the –e option) to see the parent–child relationship of processes.

  

fork() will NOT create a child process for builtins like ls, pwd, etc.

  

Within a given process, such as a login shell or subshell, you can declare, initialize, read, and change variables. Some variables, called shell variables, are local to a process. Other variables, called environment variables, are available to child processes.

  

Some bash builtins, such as if and case, as well as functions and quoted strings, span multiple lines. When bash recognizes a command that covers more than one line, it reads the entire command before processing it

  

Each string from the list is prepended with the string chap_, called the preamble, and appended with the string .txt, called the postscript. Both the preamble and the postscript are optional. The left-to-right order of the strings within the braces is preserved in the expansion. For the shell to treat the left and right braces specially and for brace expansion to occur, at least one comma must be inside the braces and no unquoted whitespace can appear inside the braces. You can nest brace expansions.

  

![](https://lh4.googleusercontent.com/5s_Eb1zE78ZzF8EBPO2TPMrvP4wAp6SV8ntYD41TEyBICOS60hcNPEonBqfIgI37sRxxUCdchPsqFN3cemrjgmVc5_0vyNpazuW3bxJ7twzlOMQcgJYmWghac9yRhPcnIpe9BpUhf4mFiYGgKk9SYtY)

  

With BRACE EXPANSION.

  
  

![](https://lh3.googleusercontent.com/joSD3f2GfYONlHjVCGqWxjktbmgsIseQOM-kuYDWCoPgezSN7capcofPtYW7wgrryFAGPiRHSZYrOaUBZLqSMsIrvf_fN9KRlSb0QsefzuqowpzngEclIYPZZv-5uEEZJIP0cGaZgPUp5cWmfn8HldY)

  

The shell substitutes the value of the HOME variable for the tilde

  

$(paramater) → parameter syntax

  
  
  
  

$((expression)) → Arithmetic expression syntax

  
  

![](https://lh6.googleusercontent.com/iDFQKsVk2p_yhMFBvkNX2o1T_89FbpNzYpmc_k_YbfscmwK16BF1f2FQ8h2sIK_Ib8P_bXc1b8lBjGEZ4X6H6BXf-L1_nqwoORO_zuBylvsCw0cSA4V_TGgP2aVXaDmUUPRKsnaUTxrKx5hoCNvcTiE)

  

^^ Example in a function

  
  

You can supply let with multiple arguments on a single command line

  

Let a=123+12 b=2372+133 → Possible.

  
  

Bash:

  

This section describes the startup files that are executed by login shells and shells that you start with the bash ––login option.

  

 /etc/profile 

  

The shell first executes the commands in /etc/profile, establishing systemwide default characteristics for users running bash

  

.bashrc An interactive nonlogin shell executes commands in the ~/.bashrc file.

The default ~/.bashrc file calls /etc/bashrc. 

  

/etc/bashrc

  

 Although not called by bash directly, many ~/.bashrc files call /etc/bashrc.

  
  

if [ -f ~/.bashrc ]; then . ~/.bashrc; fi → Tests whether or not .bashrc exists within your home directory.

  
  
  

$ cat ~/.bash_profile

if [ -f ~/.bashrc ]; then

    . ~/.bashrc                                # Read local startup file if it exists

fi

PATH=$PATH:/usr/local/bin                      #Add /usr/local/bin to PATH

export PS1='[\h \W \!]\$ '                     #Set prompt

  

→ The first command in the preceding .bash_profile file executes the commands in the user’s .bashrc file if it exists. The next command adds to the PATH variable 

  

Typically, PATH is set and exported in /etc/profile, so it does not need to be exported in a user’s startup file. 

  

The final command sets and exports PS1 (page 319), which controls the user’s prompt.

  

![](https://lh6.googleusercontent.com/NXx6Fkmxg54S_l9ZkZhiZ4DV1cP4ekQnF3s0u9SX_u9skw4MXGoLoocFVgDTFmpN0igE-UB_xXIlB8Kfy-MCtzXCwHd9wN1qUOQOe8FmEVG2kNmmGKN-amaKVRtouOXumko-jTh34qRAHt06CoZrG04)

  
  

Redirecting and Output Control:

  

![](https://lh6.googleusercontent.com/oj05tnjLCozWdRjj38tp77wDb-Wszh2ex0QkyDvcaThygSTrCI0Vgoe0OvvYiGQfspyx8zTKc9yHRvfXESYi-xTtu_FEefVMo6BYFejAeH2bz-Y43rXpTBJewLTwS5H8WgbznVHMOj5F6hmZW2S9CPs)

  

A device file resides in the file structure, usually in the /dev directory, and represents a peripheral device, such as a terminal, printer, or disk drive.

  
  

![](https://lh3.googleusercontent.com/woTiC1_8G5KEguJRubFnrNmpAAtYngNNmnjeUodBPwnZ0I_WNjmU_53i2WUqmCfDWQlwb2EQq3ABokhEfq9CbgiNk0Iz8yJiSG3_ERU90xRnDr3UMZjLEk-Bys0ows_y9WMr6SXI-0TX5sdytrJzIhI)

  

The redirect output symbol (>) instructs the shell to redirect the output of a command to the specified file instead of to the screen (Figure 5-6). The syntax of a command line that redirects output is command [arguments] > filename where command is any executable program (e.g., an application program or a utility), arguments are optional arguments, and filename is the name of the ordinary file the shell redirects the output to.

  

Caution: Redirecting output can destroy a file I

  

Users:

UID 0 Is root

UID 1 to 999 Are reserved for system

users UID 65534Is user nobody—used, for example, for mapping remote users to some well-known ID, as is the case with [“Network File System”](https://learning.oreilly.com/library/view/learning-modern-linux/9781098108939/ch07.html#nfs)

UID 1000 to 65533 and 65536 to 4294967294 Are regular users.

  

VIM:

  

ViM → $ vim [filename] → Opens a new file using vim

  

The command to quit and save edits is ZZ

  

![](https://lh3.googleusercontent.com/5L_tFOV-8w4961HYNEEFJcLgCDFkb5Dnje7RhBTVda4yMTerMIHRiMlPgA5wjlAQi1YNWTiuaRguXV_vHx7yGJnai8S6tto8Cdkt11mIlqiDvWFovOXC9vjU98-MM-glhlFByePci70kujCvLBk1Yl8)

![](https://lh6.googleusercontent.com/QVK9-xkrQVYuH0snQd2tMzaUgLC3HsuBbOM6f-f7vD0Na9hZrU3R5jCvQCnKNATs6IBBoV2cW-PQwn7M4x5_jJEv3zfcAHIUI_yuwwJDA3GUwjHx0YZ5LfFsQ9X1jqSz3zhmLWYRBkMNR4r9ZanEKvA)

  

VIM CHEATSHEAT

h = left, l = right, j = down and k = up

  

MISC:

  

PSUDEO FILESYSTEMS →

  

What is a pseudo filesystem → A pseudo filesystem is, at least in linux, a wrapping of kernel interface that can be interacted with using regular commands we use to manipulate normal filesystems, like ls etc.

  

Inside a pseudo filesystem

  

$ cat /proc/self/status | head -10 [![1](https://lh5.googleusercontent.com/ZoeyKaZcyvyt0DUDSL6PNnwFTUc7WVFO_DRjoWQFmJoHBRytjwLq_Gz6kwfWCPq2T6cAJOjCN_1_8i1eqxvmbEpusChWK3RWoTjeHMeyW5ZBigukY4z55Wyt3eq1TtfxW-E49Va0i8vqNh2dvk7VI7I)](https://learning.oreilly.com/library/view/learning-modern-linux/9781098108939/ch05.html#callout_filesystems_CO8-1)

Name:   cat

Umask:  0002

State:  R (running) [![2](https://lh6.googleusercontent.com/MrEee18KNVyyNzFypzNspgF0wp18C_PSSrmUj-C7qIxoVKK2el_dmBZtzS345ardXlDHytTYXCAUFKu5kwC6ZOuozyu3IPayfF3TKYIPie2EvaVpEXMnfrzMSkpNYn89GxgTJd-3NDPm0rCjzYxSPAE)](https://learning.oreilly.com/library/view/learning-modern-linux/9781098108939/ch05.html#callout_filesystems_CO8-2)

Tgid:   12011

Ngid:   0

Pid:    12011 [![3](https://lh6.googleusercontent.com/WCG8eGzIoda6xntjcMWdpNyjTOOUfbPBySzj0EAv1ix2hVYWzQ98iXqeVFrNp_aWS09aoWvwecDmT__6qwQHte3a-dIno-u9OtL8bIiPdqhQrJDXZP54RbKvD3_epCvyL1pnGGLTl7oC9i30eh4ePp4)](https://learning.oreilly.com/library/view/learning-modern-linux/9781098108939/ch05.html#callout_filesystems_CO8-3)

PPid:   3421 [![4](https://lh4.googleusercontent.com/G5zNbzE0q1-j47piadsggbRa47DFExpOdEwfd_4YtPmNvIbaJ7jolfMIDDWod9l0AXlAPBFoiYCti0mHmCXlH7BWtpls4J5YbreK9dI9D9NSCuH47-pgNWZU6XR-08xy7OtEoy4myLjnYhl3YBrefjk)](https://learning.oreilly.com/library/view/learning-modern-linux/9781098108939/ch05.html#callout_filesystems_CO8-4)

TracerPid:      0

Uid:    1000    1000    1000    1000

Gid:    1000    1000    1000    1000

  

![](https://lh5.googleusercontent.com/sJ1mmH4kmIanQlcb0dxNZ7osK7xdNjbY_jo70P_cS8QakpfxhZNRILdI5ujMEs37PaOPS_YE05t9-ij0tQnITFlXVBGCCcMxsgD4_XGqulrE4Uj_8i8xZ3Oc_Vsikdgs66pIerwhBQex0AK87m-a51w)

  

KERNEL → 

1.  Memory management: Keep track of how much memory is used to store what, and where
 
2.  Process management: Determine which processes can use the central processing unit (CPU), when, and for how long
 
3.  Device drivers: Act as mediator/interpreter between the hardware and processes
 
4.  System calls and security: Receive requests for service from the processes
 

MISC → 

  

Name: The name of the command the man page is describing.

Synopsis: A summary of the command and its syntax.

Configuration: Configuration details for a device.

Description: An explanation of what the program does.

Options: A description of the command-line options the command accepts.

Exit Status: Possible exit status values for the command, and what might cause them to be used.

Return Value: If the man page is for a library routine, this describes the value the library routine can send back to the function that called that routine.

Errors: A list of the values that might be placed in errno [in the event of an error](http://man7.org/linux/man-pages/man3/errno.3.html).

Environment: A list of the environment variables that affect the command or program, and in what way.

Files: A list of the files the command or program uses, such as configuration files.

Attributes: A summary of various attributes of the command.

Versions: Details of the Linux kernel or library versions where a system call or library function first appeared or changed significantly from previous versions.

Conforming to: A description of any standards with which the command might comply, such as [POSIX](https://en.wikipedia.org/wiki/POSIX).

Notes: Miscellaneous notes.

Bugs: Known issues.

Examples: One or more examples demonstrating the use of the command.

Authors: The people who wrote or maintain the command.

See also: Recommended reading related to the command or topic.

  

-rw-r--r-- 1 riversng river 1150 Sep 26 19:51 filename

|[-][-][-]-  [------] [---]

| |  |  | |     |       |

| |  |  | |     |       +------------> 7. Group

| |  |  | |     +--------------------> 6. Owner

| |  |  | +--------------------------> 5. Alternate Access Method

| |  |  +----------------------------> 4. Others Permissions

| |  +-------------------------------> 3. Group Permissions

| +----------------------------------> 2. Owner Permissions

+------------------------------------> 1. File Type

  
  
  
**