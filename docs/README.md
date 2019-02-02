# Bourne Again Shell, Bourne Again

Over the years, linux shell commands have become confusing, with often conflicting syntax. The bourne again shell is an attempt to unify as many of the most important shell commands as possible under a new, unified syntax.


## Linux Tenets

### Summary

#### 9 Major Tenets

1.	Small is beautiful
2.	Make each program do one thing well
3.	build a prototype ASAP
4.	Portability > Efficiency
5.	Store numerical data in flat files
6.	Use software leverage to your advantage (?)
7.	Use scripts for leverage & portability
8.	Avoid captive user interfaces
		-what you see is *all* you get
9.	Make every program a filter

#### 10 Lesser Tenets

1.	Allow the user to tailor the environment
2.	Make system kernels small & lightweight
3.	Use lower case and keep it short
4.	Save trees(less paper?)
5.	Silence is golder(reduce output? fail silently?)
6.	Think Parallel(?)
7.	Sum of the parts is greater than the whole
		-what you see is *all* you get
8.	Look for the ninety percent solution
9.	Worse is better(??? better than not being free and customizable ? )
10.	Think hierarchically

### EXPOSITION

#### Major

1.	small relates to the efficiency of m x n = e. m+n=size. m*n=expressiveness. If a language is larger it can be more expressive, but the language itself takes up more space and a longer time to learn. if m = (number of words in a language) and n=(number of words in an expression), then m x n is greatest when m and n have similar values. So depending on the requirements(e=expressiveness), the language should grow or shrink accordingly to reach maximum efficiency.
2.	words should have distinct boundaries. words should be able to be taken in and out of a language without destroying the language.
3.	development should be incremental, gradually working in features and testing(?). (Anything is possible if it is broken into small enough steps ? )
4.	Better to be Larger in Size and Lower in Speed than to be available on less systems.
5.	As everything is a text stream, for maximum configurability everything should be kept in text files
6.	?
7.	
8.	Don't ever let graphics limit usefulness- What you see is *all* you get. MY SOLUTION> what you see is *all you can get*.
9. 


> In a 2d surface, where the category that is inhereted is space, a vertex of a graph should be considered an area. A child of a vertex is then a subarea. If two areas overlap, then the area that overlaps can be considered as a child of two parents. It is therefore multi-parent, Directed, and Acyclic.
> In a 2d surface where it is not possible to overlap, the graph can be considered to be Single Parent, Directed and Acyclic
>  - This belongs in Mnd ? 

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

```
read 
source,sor:						-;.
match,mtc,m:					*;regex
recurse-into-files,rf,c:		false,0;true,1
recursive-max-depth,mnd:		1;[0-9]*;finalnode,fn
recursive-min-depth,mxd:		1;[0-9]*;finalnode,fn
permissions,per:				all
file-size,sz:					all	
output-format,ofm:	txt;json;csv;smart
```

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
