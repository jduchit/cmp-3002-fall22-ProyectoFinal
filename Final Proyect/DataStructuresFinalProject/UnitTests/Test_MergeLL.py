import unittest
from DataStructures.Singly_Linked_List import Node, Singly_linked_list
import sys
sys.path.append('../DataStructuresFinalProject')
from FilestoTest.Merge_Linked_Lists import merge_linked_lists

"""
Variables para 'reverse_list'
"""

even_nodes = [i for i in range(0, 10000, 2)]
odd_nodes = [j for j in range(1, 10000, 2)]
all_nodes = [k for k in range(10000)]

# *** Linked List with even nodes
LL0 =  Singly_linked_list(Node(even_nodes[0]))
for i in even_nodes[1:]:
    LL0.insert_tail(i)

# *** Linked List with odd nodes
LL1 =  Singly_linked_list(Node(odd_nodes[0]))
for i in odd_nodes[1:]:
    LL1.insert_tail(i)

# *** Empty Linked List
LL2 =  Singly_linked_list()

# *** To Test Linked List
LLT = Singly_linked_list(Node(all_nodes[0]))
for i in all_nodes[1:]:
    LLT.insert_tail(i)


class Test_Merge_Sorted_Linked_Lists(unittest.TestCase):
    
    def test_base_large_case1(self):
        # Revisa funcionamiento normal
        merged_LL = merge_linked_lists(LL0, LL1)
        self.assertEqual(merged_LL, LLT)
    
    def test_base_large_case2(self):
        # Revisa funcionamiento normal
        merged_LL = merge_linked_lists(LL1, LL0)
        self.assertEqual(merged_LL, LLT)

    def test_empty_LL(self):
        # Revisa funcionamiento para linked list de 1 solo nodo
        merged_LL = merge_linked_lists(LL2, LL2)
        self.assertEqual(merged_LL, LL2)

def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
  
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity = verbosity).run(suite)

if __name__ == '__main__':
    unittest.main()