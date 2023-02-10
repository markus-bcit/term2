Mushtaq, Muhammad Asad - Rajan, Ramith - Afonso, Markus

**Part one: 1 point**

![[Pasted image 20230208110026.png]]

**Part two: 3 points** 

![[Pasted image 20230208090132.png]]
![[Pasted image 20230208104945.png]]
![[Pasted image 20230208085516.png]]
**Found in the 1st section of the ps man page. **

**Part three: 2 points**
![[Pasted image 20230208110404.png]]
![[Pasted image 20230208100341.png]]

**part four: 2 points**

```bash 
#!/bin/bash
#: Title       : lclsrch
#: Date        : Feb 8 2023
#: Author      : Markus Afonso
#: Version     : 1.0
#: Description : searches for arg and saves to/Documents/week5/
#: Options     : None

grep -rl $1 ~ > ~/Documents/week5/search-file-$1

```
Step 1: cd into `~/bin` 
Step 2: Run `chmod u+x lclsrch` to make the script executable.
Step 3: run script lclsrch by giving it search parameter as follows: 
`./lclsrch <parameter>`. 
Example usage: `./lclsrch alias`
Step 4: the output file will be saved in directory `~/Documents/week5/`
