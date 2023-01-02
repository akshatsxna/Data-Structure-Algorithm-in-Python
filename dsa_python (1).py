# -*- coding: utf-8 -*-
"""DSA Python.ipynb



*   https://www.youtube.com/watch?v=pkYVOmU3MgA
*   https://jovian.ai/aakashns/python-binary-search

Jovian API:- eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MTQ5Njg4OSwianRpIjoiNjEzYWI4MzgtMTY3Ni00NDk5LTk3ZDMtOGQ4MjJhNjJhYmYzIiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5Ijp7ImlkIjoyNDUxODEsInVzZXJuYW1lIjoicHJhdGVlay1kdXR0YSJ9LCJuYmYiOjE2NjE0OTY4ODksImV4cCI6MTY2NTM4NDg4OX0.BBncRUBLH2BXrbhBoZo7ssJUOfUkHJtmk_yMd77AH98

Binary Search & Complexity Analysis
"""

import math

math.sqrt(64)

def locate_card(cards, query):
    pass

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

result = locate_card(cards, query)
print(result)

result == output

test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

locate_card(**test['input']) == test['output']

tests = []

tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

tests

def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0    
    # Set up a loop for repetition
    while True:
        # Check if element at the current position matche the query
        if cards[position] == query:            
            # Answer found! Return and exit..
            return position        
        # Increment the position
        position += 1        
        # Check if we have reached the end of the array
        if position == len(cards):            
            # Number not found, return -1
            return -1

test

result = locate_card(test['input']['cards'], test['input']['query'])
result

result==output

!pip install jovian --upgrade --quiet

from jovian.pythondsa import evaluate_test_case

evaluate_test_case(locate_card, test)

from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(locate_card, tests)

def locate_card(cards, query):
    position = 0
    
    print('cards:', cards)
    print('query:', query)
    
    while True:
        print('position:', position)
        
        if cards[position] == query:
            return position
        
        position += 1
        if position == len(cards):
            return -1

cards6 = tests[7]['input']['cards']
query6 = tests[7]['input']['query']

locate_card(cards6, query6)

tests[6]

locate_card(cards6, query6)

evaluate_test_cases(locate_card, tests)

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1  
        elif mid_number > query:
            lo = mid + 1
    
    return -1

evaluate_test_cases(locate_card, tests)

evaluate_test_case(locate_card, tests[8])

cards8 = tests[8]['input']['cards']
query8 = tests[8]['input']['cards']

query8[7]

def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

evaluate_test_case(locate_card, tests[8])

evaluate_test_cases(locate_card, tests)

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
    
}

result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)

print("Result: {}\nPassed: {}\nExecution Time: {} ms".format(result, passed, runtime))

result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)

print("Result: {}\nPassed: {}\nExecution Time: {} ms".format(result, passed, runtime))

def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card(cards, query):
    
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(cards) - 1, condition)

evaluate_test_cases(locate_card, tests)

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

"""Class & LinkedList"""

class Node():
    pass

Node()

node1=Node()

node1

node2=Node()

node2

node3=Node()

node3

class Node():
    def __init__(self):
        self.data = 0

node4 = Node()

node4.data

node4.data=8
node4.data

node1 = Node()
node1.data = 2

node2 = Node()
node2.data = 4

node3 = Node()
node3.data = 6

node1.data, node2.data, node3.data

class LinkedList():
    def __init__(self):
        self.head = None

list1 = LinkedList()

list1.head = Node(2)

list1.head.next = Node(1)

list1.head.next.next = Node(6)

list1.head.data, list1.head.next.data, list1.head.next.next.data

list1.head, list1.head.next, list1.head.next.next, list1.head.next.next.next

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(8)

list2.head.data, list2.head.next.data, list2.head.next.next.data

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
            
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(7)

list2.show_elements()

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
            
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
            
    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

list2.length()

list2.get_element(0)

list2.get_element(1)

list2.get_element(2)

list2.get_element(3)

def reverse(l):
    if l.head is None:
        return
    
    current_node = l.head
    prev_node = None
    
    while current_node is not None:
        # Track the next node
        next_node = current_node.next
        
        # Modify the current node
        current_node.next = prev_node
        
        # Update prev and current
        prev_node = current_node
        current_node = next_node
        
    l.head = prev_node

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

reverse(list2)

list2.show_elements()

"""Binary Search Trees, Traversals and Balancing in Python"""

class User:
    pass

user1 = User()

user1

type(user1)

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User created!')

user2 = User('Prateek', 'Prateek Dutta', 'prateekdutta2001.com')

user2

user2.name

user2.email, user2.username

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))

user3 = User('Prateek', 'Prateek Dutta', 'prateekdutta2001.com')

user3.introduce_yourself('Ramesh')

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

