; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i128 @"main"()
{
entry:
  %"$i" = alloca i128
  store i128 0, i128* %"$i"
  br label %"while.cond"
while.cond:
  %"$i.1" = load i128, i128* %"$i"
  %"cmplttmp" = icmp slt i128 %"$i.1", 5
  br i1 %"cmplttmp", label %"while.body", label %"while.end"
while.body:
  %"$i.2" = load i128, i128* %"$i"
  %".5" = bitcast [4 x i8]* @"fmt" to i8*
  %".6" = call i128 (i8*, ...) @"printf"(i8* %".5", i128 %"$i.2")
  %"$i.3" = load i128, i128* %"$i"
  %"addtmp" = add i128 %"$i.3", 1
  store i128 %"addtmp", i128* %"$i"
  br label %"while.cond"
while.end:
  %"$j" = alloca i128
  store i128 1, i128* %"$j"
  br label %"for.cond"
for.cond:
  %"$j.1" = load i128, i128* %"$j"
  %"cmpletmp" = icmp sle i128 %"$j.1", 5
  br i1 %"cmpletmp", label %"for.body", label %"for.end"
for.body:
  %"str_ptr" = getelementptr [10 x i8], [10 x i8]* @".str.428", i128 0, i128 0
  %".12" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".13" = call i128 (i8*, ...) @"printf"(i8* %".12", i8* %"str_ptr")
  br label %"for.inc"
for.inc:
  %"$j.2" = load i128, i128* %"$j"
  %"addtmp.1" = add i128 %"$j.2", 1
  store i128 %"addtmp.1", i128* %"$j"
  br label %"for.cond"
for.end:
  ret i128 0
}

declare i128 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
@"float_format" = internal constant [3 x i8] c"%f\00"
@".str.428" = internal constant [10 x i8] c"Iteracion\00"