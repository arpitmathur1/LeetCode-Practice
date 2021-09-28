'''
level order of a tree
2-ary tree
limit to levels: no

n0 = node()

n2 = node(9)
n3 = node(20)
n1 = node(3, n2, n3)

n3 = node(20)
n1 = node(3, None, n3)

n2 = node(9)
n3 = node(20)
n1 = node(3, n2, n3)

       3
    9    20
  1  2  4  5
 5 7
OP: [ [3], [9,20], [1,2,4,5], [5,7]]
'''


class node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self.value)
'''
Algo (iterative):

level_order(node n)
    final_list = []
    queue = [n]
    child_queue = []

    while queue is not empty:
        final_list.append(queue)

        for element in queue:
            if element.left is not empty:
                child_queue.append(element.left)
            if element.right is not empty:
                child_queue.append(element.right)
        queue = child_queue[:]

    final_list: [[3], [9,20], [1, 2, 4, 5], [5, 7]]
    queue : [5, 7]
'''


def level_order(n):
    final_list = []
    if n is not None:
        queue = [n]
    else:
        queue = []
    child_queue = []

    while len(queue) > 0:  # is not []:
        final_list.append(queue)

        for element in queue:
            if element.left is not None:
                child_queue.append(element.left)
            if element.right is not None:
                child_queue.append(element.right)
        queue = child_queue[:]
        child_queue = []
    print("final_list", final_list)
    return final_list

'''
       3
    9    20
  1  2  4  5
'''
n2_1 = node(1)
n2_2 = node(2)
n2_3 = node(4)
n2_4 = node(5)

n2 = node(9, n2_1, None)
n3 = node(20, n2_3, n2_4)
n1 = node(3, n2, n3)

level_order(n1)
level_order(None)
