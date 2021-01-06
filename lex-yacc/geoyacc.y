%{
	#include<stdio.h>
	#include<stdlib.h>
	#define YYDEBUG1
}%


%token LET
%token FUNC
%token RETURNS
%token IS
%token OR
%token PRINT
%token WHILE
%token RETURN
%token IF
%token ELSE
%token THEN
%token INTEGER
%token BOOLEAN
%token TRUE
%token STRING
%token CHAR
%token FALSE
%token SCAN
%token PRINT
%token IDENTIFIER
%token CONSTANT
%token RELATION
%token COMMA
%token SEMI_COLON
%token OPEN_SQUARE_BRACKET
%token CLOSED_SQUARE_BRACKET
%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token PLUS
%token MINUS
%token DIV
%token MUL
%token PERCENT
%token EQ
%token NOT_EQ

%start program

%% 

program: LET FUNC IDENTIFIER function_arguments RETURNS type OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET SEMI_COLON
	;
type: INTEGER 
	| BOOLEAN
	| STRING
	| CHAR
	;
statement_list: statement
	| statemenet_list
	;
statement: simple_declaration
	| assigned_declaration
	| assignment
	| if_statemenet
	| while_statement
	| output_statement
	| input_statement
	;
simple_declaration: LET type IDENTIFIER SEMI_COLON;
assigned_declaration: LET IDENTIFIER EQ expression SEMI_COLON;
assignment: IDENTIFIER EQ expression SEMI_COLON;
function_arguments: OPEN_ROUND_BRACKET type IDENTIFIER CLOSED_ROUND_BRACKET;
if_statement: IF condition THEN OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET ELSE 
	OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET;
while_statement: WHILE condition THEN OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET;
condition: OPEN_ROUND_BRACKET expression RELATION expression CLOSED_ROUND_BRACKET;
expression: IDENTIFIER operand IDENTIFIER
	| IDENTIFIER operand CONSTANT
	| CONSTANT operand IDENTIFIER
	| CONSTANT operand CONSTANT
	;
operand: PLUS 
	| MINUS
	| DIV
	| MUL
	| PERCENT
	;
output_statement: PRINT STRING SEMI_COLON
	| print IDENTIFIER SEMI_COLON
	;
input_statement: SCAN type IDENTIFIER SEMI_COLON;


%%