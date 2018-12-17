class SymbolTable:
    def __init__(self):
        """
        Creates a new empty symbol table.
        we use two separate hash tables to implement the symbol table: one for the class-scope
        and another one for the subroutine-scope. When a new subroutine is started,
        the subroutine-scope table should be cleared.
        """
        self.class_symbol_table = {}
        self.subroutine_symbol_table = {}

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

    def kind_of(self, name):
        """
        Returns the kind of the named identifier in the current scope. Returns NONE if the
        identifier is unknown in the current scope.
        :param name:
        :return: STATIC, FIELD, ARG, VAR, NONE
        """
        return

    def type_of(self, name):
        """
        Returns the type of the named identifier in the current scope.
        :param name:
        :return:
        """
        return

    def index_of(self, name):
        """
        Returns the index assigned to named identifier.
        :param name:
        :return:
        """
        return
