%{
  #include<stdio.h>
  #include<stdlib.h>
  void yyerror();
  int yylex();
%}

%start stmt
%token ID NUM
%left '+' '-' '*' '/'

%%

stmt : expr | ID '=' expr ;

expr : expr '+' expr
     | expr '-' expr
     | expr '*' expr
     | expr '/' expr
     | '(' expr ')'
     | ID
     | NUM ;

%%

void main()
{
 printf("Enter an expression : ");
 yyparse();
 printf("Valid Expression Identified\n");
}

void yyerror()
{
 printf("Expression Invalid\n");
 exit(0);
}
