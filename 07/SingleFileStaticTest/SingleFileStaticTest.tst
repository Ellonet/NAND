// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/07/StackArithmetic/StackTest/StackTest.tst

load SingleFileStaticTest.asm,
output-file SingleFileStaticTest.out,
compare-to SingleFileStaticTest.cmp,

set RAM[0] 256,


repeat 6000 {
  ticktock;
}

output-list RAM[0]%D2.6.2;
output;
output-list RAM[16]%D2.6.2 RAM[17]%D2.6.2 RAM[18]%D2.6.2 RAM[19]%D2.6.2 RAM[20]%D2.6.2 RAM[21]%D2.6.2 RAM[22]%D2.6.2 ;
output;
output-list RAM[23]%D2.6.2 RAM[24]%D2.6.2 RAM[25]%D2.6.2 RAM[26]%D2.6.2 RAM[27]%D2.6.2 RAM[28]%D2.6.2 RAM[29]%D2.6.2 ;
output;
output-list RAM[30]%D2.6.2 RAM[31]%D2.6.2 RAM[32]%D2.6.2 RAM[33]%D2.6.2 RAM[34]%D2.6.2 RAM[35]%D2.6.2 RAM[36]%D2.6.2 ;
output;
output-list RAM[37]%D2.6.2 RAM[38]%D2.6.2 RAM[39]%D2.6.2 RAM[40]%D2.6.2 RAM[41]%D2.6.2 RAM[42]%D2.6.2 RAM[43]%D2.6.2 ;
output;
output-list RAM[44]%D2.6.2 RAM[45]%D2.6.2 RAM[46]%D2.6.2 RAM[47]%D2.6.2 RAM[48]%D2.6.2 RAM[49]%D2.6.2 RAM[50]%D2.6.2 ;
output;
output-list RAM[51]%D2.6.2 RAM[52]%D2.6.2 RAM[53]%D2.6.2 RAM[54]%D2.6.2 RAM[55]%D2.6.2 RAM[56]%D2.6.2 RAM[57]%D2.6.2 ;
output;
output-list RAM[58]%D2.6.2 RAM[59]%D2.6.2 RAM[60]%D2.6.2 RAM[61]%D2.6.2 RAM[62]%D2.6.2 RAM[63]%D2.6.2 RAM[64]%D2.6.2 ;
output;
output-list RAM[65]%D2.6.2 RAM[66]%D2.6.2 RAM[67]%D2.6.2 RAM[68]%D2.6.2 RAM[69]%D2.6.2 RAM[70]%D2.6.2 RAM[71]%D2.6.2 ;
output;
output-list RAM[72]%D2.6.2 RAM[73]%D2.6.2 RAM[74]%D2.6.2 RAM[75]%D2.6.2 RAM[76]%D2.6.2 RAM[77]%D2.6.2 RAM[78]%D2.6.2 ;
output;
output-list RAM[79]%D2.6.2 RAM[80]%D2.6.2 RAM[81]%D2.6.2 RAM[82]%D2.6.2 RAM[83]%D2.6.2 RAM[84]%D2.6.2 RAM[85]%D2.6.2 ;
output;
output-list RAM[86]%D2.6.2 RAM[87]%D2.6.2 RAM[88]%D2.6.2 RAM[89]%D2.6.2 RAM[90]%D2.6.2 RAM[91]%D2.6.2 RAM[92]%D2.6.2 ;
output;
output-list RAM[93]%D2.6.2 RAM[94]%D2.6.2 RAM[95]%D2.6.2 RAM[96]%D2.6.2 RAM[97]%D2.6.2 RAM[98]%D2.6.2 RAM[99]%D2.6.2 ;
output;
output-list RAM[100]%D2.6.2 RAM[101]%D2.6.2 RAM[102]%D2.6.2 RAM[103]%D2.6.2 RAM[104]%D2.6.2 RAM[105]%D2.6.2 RAM[106]%D2.6.2 ;
output;
output-list RAM[107]%D2.6.2 RAM[108]%D2.6.2 RAM[109]%D2.6.2 RAM[110]%D2.6.2 RAM[111]%D2.6.2 RAM[112]%D2.6.2 RAM[113]%D2.6.2 ;
output;
output-list RAM[114]%D2.6.2 RAM[115]%D2.6.2 RAM[116]%D2.6.2 RAM[117]%D2.6.2 RAM[118]%D2.6.2 RAM[119]%D2.6.2 RAM[120]%D2.6.2 ;
output;
output-list RAM[121]%D2.6.2 RAM[122]%D2.6.2 RAM[123]%D2.6.2 RAM[124]%D2.6.2 RAM[125]%D2.6.2 RAM[126]%D2.6.2 RAM[127]%D2.6.2 ;
output;
output-list RAM[128]%D2.6.2 RAM[129]%D2.6.2 RAM[130]%D2.6.2 RAM[131]%D2.6.2 RAM[132]%D2.6.2 RAM[133]%D2.6.2 RAM[134]%D2.6.2 ;
output;
output-list RAM[135]%D2.6.2 RAM[136]%D2.6.2 RAM[137]%D2.6.2 RAM[138]%D2.6.2 RAM[139]%D2.6.2 RAM[140]%D2.6.2 RAM[141]%D2.6.2 ;
output;
output-list RAM[142]%D2.6.2 RAM[143]%D2.6.2 RAM[144]%D2.6.2 RAM[145]%D2.6.2 RAM[146]%D2.6.2 RAM[147]%D2.6.2 RAM[148]%D2.6.2 ;
output;
output-list RAM[149]%D2.6.2 RAM[150]%D2.6.2 RAM[151]%D2.6.2 RAM[152]%D2.6.2 RAM[153]%D2.6.2 RAM[154]%D2.6.2 RAM[155]%D2.6.2 ;
output;
output-list RAM[156]%D2.6.2 RAM[157]%D2.6.2 RAM[158]%D2.6.2 RAM[159]%D2.6.2 RAM[160]%D2.6.2 RAM[161]%D2.6.2 RAM[162]%D2.6.2 ;
output;
output-list RAM[163]%D2.6.2 RAM[164]%D2.6.2 RAM[165]%D2.6.2 RAM[166]%D2.6.2 RAM[167]%D2.6.2 RAM[168]%D2.6.2 RAM[169]%D2.6.2 ;
output;
output-list RAM[170]%D2.6.2 RAM[171]%D2.6.2 RAM[172]%D2.6.2 RAM[173]%D2.6.2 RAM[174]%D2.6.2 RAM[175]%D2.6.2 RAM[176]%D2.6.2 ;
output;
output-list RAM[177]%D2.6.2 RAM[178]%D2.6.2 RAM[179]%D2.6.2 RAM[180]%D2.6.2 RAM[181]%D2.6.2 RAM[182]%D2.6.2 RAM[183]%D2.6.2 ;
output;
output-list RAM[184]%D2.6.2 RAM[185]%D2.6.2 RAM[186]%D2.6.2 RAM[187]%D2.6.2 RAM[188]%D2.6.2 RAM[189]%D2.6.2 RAM[190]%D2.6.2 ;
output;
output-list RAM[191]%D2.6.2 RAM[192]%D2.6.2 RAM[193]%D2.6.2 RAM[194]%D2.6.2 RAM[195]%D2.6.2 RAM[196]%D2.6.2 RAM[197]%D2.6.2 ;
output;
output-list RAM[198]%D2.6.2 RAM[199]%D2.6.2 RAM[200]%D2.6.2 RAM[201]%D2.6.2 RAM[202]%D2.6.2 RAM[203]%D2.6.2 RAM[204]%D2.6.2 ;
output;
output-list RAM[205]%D2.6.2 RAM[206]%D2.6.2 RAM[207]%D2.6.2 RAM[208]%D2.6.2 RAM[209]%D2.6.2 RAM[210]%D2.6.2 RAM[211]%D2.6.2 ;
output;
output-list RAM[212]%D2.6.2 RAM[213]%D2.6.2 RAM[214]%D2.6.2 RAM[215]%D2.6.2 RAM[216]%D2.6.2 RAM[217]%D2.6.2 RAM[218]%D2.6.2 ;
output;
output-list RAM[219]%D2.6.2 RAM[220]%D2.6.2 RAM[221]%D2.6.2 RAM[222]%D2.6.2 RAM[223]%D2.6.2 RAM[224]%D2.6.2 RAM[225]%D2.6.2 ;
output;
output-list RAM[226]%D2.6.2 RAM[227]%D2.6.2 RAM[228]%D2.6.2 RAM[229]%D2.6.2 RAM[230]%D2.6.2 RAM[231]%D2.6.2 RAM[232]%D2.6.2 ;
output;
output-list RAM[233]%D2.6.2 RAM[234]%D2.6.2 RAM[235]%D2.6.2 RAM[236]%D2.6.2 RAM[237]%D2.6.2 RAM[238]%D2.6.2 RAM[239]%D2.6.2 ;
output;
output-list RAM[240]%D2.6.2 RAM[241]%D2.6.2 RAM[242]%D2.6.2 RAM[243]%D2.6.2 RAM[244]%D2.6.2 RAM[245]%D2.6.2 RAM[246]%D2.6.2 ;
output;
output-list RAM[247]%D2.6.2 RAM[248]%D2.6.2 RAM[249]%D2.6.2 RAM[250]%D2.6.2 RAM[251]%D2.6.2 RAM[252]%D2.6.2 RAM[253]%D2.6.2 ;
output;
output-list RAM[254]%D2.6.2 RAM[255]%D2.6.2 RAM[256]%D2.6.2 RAM[257]%D2.6.2 RAM[258]%D2.6.2 RAM[259]%D2.6.2 RAM[260]%D2.6.2 ;
output;
output-list RAM[261]%D2.6.2 RAM[262]%D2.6.2 RAM[263]%D2.6.2 RAM[264]%D2.6.2 ;
output;

