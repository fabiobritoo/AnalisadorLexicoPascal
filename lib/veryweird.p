program veryweird;
uses crt;
type aaa=array[1..40,1..12] of char;
var a,b,c,d,e,pa,pd:integer; f:aaa; g:char;
label 1,2,3,4;
begin
pa:=1;
pd:=1;
writeln('hello');
writeln('press the arrow keys to move');
2:
IF KeyPressed THEN
BEGIN
g:=readkey;
CASE g OF
'H' :
begin
if pd=1 then goto 2; 
f[pa,pd]:='_';
pd:=pd-1;
f[pa,pd]:='@';
end;       
'K' :
begin
if pa=1 then goto 2;
f[pa,pd]:='_';
pa:=pa-1;
f[pa,pd]:='@';
end;
'M' :
begin
if pa=40 then goto 2;
f[pa,pd]:='_';
pa:=pa+1;
f[pa,pd]:='@';
end;
'P' :
begin
if pd=12 then goto 2;
f[pa,pd]:='_';
pd:=pd+1;
f[pa,pd]:='@';
end;
end;
clrscr;
for a:=1 to 12 do writeln(f[1,a],f[2,a],f[3,a],f[4,a],f[5,a],f[6,a],f[7,a],f[8,a],f[9,a],f[10,a],f[11,a],f[12,a],f[13,a],f[14,a],f[15,a],f[16,a],f[17,a],f[18,a],f[19,a],f[20,a],f[21,a],f[22,a],f[23,a],f[24,a],f[25,a],f[26,a],f[27,a],f[28,a],f[29,a],f[30,a],f[31,a],f[32,a],f[33,a],f[34,a],f[35,a],f[36,a],f[37,a],f[38,a],f[39,a],f[40,a]);
goto 2;
end
else goto 2;
end.