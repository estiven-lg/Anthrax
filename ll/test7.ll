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
  %"cmplttmp" = icmp slt i32 %"$x.1", 20
  br i1 %"cmplttmp", label %"for.body", label %"for.end"
for.body:
  %"$x.2" = load i32, i32* %"$x"
  %".5" = bitcast [4 x i8]* @"fmt" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %"$x.2")
  br label %"for.inc"
for.inc:
  %"$x.3" = load i32, i32* %"$x"
  %"addtmp" = add i32 %"$x.3", 5
  store i32 %"addtmp", i32* %"$x"
  br label %"for.cond"
for.end:
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"