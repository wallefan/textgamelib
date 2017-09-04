"""Welcome to TextGameLib, your go-to library for making text-based games!"""

import shlex

KEY=0
VALUE=1

class ParseError(Exception):
    "Raised in lieu of SyntaxError by the parser.  Strings always start with an Emacs-friendly error leader."

def load(file):
    lexer=shlex.shlex(file)
    lexer.comment = '#'
    lexer.source = 'include'
    namespace = {}
    key = None
    state = KEY
    ...
    for token in lexer:
        if token==':':
            if state==KEY:
                state=VALUE
            else:
                raise ParseError(lexer.error_leader() + 
            
 # TODO FINISH ME
