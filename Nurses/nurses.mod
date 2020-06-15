var X1 integer;
var X2 integer;
var X3 integer;
var X4 integer;
var X5 integer;
var X6 integer;
var X7 integer;
param d1 ;
param d2 ;
param d3 ;
param d4 ;
param d5 ;
param d6 ;
param d7 ;
minimize tsum : X1 + X2 + X3 + X4 + X5 + X6 + X7;
subject to cond1 : X1 + X4 + X5 + X6 + X7 >= d1;
subject to cond2 : X1 + X2 + X5 + X6 + X7 >= d2;
subject to cond3 : X1 + X2 + X3 + X6 + X7 >= d3;
subject to cond4 : X1 + X2 + X3 + X4 + X7 >= d4;
subject to cond5 : X1 + X2 + X3 + X4 + X5 >= d5;
subject to cond6 : X2 + X3 + X4 + X5 + X6 >= d6;
subject to cond7 : X3 + X4 + X5 + X6 + X7 >= d7;
subject to limit1 : X1 >= 0;
subject to limit2 : X2 >= 0;
subject to limit3 : X3 >= 0;
subject to limit4 : X4 >= 0;
subject to limit5 : X5 >= 0;
subject to limit6 : X6 >= 0;
subject to limit7 : X7 >= 0;