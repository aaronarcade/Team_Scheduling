\ Model assignment
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  -0 t1 + -0 t2 + x[Amy,T2] + 2 x[Bob,T1] + x[Amy,T1] + 3 x[Cat,T2]
Subject To
 p1: w1 <= 1
 p2: w2 <= 1
 p3: w3 <= 1
 p4: w4 <= 1
 p4: w4 <= 1
 T1: x[Bob,T1] + x[Amy,T1] <= 2
 T2: x[Amy,T2] + x[Cat,T2] <= 2
Bounds
 x[Amy,T2] <= 1
 x[Bob,T1] <= 1
 x[Amy,T1] <= 1
 x[Cat,T2] <= 1
End
