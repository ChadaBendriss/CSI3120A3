class Symbol:
    def __init__(self):
        self.type = ""
        self.name = ""
        self.value = ""


class SymbolTable:
    def __init__(self):
        self.symbols = [Symbol() for _ in range(MAX_SYMBOLS)]

# Represents a node in a linked list structure, each node effectively representing a scope with its own symbol table
# next: Pointer to the next node in the linked list 
# count: Tracks the number of symbols currently in the node's symbol table
# symbolTable: An instance of SymbolTable containing symbols relevant to this scope
class Node:
    def __init__(self):
        # To be completed
        self.next = None
        self.count = 0
        self.symbolTable = SymbolTable()

    # Creates a new Node and links it to the current scope  
    def push_scope(self):
        # To be completed
        nnode = Node()
        nnode.next = self
        return nnode

    # Removes the current scope and returns the next scope
    def pop_scope(self):
        # To be completed
        if self is not None:
            return self.next
        else:
            return self
    
    # Prints all symbols in the current scope
    def print_current_scope(self):
        # To be completed
        if self is not None:
            i=0
            while i<self.count:
                symbolofi = self.symbolTable.symbols[i]
                print(symbolofi.name + " "+ symbolofi.value)
                i+=1
        else:
            return None

    # Prints all symbols in all scopes, starting from the current one
    def print_all_scopes(self):
        # To be completed
        current = self
        while current is not None:
            i=0
            while i<current.count:
                symbolofi = current.symbolTable.symbols[i]
                print(symbolofi.name + " "+ symbolofi.value)
                i+=1
            current = current.next

    # Inserts a new symbol into the current node's symbol table
    def insert_symbol(self, symbol_type, symbol_name, symbol_value):
        # To be completed
        if self.count < 100:
            symbolofi = self.symbolTable.symbols[self.count]
            symbolofi.type = symbol_type
            symbolofi.name = symbol_name
            symbolofi.value = symbol_value
            
            self.count += 1
        else:
           return None
    
    # Checks if a symbol exists in any scope, starting from the current and moving upwards
    def symbol_exists(self, name):
        # To be completed
        currentNode = self
        while currentNode is not None:
            i=0
            while i<currentNode.count:
                symbolofi=currentNode.symbolTable.symbols[i]
                if symbolofi.name == name:
                    return symbolofi
                i+=1
            currentNode = currentNode.next
        return None
    
    # Checks if a symbol exists in the current scope
    def symbol_existsInCurrent(self, name):
        # To be completed
        i=0
        while i<self.count:
            symbolofi=self.symbolTable.symbols[i]
            if symbolofi.name == name:
                return symbolofi
            i+=1
        return None

# A utility function to delete all nodes in the linked list, effectively clearing the environment
def free_environment(head):
    # To be completed
    while head is not None:
        head = head.next
  


MAX_SYMBOLS = 100


