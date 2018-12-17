class SymbolTable:
    def __init__(self):
        """
        Creates a new empty symbol table.
        """

    def start_subroutine(self):
        """
        Starts a new subroutine scope (i.e. erases all names in the previous subroutine’s scope.)
        :return:
        """
        return

    def define(self, name, type_, kind):
        """
        Defines a new identifier of a given name, type, and kind and assigns it a running index.
        STATIC and FIELD identifiers have a class scope, while ARG and VAR identifiers have a subroutine scope.
        :param name:
        :param type_:
        :param kind: STATIC, FIELD, ARG, or VAR
        :return:
        """
        return

    def var_count(self, kind):
        """
        Returns the number of variables of the given kind already defined in the current scope
        :param kind: STATIC, FIELD, ARG, or VAR
        :return:
        """
        return

    def 