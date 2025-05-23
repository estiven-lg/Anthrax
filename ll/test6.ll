; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"$contador" = alloca i32
  store i32 10, i32* %"$contador"
  br label %"while.cond"
while.cond:
  %"$contador.1" = load i32, i32* %"$contador"
  %"cmpgttmp" = icmp sgt i32 %"$contador.1", 0
  br i1 %"cmpgttmp", label %"while.body", label %"while.end"
while.body:
  %"$contador.2" = load i32, i32* %"$contador"
  %".5" = bitcast [4 x i8]* @"fmt" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %"$contador.2")
  %"$contador.3" = load i32, i32* %"$contador"
  %"subtmp" = sub i32 %"$contador.3", 1
  store i32 %"subtmp", i32* %"$contador"
  br label %"while.cond"
while.end:
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"