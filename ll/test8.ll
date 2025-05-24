; ModuleID = './ll/temp.ll'
source_filename = "./ll/temp.ll"
target triple = "x86_64-pc-linux-gnu"

@.str.917 = internal constant [2 x i8] c"A\00"

; Function Attrs: nofree nounwind
define i128 @main() local_unnamed_addr #0 {
entry:
  %puts = tail call i32 @puts(i8* nonnull dereferenceable(1) getelementptr inbounds ([2 x i8], [2 x i8]* @.str.917, i64 0, i64 0))
  ret i128 0
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(i8* nocapture noundef readonly) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
