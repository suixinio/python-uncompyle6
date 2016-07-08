#  Copyright (c) 2016 Rocky Bernstein
"""
spark grammar differences over Python2.6 for Python 2.6.
"""

from uncompyle6.parser import PythonParserSingle
from spark_parser import DEFAULT_DEBUG as PARSER_DEFAULT_DEBUG
from uncompyle6.parsers.parse26 import Python26Parser

class Python25Parser(Python26Parser):
    def __init__(self, debug_parser=PARSER_DEFAULT_DEBUG):
        super(Python25Parser, self).__init__(debug_parser)
        self.customized = {}

    def p_misc(self, args):
        '''

        # If "return_if_stmt" is in a loop, a JUMP_BACK can be emitted. In 2.6 the
        # JUMP_BACK doesn't appear

        return_if_stmt ::= ret_expr  RETURN_END_IF JUMP_BACK

        # Pyython 2.6 uses ROT_TWO instead of the STORE_FAST
        setupwithas ::= DUP_TOP LOAD_ATTR STORE_FAST LOAD_ATTR CALL_FUNCTION_0 STORE_FAST
                        SETUP_FINALLY LOAD_FAST DELETE_FAST

        # Python 2.6 omits ths LOAD_FAST DELETE_FAST below
        withasstmt ::= expr setupwithas designator suite_stmts_opt
                       POP_BLOCK LOAD_CONST COME_FROM
                       LOAD_FAST DELETE_FAST
                       WITH_CLEANUP END_FINALLY


        '''

class Python25ParserSingle(Python26Parser, PythonParserSingle):
    pass

if __name__ == '__main__':
    # Check grammar
    p = Python26Parser()
    p.checkGrammar()
