; ModuleID = "AntraxModule"
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"$password" = alloca i32
  store i32 123554, i32* %"$password"
  %"$password.1" = load i32, i32* %"$password"
  %"cmpeqtmp" = icmp eq i32 %"$password.1", 1234
  br i1 %"cmpeqtmp", label %"then", label %"else"
then:
  %"str_ptr" = getelementptr [17 x i8], [17 x i8]* @".str.701", i32 0, i32 0
  %".4" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i8* %"str_ptr")
  br label %"ifcont"
else:
  %"str_ptr.1" = getelementptr [16 x i8], [16 x i8]* @".str.633", i32 0, i32 0
  %".7" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i8* %"str_ptr.1")
  %"str_ptr.2" = getelementptr [26 x i8], [26 x i8]* @".str.458", i32 0, i32 0
  %".9" = bitcast [4 x i8]* @"fmt_str" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i8* %"str_ptr.2")
  br label %"ifcont"
ifcont:
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fmt" = internal constant [4 x i8] c"%d\0a\00"
@"fmt_str" = internal constant [4 x i8] c"%s\0a\00"
@".str.701" = internal constant [17 x i8] c"Acceso concedido\00"
@".str.633" = internal constant [16 x i8] c"Acceso denegado\00"
@".str.458" = internal constant [26 x i8] c"Verifica tus credenciales\00"