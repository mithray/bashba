# Bashba

This shell is aimed to radically simplify many bash commands to make the interface pedantically consistent, which should remove the need to memorize so many flags and peruse the man pages so frequently.

So far, only basic file management has been considered.
[I am now thinking the name 'Read' should be replaced by 'Search' and apply only to searching the file system. Printing from files should be a separate command. Search is for metadata. Read is for files and streams.]

## config.yaml
```
ls:
  search:
    recursive: 1,1
  output:
    format: yaml
    human: true
  verbosity:
    permission: true
    owner: true
    size: true
    created: true
    name: true
    accessed: false
    modified: false
    inode: false
rd:
  input:
    detect: true
    raw: false
    zip: false
    bz2: false
    gz: false
    tar: false
    rar: false
  output:
    raw: true
  portion: m,n
```

## ls, list - Operates on File and Directory Metadata
```
# Searching and Output
ls -f --format <pretty|json|yaml|bash|csv> # Defaults to pretty, similar to tree
ls -r --recursive <m,n> 
ls -v --verbose <1|2|acimopsn> # Which Metadata to include in output
ls -h --human # Human Readable Units

# Constraints Based on Metadata
ls -a --accessed <m,n>
ls -c --created <m,n>
ls -i --inode <m,n>
ls -m --modified <m,n>
ls -o --owner x:x
ls -p --permission <xxx>
ls -s --size <m,n>
ls -n --name
```
This command aims to replace all commands related to listing, searching, and printing, as these are all really names for the same thing.

``` Listing

# Bash 'ls' lists hidden files by default, and just like 'ls', it assumes default path is '.'
ls -a <path> 
ls <path>

# 'ls' replaces the ls '-l' flag with a 'verbose' flag '-v'
ls -al <path>
ls -v <1|2> <path> # mode 1 is default without the -v flag, mode 2 is default with the -v flag
ls -v <acmops> <path> # These specify which metadata to include in the output from accessed, created, modified, owner, permission, size

# 'ls' gives the opportunity of outputting into other formats such as json. Pretty printing is standals.
ls -a <path> | jq . # There is no equivalent in bash. But jq is a common package to manage json in a command line interface.
ls -f <pretty|json|bash|csv> <path>
```

``` Searching

# Find - Find in Filesystem
# 'find' is basically a recursive 'ls' with more options, so these commands are combined with functionality determined with flags. There is no need for two commands that do the same thing.
find <path>
ls -r <path>

# As the path can contain a regex expression, there is no need for -name or -iname
find <path> -name <regex>
ls -r <path>/<regex>

# the mindepth and maxdepth specify the level of recursion, the syntax follows javascript and is also similar to transmission-remote where multiple options are separated with a comma.
# The '-rm,' flag, where m is an integer,  specifies that the search will be performed starting at depth 'm' of the <path> and descending to the end of the file heirarchy.
find <path> -mindepth m
ls -rm, <path>

# The '-r,n' flag, where n is an integer, specifies that the search will be performed starting at <path> and and descending to depth 'n' of the file heirarchy.
find <path> -maxdepth n
ls -r,n <path>

# The '-rm,n' flag, where m and n are integers, specifies that the search will be performed starting at <path> and and descending to depth 'n' of the file heirarchy.
find <path> -mindepth m -maxdepth n
ls -rm,n <path>

# Find - Metadata Constraints
ls -a m,		# Find files accessed m days ago or greater
ls -a ,n		# Find files accessed up to n days ago
ls -a m,n		# Find files accessed between m and n days ago

ls -c m,		# Find files created m days ago or greater
ls -c ,n		# Find files created up to n days ago
ls -c m,n		# Find files created between m and n days ago

ls -m m,		# Find files modified m days ago or greater
ls -m ,n		# Find files modified up to n days ago
ls -m m,n		# Find files modified between m and n days ago

ls -s m,		# Find files with a size of m or greater
ls -s ,n		# Find files with a size up to n
ls -s m,n		# Find files with a size between m and n
```

## Reading = Printing(Catting) Reads and parses the Contents of Files and Folders themselves
``` bash
cat <path>
rd <path>

bzip
bunzip
gzip
gunzip
tar
pandoc
```

## System
``` bash
sys # with no parameters, this should give a summary of each of the other system categories, such as Network and Resource use, and attached devices

sys -u # Live Updates

sys -p # Processes
ps e

sys -n # Network
ss -tl # Network Default Summary = Listening TCP Sockets[ and include IP Address ?]

sys -r # Resources - cpu, motherboard, graphics, temperature load
free -a # Resource default Summary

sys -d # attached devices
fdisk -l #

```