user4 = User('Prateek', 'Prateek Dutta', 'prateekdutta2001.com')

user4

class UserDatabase:
    def insert(self, user):
        pass
    
    def find(self, username):
        pass
    
    def update(self, user):
        pass
        
    def list_all(self):
        pass

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

biraj.username, biraj.email, biraj.name

print(aakash)

users

'biraj' < 'hemanth'

class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users

database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user = database.find('siddhant')
user

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))

user = database.find('siddhant')
user

database.list_all()

database.insert(biraj)

database.list_all()

# Commented out IPython magic to ensure Python compatibility.
# %%time
# for i in range(100000000):
#     j = i*i

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0

node0.key

node0.left = node1
node0.right = node2

tree = node0

tree.key

tree.left.key

tree.right.key

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))

tree2

tree2.key

tree2.left.key, tree2.right.key

tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key

tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key

def tree_to_tuple(node):
    pass

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)

display_keys(tree2, '  ')

def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))

tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))

display_keys(tree, '  ')

traverse_in_order(tree)

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

tree_height(tree)

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

tree_size(tree)

class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

tree_tuple

tree = TreeNode.parse_tuple(tree_tuple)

tree

tree.display_keys('  ')

tree.height()

tree.size()

tree.traverse_in_order()

tree.to_tuple()

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key

tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))

is_bst(tree1)

tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))

is_bst(tree2)

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# Level 0
tree = BSTNode(jadhesh.username, jadhesh)

# View Level 0
tree.key, tree.value

# Level 1
tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)

# View Level 1
tree.left.key, tree.left.value, tree.right.key, tree.right.value

display_keys(tree)

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree = insert(None, jadhesh.username, jadhesh)

insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

display_keys(tree)

tree2 = insert(None, aakash.username, aakash)
insert(tree2, biraj.username, biraj)
insert(tree2, hemanth.username, hemanth)
insert(tree2, jadhesh.username, jadhesh)
insert(tree2, siddhant.username, siddhant)
insert(tree2, sonaksh.username, sonaksh)
insert(tree2, vishal.username, vishal)

display_keys(tree2)

tree_height(tree2)

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

node = find(tree, 'hemanth')

node.key, node.value

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))

node = find(tree, 'hemanth')
node.value

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

list_all(tree)

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height

is_balanced(tree)

is_balanced(tree2)

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root

data = [(user.username, user) for user in users]
data

tree = make_balanced_bst(data)

display_keys(tree)

tree3 = None
for username, user in data:
    tree3 = insert(tree3, username, user)

def balance_bst(node):
    return make_balanced_bst(list_all(node))

tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)

display_keys(tree1)

tree2 = balance_bst(tree1)

display_keys(tree2)

import math
math.log(100000000, 2)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# for i in range(26):
#     j = i*i

# Commented out IPython magic to ensure Python compatibility.
# %%time
# for i in range(100000000):
#     j = i*i

"""A Python-Friendly Treemap"""

class TreeMap():
    def __init__(self):
        self.root = None
        
    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)
            
        
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root))
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_keys(self.root)

users

treemap=TreeMap()

treemap.display()

treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh

treemap.display()

treemap['jadhesh']

len(treemap)

treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal

treemap.display()

for key, value in treemap:
    print(key, value)

list(treemap)

treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')

treemap['aakash']

"""Class & Linked List"""

class Node():
    pass

Node()

node1=Node()

node1

node2=Node()

node2

node3=Node()

node3

class Node():
    def __init__(self):
        self.data = 0

node4=Node()

node4.data

node4.data=10

node4.data

node1 = Node()
node1.data = 2

node2 = Node()
node2.data = 3

node3 = Node()
node3.data = 5

node1.data, node2.data, node3.data

class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

node1 = Node(2)
node2 = Node(3)
node3 = Node(5)

node1.data, node2.data, node3.data

class LinkedList():
    def __init__(self):
        self.head = None

list1 = LinkedList()

list1.head = Node(2)

list1.head.next = Node(3)

list1.head.next.next = Node(4)

list1.head.data, list1.head.next.data, list1.head.next.next.data

list1.head, list1.head.next, list1.head.next.next, list1.head.next.next.next

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)

list2.head.data, list2.head.next.data, list2.head.next.next.data

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
            
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)

list2.show_elements()

class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)
            
    def show_elements(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result
            
    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

list2.length()

list2.get_element(0)

list2.get_element(1)

list2.get_element(2)

list2.get_element(3)

def reverse(l):
    if l.head is None:
        return
    
    current_node = l.head
    prev_node = None
    
    while current_node is not None:
        # Track the next node
        next_node = current_node.next
        
        # Modify the current node
        current_node.next = prev_node
        
        # Update prev and current
        prev_node = current_node
        current_node = next_node
        
    l.head = prev_node

list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)
list2.append(9)

