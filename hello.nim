import json
import re
import osproc
import system
import parseopt
import os

proc writeHelp() = 
  echo """

Bashba 0.0.1
Allowed Commands:
  ls       : list
  rd   : read
     : 
     : 
Allowed Options:
  -h | --help       : show help
  -a | --accessed   : 
  -m | --modified   : 
  -c | --created    : 
  """


let params = commandLineParams()
#let name: string = readLine(stdin)
var p = initOptParser(params)

while true:
  p.next()
  case p.kind
  of cmdEnd: break
  of cmdShortOption, cmdLongOption:
    if p.val == "":
     echo "Option: ", p.key
    else:
      echo "Option and value: ", p.key, ", ", p.val
  of cmdArgument:
    let outp = execCmdEx p.key
    let results = split(outp.output, re(r"\n"))
    let results_json = %* results
    echo pretty(results_json)

