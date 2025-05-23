; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"$x" = alloca i32
  store i32 0, i32* %"$x"
  br label %"for.cond"
for.cond:
  %"$x.1" = load i32, i32* %"$x"
  %"cmplttmp" = icmp slt i32 %"$x.1", 10
  br i1 %"cmplttmp", label %"for.body", label %"for.end"
for.body:
  %"$x.2" = load i32, i32* %"$x"
  %".5" = call i32 @"fib"(i32 %"$x.2")
  %".6" = bitcast [4 x i8]* @"fmt" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  br label %"for.inc"
for.inc:
  %"$x.3" = load i32, i32* %"$x"
  %"addtmp" = add i32 %"$x.3", 1
  store i32 %"addtmp", i32* %"$x"
  br label %"for.cond"
for.end:
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
define i32 @"fib"(i32 %".1")
{
entry:
  %"$n" = alloca i32
  store i32 %".1", i32* %"$n"
  %"$n.1" = load i32, i32* %"$n"
  %"cmpletmp" = icmp sle i32 %"$n.1", 1
  br i1 %"cmpletmp", label %"then", label %"ifcont"
then:
  %"$n.2" = load i32, i32* %"$n"
  ret i32 %"$n.2"
ifcont:
  %"$n.3" = load i32, i32* %"$n"
  %"subtmp" = sub i32 %"$n.3", 1
  %".6" = call i32 @"fib"(i32 %"subtmp")
  %"$n.4" = load i32, i32* %"$n"
  %"subtmp.1" = sub i32 %"$n.4", 2
  %".7" = call i32 @"fib"(i32 %"subtmp.1")
  %"addtmp" = add i32 %".6", %".7"
  ret i32 %"addtmp"
}