reverse(list2)

list2.show_elements()

"""Sorting Algorithms and Divide & Conquer


"""

def sort(nums):
    pass

# List of numbers in random order
test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}

# List of numbers in random order
test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}

# A list that's already sorted
test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list that's sorted in descending order
test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list containing repeating elements
test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

# An empty list 
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}

# A list containing just one element
test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

# A list containing one element repeated many times
test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    
    # 4. Repeat the process n-1 times
    for _ in range(len(nums) - 1):
        
        # 1. Iterate over the array (except last element)
        for i in range(len(nums) - 1):
            
            # 2. Compare the number with  
            if nums[i] > nums[i+1]:
                
                # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums

x, y = 2, 3
x, y = y, x
x, y

nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = bubble_sort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

result0 == output0

!pip install jovian --upgrade --quiet
from jovian.pythondsa import evaluate_test_cases
results = evaluate_test_cases(bubble_sort, tests)

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums

nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = insertion_sort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    
    # Get the midpoint
    mid = len(nums) // 2
    
    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    
    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    
    # Combine the results of the two halves
    sorted_nums =  merge(left_sorted, right_sorted)
    
    return sorted_nums

def merge(nums1, nums2):    
    # List to store the results 
    merged = []
    
    # Indices for iteration
    i, j = 0, 0
    
    # Loop over the two lists
    while i < len(nums1) and j < len(nums2):        
        
        # Include the smaller element in the result and move to next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1 
        else:
            merged.append(nums2[j])
            j += 1
    
    # Get the remaining parts
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    
    # Return the final merged array
    return merged + nums1_tail + nums2_tail

merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12])

nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = merge_sort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

results = evaluate_test_cases(merge_sort, tests)

def merge(nums1, nums2, depth=0):
    print('  '*depth, 'merge:', nums1, nums2)
    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]
        
def merge_sort(nums, depth=0):
    print('  '*depth, 'merge_sort:', nums)
    if len(nums) < 2: 
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid], depth+1), 
                 merge_sort(nums[mid:], depth+1), 
                 depth+1)

merge_sort([5, -12, 2, 6, 1, 23, 7, 7, -12])

def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums

def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1
    
    # Initialize right and left pointers
    l, r = start, end-1
    
    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        
        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        
        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

l1 = [1, 5, 6, 2, 0, 11, 3]
pivot = partition(l1)
print(l1, pivot)

nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = quicksort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

nums0, output0 = test0['input']['nums'], test0['output']

print('Input:', nums0)
print('Expected output:', output0)
result0 = quicksort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

from jovian.pythondsa import evaluate_test_cases
results = evaluate_test_cases(quicksort, tests)

class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes
        
    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)

nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]

notebooks

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'

def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'

def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare), 
                 merge_sort(objs[mid:], compare), 
                 compare)

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

sorted_notebooks = merge_sort(notebooks, compare_likes)

sorted_notebooks

def compare_titles(nb1, nb2):
    if nb1.title < nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    elif nb1.title > nb2.title:
        return 'greater'

merge_sort(notebooks, compare_titles)

"""Recursion and Dynamic Programming"""

T0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
}

T1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

T2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

T3 = {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T4 = {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
}

T5 = {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
}

T6 = {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
}

T7 = {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}

lcq_tests = [T0, T1, T2, T3, T4, T5, T6, T7]

# 0-1 Knapsack Problem
test0 = {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
}

test1 = {
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
}

test2 = {
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
}

test3 = {
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
}

test4 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
}

test5 = {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
}

tests = [test0, test1, test2, test3, test4, test5]

def lcq_recursive(seq1, seq2, idx1=0, idx2=0):
    # Check if either of the sequences is exhausted
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    
    # Check if the current characters are equal
    if seq1[idx1] == seq2[idx2]:
        return 1 + lcq_recursive(seq1, seq2, idx1+1, idx2+1)
    # Skip one element from each sequence
    else:
        return max(lcq_recursive(seq1, seq2, idx1+1, idx2), 
                   lcq_recursive(seq1, seq2, idx1, idx2+1))

from jovian.pythondsa import evaluate_test_cases

evaluate_test_cases(lcq_recursive, lcq_tests)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# lcq_recursive('seredipitous', 'precipitation')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# lcq_recursive('Asdfsfafssess', 'oypiououuiuo')

def lcq_memoized(seq1, seq2):
    memo = {}
    
    def recurse(idx1, idx2):
        key = idx1, idx2
        
        if key in memo:
            return memo[key]
        
        if idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), 
                            recurse(idx1, idx2+1))
        return memo[key]
        
    return recurse(0, 0)

