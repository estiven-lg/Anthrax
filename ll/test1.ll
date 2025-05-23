; ModuleID = './ll/temp.ll'
source_filename = "./ll/temp.ll"
target triple = "x86_64-pc-linux-gnu"

@fmt = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
define i32 @main() local_unnamed_addr #0 {
entry:
  %.4 = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i32 15)
  %.7 = tail call i32 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i32 35)
  ret i32 0
}

; Function Attrs: nofree nounwind
declare noundef i32 @printf(i8* nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: mustprogress nofree norecurse nosync nounwind readnone willreturn
define i32 @sum(i32 %.1, i32 %.2) local_unnamed_addr #1 {
entry:
  %addtmp = add i32 %.2, %.1
  ret i32 %addtmp
}

attributes #0 = { nofree nounwind }
attributes #1 = { mustprogress nofree norecurse nosync nounwind readnone willreturn }
