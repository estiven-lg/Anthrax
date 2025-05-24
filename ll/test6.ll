; ModuleID = './ll/temp.ll'
source_filename = "./ll/temp.ll"
target triple = "x86_64-pc-linux-gnu"

@fmt = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
define i128 @main() local_unnamed_addr #0 {
entry:
  %.6 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 10)
  %.6.1 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 9)
  %.6.2 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 8)
  %.6.3 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 7)
  %.6.4 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 6)
  %.6.5 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 5)
  %.6.6 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 4)
  %.6.7 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 3)
  %.6.8 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 2)
  %.6.9 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 1)
  ret i128 0
}

; Function Attrs: nofree nounwind
declare noundef i128 @printf(i8* nocapture noundef readonly, ...) local_unnamed_addr #0

attributes #0 = { nofree nounwind }
