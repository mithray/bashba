import  strutils, os, strtabs, streams, cpuinfo, winlean


let outp = execProcess("nim", args=["c", "-r", "hello.nim"])
