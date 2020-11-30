%{
  #include <stdio.h>
  #include <string.h>
  #include "y.tab.h"
%}

identifier [a-zA-Z][_a-zA-Z0-9]*
number [0-9]+

%%

main\(\) return MAIN;
if return IF;
else return ELSE;
while return WHILE;
int|char|float return TYPE;
{identifier} {strcpy(yylval.var,yytext); return VAR;}
{number} {strcpy(yylval.var,yytext); return NUM;}
\<|\>|\>=|\<=|== {strcpy(yylval.var,yytext); return RELOP;}
[\t] ;
[\n] {yylineno++;}
. return yytext[0];

%%

int yywrap(void)
{
 return 1;
}
