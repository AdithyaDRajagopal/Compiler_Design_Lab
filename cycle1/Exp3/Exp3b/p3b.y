%{
  #include<stdio.h>
  #include<stdlib.h>
  void yyerror();
  int yylex();
%}

%start stmt
%token ID

%%

stmt : ID;

%%

void main()
{
 printf("Enter an expression : ");
 yyparse();
 printf("Valid Identifier\n");
}

void yyerror()
{
 printf("Invalid Identifier\n");
 exit(0);
}
