; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i128 @"main"()
{
entry:
  %".2" = call i128 @"factoria"(i128 100)
  %".3" = bitcast [4 x i8]* @"fmt" to i8*
  %".4" = call i128 (i8*, ...) @"printf"(i8* %".3", i128 %".2")
  ret i128 0
}

declare i128 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
@"float_format" = internal constant [3 x i8] c"%f\00"
define i128 @"factoria"(i128 %".1")
{
entry:
  %"$n" = alloca i128
  store i128 %".1", i128* %"$n"
  %"$n.1" = load i128, i128* %"$n"
  %"cmpeqtmp" = icmp eq i128 %"$n.1", 0
  br i1 %"cmpeqtmp", label %"then", label %"ifcont"
then:
  ret i128 1
ifcont:
  %"$n.2" = load i128, i128* %"$n"
  %"$n.3" = load i128, i128* %"$n"
  %"subtmp" = sub i128 %"$n.3", 1
  %".6" = call i128 @"factoria"(i128 %"subtmp")
  %"multmp" = mul i128 %"$n.2", %".6"
  ret i128 %"multmp"
}
