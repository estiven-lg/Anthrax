; ModuleID = './ll/temp.ll'
source_filename = "./ll/temp.ll"
target triple = "x86_64-pc-linux-gnu"

@fmt = internal constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
define i128 @main() local_unnamed_addr #0 {
entry:
  %.4 = tail call i128 (i8*, ...) @printf(i8* nonnull dereferenceable(1) getelementptr inbounds ([4 x i8], [4 x i8]* @fmt, i64 0, i64 0), i128 15511210043330985984000000)
  ret i128 0
}

; Function Attrs: nofree nounwind
declare noundef i128 @printf(i8* nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nosync nounwind readnone
define i128 @factoria(i128 %.1) local_unnamed_addr #1 {
entry:
  %cmpeqtmp3 = icmp eq i128 %.1, 0
  br i1 %cmpeqtmp3, label %common.ret, label %ifcont

common.ret:                                       ; preds = %ifcont, %entry
  %accumulator.tr.lcssa = phi i128 [ 1, %entry ], [ %multmp, %ifcont ]
  ret i128 %accumulator.tr.lcssa

ifcont:                                           ; preds = %entry, %ifcont
  %.1.tr5 = phi i128 [ %subtmp, %ifcont ], [ %.1, %entry ]
  %accumulator.tr4 = phi i128 [ %multmp, %ifcont ], [ 1, %entry ]
  %subtmp = add i128 %.1.tr5, -1
  %multmp = mul i128 %.1.tr5, %accumulator.tr4
  %cmpeqtmp = icmp eq i128 %subtmp, 0
  br i1 %cmpeqtmp, label %common.ret, label %ifcont
}

attributes #0 = { nofree nounwind }
attributes #1 = { nofree nosync nounwind readnone }
