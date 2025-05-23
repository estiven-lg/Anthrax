; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"$score" = alloca i32
  store i32 900, i32* %"$score"
  %"$score.1" = load i32, i32* %"$score"
  %"cmpgetmp" = icmp sge i32 %"$score.1", 90
  br i1 %"cmpgetmp", label %"then", label %"else"
then:
  %"str_ptr" = getelementptr [2 x i8], [2 x i8]* @".str.787", i32 0, i32 0
  %".4" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8* %"str_ptr")
  br label %"ifcont"
else:
  %"$score.2" = load i32, i32* %"$score"
  %"cmpgetmp.1" = icmp sge i32 %"$score.2", 80
  br i1 %"cmpgetmp.1", label %"then.1", label %"else.1"
ifcont:
  ret i32 0
then.1:
  %"str_ptr.1" = getelementptr [2 x i8], [2 x i8]* @".str.488", i32 0, i32 0
  %".8" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i8* %"str_ptr.1")
  br label %"ifcont.1"
else.1:
  %"str_ptr.2" = getelementptr [10 x i8], [10 x i8]* @".str.582", i32 0, i32 0
  %".11" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i8* %"str_ptr.2")
  br label %"ifcont.1"
ifcont.1:
  br label %"ifcont"
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
@".str.787" = internal constant [2 x i8] c"A\00"
@".str.488" = internal constant [2 x i8] c"B\00"
@".str.582" = internal constant [10 x i8] c"C o menor\00"