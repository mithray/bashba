I believe there is a need to make a unified meta system of linux commands.
This command set must be able to do anything that can be done with an ordinary set of linux commands, but they should be intuitive and easier to learn grok quickly.

rules
1. It must be faster to learn than the full set of Linux commands
2. It must cover at least the same domain as the full set of Linux commands
3. It must be faster to type on average than the full set of Linux commands 
4. It must be moving toward being the fastest way to type and express any desired linux command
5. It must be moving toward using the fastest algoritms possible.
6. It must demonstrably meet the above standards

it seems that there are three ways of accessing a file so perhaps all commands could be broken into these three categories? read, write and execute.

an issue here is that only having three global commands in the namespace is actually an inefficient language. The more words that are in a language, the more potential it has of expressing many things in fewer words. One slight remedy could be to put 'r' as the default, this way r never needs to be typed and its arguments would be equivalent to a namespace/vocabulary.

read, r

replaces ls, find, cat and grep

read 
source,sor:						-;.
match,mtc,m:					*;regex
recurse-into-files,rf,c:		false,0;true,1
recursive-max-depth,mnd:		1;[0-9]*;finalnode,fn
recursive-min-depth,mxd:		1;[0-9]*;finalnode,fn
permissions,per:				all
file-size,sz:					all	
output-format,ofm:	txt;json;csv;smart

this command can be used to read or view anything, system resources, files, system searches, web searches. The key is this is read, not write not execute.
System info could be referenced by names which are stored in shell variables.

EXAMPLES
``` bash
r 			# r by itself works like *ls*. it uses defaults such as max-depth=1 min-depth=1 and just prints the files in the current directory
r r:d			# works like *find* with no arguments, searching all directories for all files
r :c			# works like *cat*. prints the contents for each file listed in the source. Given no source it 'cats' all files in the working directory.
r r:fn			# prints all the contents of all files recursively in all child directories
r r:fn m=*		
```
write, w

execute, x

could be used to execute standard linux commands, as well as being equivalent to ./

commands could be referenced by path or by name.
