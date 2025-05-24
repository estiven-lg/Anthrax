; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"$a1" = alloca float
  %"addftmp" = fadd float 0x4059000000000000, 0x4049000000000000
  store float %"addftmp", float* %"$a1"
  %"$a1.1" = load float, float* %"$a1"
  %".3" = bitcast [3 x i8]* @"float_format" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", float %"$a1.1")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
@"float_format" = internal constant [3 x i8] c"%f\00"