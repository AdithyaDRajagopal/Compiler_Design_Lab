%{
  #include <stdio.h>
  #include <stdlib.h>
  #include "p2.h"
%}

letter [a-zA-Z]
digit [0-9]
id {letter}*|({letter}{digit})+
notid ({digit}{letter})+

%%

prog|integer|begin|read|if|then|endif|while|do|endwhile|write|end return KEYWORD;
{id} return IDENTIFIER;
":=" return ASSIGN_OP;
"<" return LT;
">" return GT;
">=" return GTE;
"<=" return LTE;
[1-9][0-9]* return DIGIT;
";" return SEMICOLON;
"+" return ADD_OP;
"-" return SUB_OP;
"*" return MUL_OP;
"/" return DIV_OP;
"=" return EQU_OP;
[{,},(,)] return LITERAL;
"." return DOT;
{notid} {printf("Invalid identifier %s in line %d\n",yytext,yylineno);exit(0);}
[\n] {yylineno++;}
[\t] ;

%%

int yywrap(void)
{
 return 1;
}
