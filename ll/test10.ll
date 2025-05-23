; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = call i32 @"factoria"(i32 5)
  %".3" = bitcast [4 x i8]* @"fmt" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
define i32 @"factoria"(i32 %".1")
{
entry:
  %"$n" = alloca i32
  store i32 %".1", i32* %"$n"
  %"$n.1" = load i32, i32* %"$n"
  %"cmpeqtmp" = icmp eq i32 %"$n.1", 0
  br i1 %"cmpeqtmp", label %"then", label %"ifcont"
then:
  ret i32 1
ifcont:
  %"$n.2" = load i32, i32* %"$n"
  %"$n.3" = load i32, i32* %"$n"
  %"subtmp" = sub i32 %"$n.3", 1
  %".6" = call i32 @"factoria"(i32 %"subtmp")
  %"multmp" = mul i32 %"$n.2", %".6"
  ret i32 %"multmp"
}
