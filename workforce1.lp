\ Model assignment
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  x[Amy,T2] + 2 x[Bob,T1] + x[Amy,T1]
Subject To
 T1: x[Bob,T1] + x[Amy,T1] <= 2
 T2: x[Amy,T2] <= 2
Bounds
 x[Amy,T2] <= 1
 x[Bob,T1] <= 1
 x[Amy,T1] <= 1
End
