; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"$edad" = alloca i32
  store i32 19, i32* %"$edad"
  %"$edad.1" = load i32, i32* %"$edad"
  %"cmpgetmp" = icmp sge i32 %"$edad.1", 18
  br i1 %"cmpgetmp", label %"then", label %"else"
then:
  %"str_ptr" = getelementptr [19 x i8], [19 x i8]* @".str.623", i32 0, i32 0
  %".4" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8* %"str_ptr")
  br label %"ifcont"
else:
  %"str_ptr.1" = getelementptr [19 x i8], [19 x i8]* @".str.715", i32 0, i32 0
  %".7" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i8* %"str_ptr.1")
  br label %"ifcont"
ifcont:
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
@".str.623" = internal constant [19 x i8] c"Eres mayor de edad\00"
@".str.715" = internal constant [19 x i8] c"Eres menor de edad\00"