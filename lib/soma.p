 program Soma_Pares;
 uses crt;
 var
  superior, soma, num: integer;
 begin
  soma:=0;
  write ('Entre com o limite superior');
  readln (superior);
  num:=2;

  repeat
 soma:=soma+num;
 num:=num+2;
  until (num > superior);

  writeln('A soma dos números pares de 2 até ', superior,' é ', soma);
  readln;
 end.