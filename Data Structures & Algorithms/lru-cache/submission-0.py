class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = {}  # key -> Node
        self.Low = Node(-1, 0)
        self.High = Node(-1, 0)
        self.Low.next = self.High
        self.High.prev = self.Low

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add_node(node)
            return node.val
        else:
            return -1
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_node(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_node(node)
            if self.size < self.capacity:
                self.size += 1
            else:
                node_to_remove = self.Low.next
                self.remove(node_to_remove)
                del self.cache[node_to_remove.key]

    def remove(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev

    def add_node(self, node):
        node_prev = self.High.prev
        node.next = self.High
        node_prev.next = node
        self.High.prev = node
        node.prev = node_prev
