grammar Antrax;

// definicion de la estructura del programa
root: 'Program' 'antrax' '{' stat+ '}' EOF?;

stat:
	varDecl ';'
	| varAsg ';'
	| ifStat ';'
	| whileStat ';'
	| forStat ';'
	| printStat ';'
	| retStat ';'
	| funcStat ';'
	| funcCall ';'
	| tryStat ';'
	;

// estructura de las sentencias de control
ifStat:
	'if' '(' expr ')' '{' ifAction '}' (
		'else' '{' elseAction '}'
	)?;
//tryCatch statement
tryStat: 'try' '{'tryAction'}' 'catch' ID '{' catchAction '}';

//acciones de trycatch
tryAction: stat+;
catchAction: stat+;

// acciones de las sentencias de control
ifAction: stat+;
elseAction: stat+;

// estructura del bloque while 
whileStat: 'while' '(' expr ')' '{' stat+ '}';

// estructura del bloque for
forStat:
	'for' '(' varDecl ';' expr ';' varAsg ')' '{' stat+ '}';

// estructura para funcion para mostrar datos
printStat: 'print' '(' (expr | STRING) ')';

// estructura de una declaración de variable
varDecl: TYPE ID '=' expr;
// reasignacion de variable
varAsg: ID '=' expr;
// estructura de una funcion
funcStat: 'Fx:' TYPE FID '(' params? ')' '{' stat+ '}';
// estructura de los parametros de una funcion
params: (param (',' param)*);
param: TYPE ID;
//sentencia return
retStat: RETURN (STRING | expr);

// llamamos a la funcion
funcCall: FID '(' (expr (',' expr)*)? ')';



// estructura de una expresión ya sea operaciones aritméticas o de comparación booleana
// expr:
// 	expr (MULT | DIV) expr
// 	| expr (PLUS | MINUS) expr
// 	| '(' expr ')'
// 	| NUM
// 	| expr (LT | GT | LEQ | GEQ | EQ | NEQ) expr
// 	| ID
// 	| funcCall
// 	| STRING;

// estructura de una expresión ya sea operaciones aritméticas o de comparación booleana
expr:
	exprBool
	;

exprBool:
	exprAdd ((LT | GT | LEQ | GEQ | EQ | NEQ) exprAdd)*
	;
	
exprAdd
    : exprMul ( (PLUS | MINUS) exprMul )*
    ;

exprMul
    : exprAtom ( (MULT | DIV) exprAtom )*
    ;

exprAtom
    : '(' expr ')'
    | NUM
    | ID
    | funcCall
    | STRING ;

// Definición de tokens
ID: '$' [a-zA-Z_]([a-zA-Z_0-9])*;
FID: '@' [a-zA-Z_]([a-zA-Z_0-9])*;
NUM: [0-9]+ ('.' [0-9]+)?;
STRING: '"' .*? '"';
TYPE: ('int'|'float'|'boolean'|'string'|'void');
RETURN: 'return';

// Operadores aritméticos
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

// Operadores de comparación
LT: '<';
GT: '>';
LEQ: '<=';
GEQ: '>=';
EQ: '==';
NEQ: '!=';

WS: [ \t\r\n]+ -> skip;
COMMENT: '/*' .*? '*/' -> skip;