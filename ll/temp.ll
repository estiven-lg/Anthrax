; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i128 @"main"()
{
entry:
  %"$password" = alloca i128
  store i128 123554, i128* %"$password"
  %"$password.1" = load i128, i128* %"$password"
  %"cmpeqtmp" = icmp eq i128 %"$password.1", 1234
  br i1 %"cmpeqtmp", label %"then", label %"else"
then:
  %"str_ptr" = getelementptr [17 x i8], [17 x i8]* @".str.956", i128 0, i128 0
  %".4" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".5" = call i128 (i8*, ...) @"printf"(i8* %".4", i8* %"str_ptr")
  br label %"ifcont"
else:
  %"str_ptr.1" = getelementptr [16 x i8], [16 x i8]* @".str.592", i128 0, i128 0
  %".7" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".8" = call i128 (i8*, ...) @"printf"(i8* %".7", i8* %"str_ptr.1")
  %"str_ptr.2" = getelementptr [26 x i8], [26 x i8]* @".str.42", i128 0, i128 0
  %".9" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".10" = call i128 (i8*, ...) @"printf"(i8* %".9", i8* %"str_ptr.2")
  br label %"ifcont"
ifcont:
  ret i128 0
}

declare i128 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
@"float_format" = internal constant [3 x i8] c"%f\00"
@".str.956" = internal constant [17 x i8] c"Acceso concedido\00"
@".str.592" = internal constant [16 x i8] c"Acceso denegado\00"
@".str.42" = internal constant [26 x i8] c"Verifica tus credenciales\00"