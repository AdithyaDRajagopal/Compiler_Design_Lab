#include <stdio.h>
#include "p2.h"

extern int yylex();
extern int yylineno;
extern char* yytext;

void main()
{
 int token;
 token=yylex();
 while(token)
 {
  printf("Token : %d\tValue : %s\n",ntoken,yytext);
  token=yylex();
 }
}
