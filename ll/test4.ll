; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"$num1" = alloca i32
  %"addtmp" = add i32 10, 5
  %"multmp" = mul i32 %"addtmp", 2
  store i32 %"multmp", i32* %"$num1"
  %"$num2" = alloca i32
  %"$num1.1" = load i32, i32* %"$num1"
  %"divtmp" = sdiv i32 %"$num1.1", 3
  %"subtmp" = sub i32 %"divtmp", 1
  store i32 %"subtmp", i32* %"$num2"
  %"$num1.2" = load i32, i32* %"$num1"
  %".4" = bitcast [4 x i8]* @"fmt" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %"$num1.2")
  %"$num2.1" = load i32, i32* %"$num2"
  %".6" = bitcast [4 x i8]* @"fmt" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %"$num2.1")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"