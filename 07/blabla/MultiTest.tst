// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/StackArithmetic/StackTest/StackTest.tst

load MultiTest.asm,
output-file MultiTest.out,
compare-to MultiTest.cmp,

set RAM[0] 256,
set RAM[1] 4096,
set RAM[2] 4196,
set RAM[3] 4226,
set RAM[4] 4246,

repeat 8000 {
  ticktock;
}

output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[3]%D2.6.2 RAM[4]%D2.6.2 RAM[5]%D2.6.2 RAM[6]%D2.6.2 ;
output;
output-list RAM[7]%D2.6.2 RAM[8]%D2.6.2 RAM[9]%D2.6.2 RAM[10]%D2.6.2 RAM[11]%D2.6.2 RAM[12]%D2.6.2 RAM[16]%D2.6.2;
output;
output-list RAM[17]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2 RAM[259]%D2.6.2 RAM[260]%D2.6.2 ;
output;
output-list RAM[261]%D2.6.2 RAM[262]%D2.6.2 RAM[263]%D2.6.2 RAM[264]%D2.6.2 RAM[265]%D2.6.2 RAM[266]%D2.6.2 RAM[267]%D2.6.2 ;
output;
output-list RAM[268]%D2.6.2 RAM[269]%D2.6.2 RAM[270]%D2.6.2 RAM[271]%D2.6.2 RAM[272]%D2.6.2 RAM[273]%D2.6.2 RAM[274]%D2.6.2 ;
output;
output-list RAM[275]%D2.6.2 RAM[276]%D2.6.2 RAM[277]%D2.6.2 RAM[278]%D2.6.2 RAM[279]%D2.6.2 RAM[280]%D2.6.2 RAM[281]%D2.6.2 ;
output;
output-list RAM[282]%D2.6.2 RAM[283]%D2.6.2 RAM[284]%D2.6.2 RAM[285]%D2.6.2 RAM[286]%D2.6.2 RAM[287]%D2.6.2 RAM[288]%D2.6.2 ;
output;
output-list RAM[289]%D2.6.2 RAM[290]%D2.6.2 RAM[291]%D2.6.2 RAM[292]%D2.6.2 RAM[293]%D2.6.2 RAM[294]%D2.6.2 RAM[295]%D2.6.2 ;
output;
output-list RAM[296]%D2.6.2 RAM[297]%D2.6.2 RAM[298]%D2.6.2 RAM[299]%D2.6.2 RAM[300]%D2.6.2 RAM[301]%D2.6.2 RAM[302]%D2.6.2 ;
output;
output-list RAM[303]%D2.6.2 RAM[304]%D2.6.2 RAM[305]%D2.6.2 RAM[306]%D2.6.2 RAM[307]%D2.6.2 RAM[308]%D2.6.2 RAM[309]%D2.6.2 ;
output;
output-list RAM[310]%D2.6.2 RAM[311]%D2.6.2 RAM[312]%D2.6.2 RAM[313]%D2.6.2 RAM[314]%D2.6.2 RAM[315]%D2.6.2 RAM[316]%D2.6.2 ;
output;
output-list RAM[317]%D2.6.2 RAM[318]%D2.6.2 RAM[319]%D2.6.2 RAM[320]%D2.6.2 RAM[321]%D2.6.2 RAM[322]%D2.6.2 RAM[323]%D2.6.2 ;
output;
output-list RAM[324]%D2.6.2 RAM[325]%D2.6.2 RAM[326]%D2.6.2 RAM[327]%D2.6.2 RAM[328]%D2.6.2 RAM[329]%D2.6.2 RAM[330]%D2.6.2 ;
output;
output-list RAM[331]%D2.6.2 RAM[332]%D2.6.2 RAM[333]%D2.6.2 RAM[334]%D2.6.2 RAM[335]%D2.6.2 RAM[336]%D2.6.2 RAM[337]%D2.6.2 ;
output;
output-list RAM[338]%D2.6.2 RAM[339]%D2.6.2 RAM[340]%D2.6.2 RAM[341]%D2.6.2 RAM[342]%D2.6.2 ;
output;
output-list RAM[345]%D2.6.2 RAM[4096]%D2.6.2 RAM[4097]%D2.6.2 RAM[4098]%D2.6.2 RAM[4099]%D2.6.2 RAM[4196]%D2.6.2 RAM[4197]%D2.6.2 ;
output;
output-list RAM[4198]%D2.6.2 RAM[4199]%D2.6.2 RAM[4226]%D2.6.2 RAM[4227]%D2.6.2 RAM[4228]%D2.6.2 RAM[4229]%D2.6.2 RAM[5000]%D2.6.2 ;
output;
output-list RAM[5001]%D2.6.2 RAM[5002]%D2.6.2 RAM[5003]%D2.6.2 RAM[5010]%D2.6.2 RAM[5011]%D2.6.2 RAM[5012]%D2.6.2 RAM[5013]%D2.6.2 ;
output;
