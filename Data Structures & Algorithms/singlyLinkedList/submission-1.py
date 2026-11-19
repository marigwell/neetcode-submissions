class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        i = 0

        while current:
            if i == index:
                return current.val

            current = current.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        current = self.head
        i = 0

        while current and current.next:
            if i + 1 == index:
                current.next = current.next.next
                return True

            current = current.next
            i += 1

        return False

    def getValues(self) -> List[int]:
        values = []
        current = self.head

        while current:
            values.append(current.val)
            current = current.next

        return values