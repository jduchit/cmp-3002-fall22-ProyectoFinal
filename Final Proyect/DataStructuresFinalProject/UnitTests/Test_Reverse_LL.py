import unittest
import sys
sys.path.append('../DataStructuresFinalProject')
from DataStructures.Singly_Linked_List import Node, Singly_linked_list

"""
Variables para 'reverse_list'
"""

nodes = [i for i in range(10000)]
reverse_nodes = nodes.copy()
reverse_nodes.reverse()

# *** Linked List average
LL0 =  Singly_linked_list(Node(nodes[0]))
for i in nodes[1:]:
    LL0.insert_tail(i)

# *** Reversed Linked List average
LL0_rev =  Singly_linked_list(Node(reverse_nodes[0]))
for i in reverse_nodes[1:]:
    LL0_rev.insert_tail(i)


# *** Linked List with one element
LL1 =  Singly_linked_list(Node(3))
LL1_rev =  Singly_linked_list(Node(3))


# *** Empty Linked List
LL2 =  Singly_linked_list()
LL2_rev =  Singly_linked_list(None)


class Test_Reverse_Linked_List(unittest.TestCase):
    
    def test_reverse_list_avg(self):
        # Revisa funcionamiento normal
        LL0.reverse_list()
        self.assertEqual(LL0.list_traversed(), LL0_rev.list_traversed())
    
    def test_one_element(self):
        # Revisa funcionamiento para linked list de 1 solo nodo
        LL1.reverse_list()
        self.assertEqual(LL1.list_traversed(), LL1_rev.list_traversed())

    def test_empty_LL(self):
        # Revisar funcionamiento para linked list de 0 elementos
        LL2.reverse_list()
        self.assertEqual(LL2.head_node, None)
        self.assertEqual(LL2_rev.head_node, None)
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    

    














