program learn;
uses crt;
var a,b,c,e,f,right: integer; d:real;
label 1,2,3,4,5;
begin
textbackground(green);
textcolor(white);
clrscr;
repeat
inc(f);
until f=100000;
randomize;
1:
e:=random(3)+1;
b:=random(200)+1;
c:=random(200)+1;
if e=1 then d:=b+c;
if e=2 then d:=b-c;
if e=3 then d:=b*c;
writeln('  ',b:3);
if e=1 then write('+ ');  
if e=2 then write('- ');
if e=3 then write('x ');
writeln(c:3);
writeln('______');
readln(a);
if a=d then
begin                                       
inc(right);
writeln('HORRAY! YOU GOT IT RIGHT! you have ',right,' points!');
end
else
begin
right:=right-1;
writeln('WRONG! you have ',right,' points');
end;
goto 1;
end.