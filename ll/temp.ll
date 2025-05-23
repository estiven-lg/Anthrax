; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"$i" = alloca i32
  store i32 0, i32* %"$i"
  br label %"while.cond"
while.cond:
  %"$i.1" = load i32, i32* %"$i"
  %"cmplttmp" = icmp slt i32 %"$i.1", 5
  br i1 %"cmplttmp", label %"while.body", label %"while.end"
while.body:
  %"$i.2" = load i32, i32* %"$i"
  %".5" = bitcast [4 x i8]* @"fmt" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %"$i.2")
  %"$i.3" = load i32, i32* %"$i"
  %"addtmp" = add i32 %"$i.3", 1
  store i32 %"addtmp", i32* %"$i"
  br label %"while.cond"
while.end:
  %"$j" = alloca i32
  store i32 1, i32* %"$j"
  br label %"for.cond"
for.cond:
  %"$j.1" = load i32, i32* %"$j"
  %"cmpletmp" = icmp sle i32 %"$j.1", 5
  br i1 %"cmpletmp", label %"for.body", label %"for.end"
for.body:
  %"str_ptr" = getelementptr [10 x i8], [10 x i8]* @".str.302", i32 0, i32 0
  %".12" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".12", i8* %"str_ptr")
  br label %"for.inc"
for.inc:
  %"$j.2" = load i32, i32* %"$j"
  %"addtmp.1" = add i32 %"$j.2", 1
  store i32 %"addtmp.1", i32* %"$j"
  br label %"for.cond"
for.end:
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
@".str.302" = internal constant [10 x i8] c"Iteracion\00"