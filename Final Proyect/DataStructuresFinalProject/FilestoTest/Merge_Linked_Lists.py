import sys
sys.path.append('../DataStructuresFinalProject')
from DataStructures.Singly_Linked_List import Singly_linked_list

def merge_nodes(node1, node2): # Se define una function auxiliar que recibe nodos 
                                # ya que no se puede realizar el merge directamente con las linked list
        if not node2: #Caso base 1. Si no existe node2, retorna node1. Es como hacer merge de un elemento con otro vacio
            return node1
        if not node1: #Caso base 2. Equivalente al anterior caso base.
            return node2
        if node1.val < node2.val: # Caso base 3. 
            node1.next_node = merge_nodes(node1.next_node, node2) # Si node1<node2 seteo el node1.next_node de acuerdo al orden que me retorne la llamada recursiva
            return node1 #Retorno node1 tal que: node1 -> ... -> ...
        else:
            node2.next_node = merge_nodes(node1, node2.next_node) # Equivalente al anterior.
            return node2 #Retorno node2 tal que: node2 -> ... -> ...
def merge_linked_lists(llist1, llist2):
    newllist = Singly_linked_list(merge_nodes(llist1.head_node, llist2.head_node)) #Devuelvo la linked list seteando el nodo cabeza 
    return newllist
