class LinkedListNode:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self, head=None):
    self.head = head
    return

  def add_to_tail(self, data):
    new_node = LinkedListNode(data)
    if self.head:
      cur = self.head

      while cur.next:
        cur = cur.next

      cur.next = new_node
    else:
      self.head = new_node

  #   pass

  # def remove_head:
  #   pass

  # def remove_tail:
  #   pass

