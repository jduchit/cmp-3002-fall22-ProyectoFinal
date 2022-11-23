class Node:
    """
    Implementation of a node
    """
    def __init__(self, val=None):
        self.val = val
        self.next_node = None
        self.prev_node = None

class Doubly_linked_list:
    """
    Implementation of a singly linked list
    """
    def __init__(self, head_node=None):
        self.head_node = head_node
        
    
    def list_traversed(self):
        node = self.head_node
        while node:
            print(node.val)
            node = node.next_node
            
    def insert_at_start(self, data):
        """
        Insert a node at the start of the list
        """    
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
            return
        new_node = Node(data)
        new_node.next_node = self.head_node
        self.head_node.prev_node = new_node
        self.head_node = new_node
        
    def insert_at_end(self, data):
        """
        Insert a node at the end of the list
        """    
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
            return
        node = self.head_node
        while node.next_node:
            node = node.next_node
        new_node = Node(data)
        new_node.prev_node = node
        node.next_node = new_node
        
    def insert_after_node(self, value, data):
        """
        Insert a node after a given node
        """        
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
            return
        n = self.head_node
        while n.next_node:
            if n.val == value:
                break
            n = n.next_node
        if not n:
            raise ValueError("node not found")

        new_node = Node(data)
        new_node.next_node = n.next_node
        n.next_node.prev_node = new_node
        n.next_node = new_node
        new_node.prev_node = n
        
    def insert_before_node(self, value, data):
        """
        Insert a node before a given node
        """        
        if self.head_node is None:
            new_node = Node(data)
            self.head_node = new_node
            return
        n = self.head_node
        while n.next_node:
            if n.val == value:
                break
            n = n.next_node
        if not n:
            raise ValueError("node not found")

        new_node = Node(data)
        new_node.prev_node = n.prev_node
        n.prev_node = new_node
        new_node.next_node = n
        new_node.prev_node.next_node = new_node
    
    def delete_at_start(self):
        self.head_node = self.head_node.next_node
        self.head_node.prev_node = None
        
        
    def delete_at_end(self):
        prev = self.head_node
        node = prev.next_node
        
        while node.next_node:
            prev = node
            node = node.next_node

        
        prev.next_node = None
        #node.next_node = None
        
    def delete_after_node(self, value):
        
        n = self.head_node
        while n.next_node:
            if n.val == value:
                break
            n = n.next_node
        if not n:
            raise ValueError("node not found")
        
        n.next_node.prev_node = n.prev_node
        n.prev_node.next_node = n.next_node