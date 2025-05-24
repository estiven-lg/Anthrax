; ModuleID = './ll/temp.ll'
source_filename = "./ll/temp.ll"
target triple = "x86_64-pc-linux-gnu"

@fmt = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
define i128 @main() local_unnamed_addr #0 {
entry:
  %.5 = tail call i128 @fib(i128 0)
  %.7 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5)
  %.5.1 = tail call i128 @fib(i128 1)
  %.7.1 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.1)
  %.5.2 = tail call i128 @fib(i128 2)
  %.7.2 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.2)
  %.5.3 = tail call i128 @fib(i128 3)
  %.7.3 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.3)
  %.5.4 = tail call i128 @fib(i128 4)
  %.7.4 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.4)
  %.5.5 = tail call i128 @fib(i128 5)
  %.7.5 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.5)
  %.5.6 = tail call i128 @fib(i128 6)
  %.7.6 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.6)
  %.5.7 = tail call i128 @fib(i128 7)
  %.7.7 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.7)
  %.5.8 = tail call i128 @fib(i128 8)
  %.7.8 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.8)
  %.5.9 = tail call i128 @fib(i128 9)
  %.7.9 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 %.5.9)
  ret i128 0
}

; Function Attrs: nofree nounwind
declare noundef i128 @printf(i8* nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nosync nounwind readnone
define i128 @fib(i128 %.1) local_unnamed_addr #1 {
entry:
  %cmpletmp4 = icmp slt i128 %.1, 2
  br i1 %cmpletmp4, label %common.ret, label %ifcont

common.ret:                                       ; preds = %ifcont, %entry
  %accumulator.tr.lcssa = phi i128 [ 0, %entry ], [ %addtmp, %ifcont ]
  %.1.tr.lcssa = phi i128 [ %.1, %entry ], [ %subtmp.1, %ifcont ]
  %accumulator.ret.tr = add i128 %.1.tr.lcssa, %accumulator.tr.lcssa
  ret i128 %accumulator.ret.tr

ifcont:                                           ; preds = %entry, %ifcont
  %.1.tr6 = phi i128 [ %subtmp.1, %ifcont ], [ %.1, %entry ]
  %accumulator.tr5 = phi i128 [ %addtmp, %ifcont ], [ 0, %entry ]
  %subtmp = add nsw i128 %.1.tr6, -1
  %.6 = tail call i128 @fib(i128 %subtmp)
  %subtmp.1 = add nsw i128 %.1.tr6, -2
  %addtmp = add i128 %.6, %accumulator.tr5
  %cmpletmp = icmp ult i128 %.1.tr6, 4
  br i1 %cmpletmp, label %common.ret, label %ifcont
}

attributes #0 = { nofree nounwind }
attributes #1 = { nofree nosync nounwind readnone }