evaluate_test_cases(lcq_memoized, lcq_tests)

def lcq_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
            else:
                results[idx1+1][idx2+1] = max(results[idx1][idx2+1], results[idx1+1][idx2])
    return results[-1][-1]

evaluate_test_cases(lcq_dp, lcq_tests)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# lcq_dp('Asdfsfafssess', 'oypiououuiuo')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# lcq_dp('seredipitous', 'precipitation')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# lcq_dp('longest', 'stone')

from jovian.pythondsa import evaluate_test_cases

def max_profit_recursive(capacity, weights, profits, idx=0):
    if idx == len(weights):
        return 0
    if weights[idx] > capacity:
        return max_profit_recursive(capacity, weights, profits, idx+1)
    else:
        return max(max_profit_recursive(capacity, weights, profits, idx+1),
                   profits[idx] + max_profit_recursive(capacity-weights[idx], weights, profits, idx+1))

evaluate_test_cases(max_profit_recursive, tests)

def knapsack_memo(capacity, weights, profits):
    memo = {}
    
    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx+1, remaining)
        else:
            memo[key] = max(recurse(idx+1, remaining), 
                            profits[idx] + recurse(idx+1, remaining-weights[idx]))
        return memo[key] 
        
    return recurse(0, capacity)

evaluate_test_cases(knapsack_memo, tests)

def knapsack_dp(capacity, weights, profits):
    n = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for idx in range(n):
        for c in range(capacity+1):
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            else:
                results[idx+1][c] = max(results[idx][c], profits[idx] + results[idx][c-weights[idx]])
            
    return results[-1][-1]

evaluate_test_cases(knapsack_dp, tests)

"""Graph Algorithms (BFS, DFS, Shortest Paths)"""

num_nodes3 = 9
edges3 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
num_nodes3, len(edges3)

# Graph with weights
num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

num_nodes5, len(edges5)

num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
num_nodes6, len(edges6)

def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
num_nodes7, len(edges7)

num_nodes1 = 5
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]
num_nodes1, len(edges1)

num_nodes3 = 9
edges3 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]
num_nodes3, len(edges3)

num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6), 
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

num_nodes5, len(edges5)

# Directed graph
num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]
num_nodes6, len(edges6)

num_nodes7 = 6
edges7 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
num_nodes7, len(edges7)

class Graph:
    def __init__(self, num_nodes, edges):
        self.data = [[] for _ in range(num_nodes)]
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)
            
    def __repr__(self):
        return "\n".join(["{} : {}".format(i, neighbors) for (i, neighbors) in enumerate(self.data)])

    def __str__(self):
        return repr(self)

g1 = Graph(num_nodes1, edges1)

g1

#BFS[Breadth First Search]
def bfs(graph, source):
    visited = [False] * len(graph.data)
    queue = []
    
    visited[source] = True    
    queue.append(source)
    i = 0
    
    while i < len(queue):
        for v in graph.data[queue[i]]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
        i += 1
        
    return queue

bfs(g1, 3)

# DFS[Depth First Search]
def dfs(graph, source):
    visited = [False] * len(graph.data)
    stack = [source]
    result = []
    
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            result.append(current)
            visited[current] = True
            for v in graph.data[current]:
                stack.append(v)
                
    return result

dfs(g1,0)

#Directed Weighted graph
class Graph:
    def __init__(self, num_nodes, edges, directed=False):
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        
        self.directed = directed
        self.weighted = len(edges) > 0 and len(edges[0]) == 3
            
        for e in edges:
            self.data[e[0]].append(e[1])
            if self.weighted:
                self.weight[e[0]].append(e[2])
            
            if not directed:
                self.data[e[1]].append(e[0])
                if self.weighted:
                    self.data[e[1]].append(e[2])
                
    def __repr__(self):
        result = ""
        for i in range(len(self.data)):
            pairs = list(zip(self.data[i], self.weight[i]))
            result += "{}: {}\n".format(i, pairs)
        return result

    def __str__(self):
        return repr(self)

g7 = Graph(num_nodes7, edges7, directed=True)

g7

g7.weight

# Shortest Path - Dijkstra's Algorithm
def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node
        
def shortest_path(graph, source, dest):
    """Find the length of the shortest path between source and destination"""
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    parent = [None] * len(graph.data)
    queue = []
    idx = 0
    
    queue.append(source)
    distance[source] = 0
    visited[source] = True    
    while idx < len(queue) and not visited[dest]:
        current = queue[idx]
        update_distances(graph, current, distance, parent)        
        next_node = pick_next_node(distance, visited)
        if next_node is not None:
            visited[next_node] = True
            queue.append(next_node)
        idx += 1        
    return distance[dest], distance, parent

shortest_path(g7, 0, 5)

