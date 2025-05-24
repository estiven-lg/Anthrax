; ModuleID = './ll/temp.ll'
source_filename = "./ll/temp.ll"
target triple = "x86_64-pc-linux-gnu"

@fmt = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
define i128 @main() local_unnamed_addr #0 {
entry:
  %.4 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 15)
  %.7 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 35)
  ret i128 0
}

; Function Attrs: nofree nounwind
declare noundef i128 @printf(i8* nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: mustprogress nofree norecurse nosync nounwind readnone willreturn
define i128 @sum(i128 %.1, i128 %.2) local_unnamed_addr #1 {
entry:
  %addtmp = add i128 %.2, %.1
  ret i128 %addtmp
}

attributes #0 = { nofree nounwind }
attributes #1 = { mustprogress nofree norecurse nosync nounwind readnone willreturn }
