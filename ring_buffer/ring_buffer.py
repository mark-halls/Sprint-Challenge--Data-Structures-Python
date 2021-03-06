from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # write pointer
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if we haven't started our buffer, add an item to it
        if len(self.storage) == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            return

        # set the next node on tail to be the head if we reach capacity
        if (len(self.storage)) == self.capacity and self.storage.tail.next is None:
            self.storage.tail.next = self.storage.head

        # if tail.next is still None we can keep appending to tail
        if self.storage.tail.next is None:
            self.storage.add_to_tail(item)
            self.current = self.current.next
        else:
            # otherwise, set the next nodes value to be the item.
            self.current = self.current.next
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cursor = self.storage.head

        # add the first element of our buffer to the array so we have a stopping point
        list_buffer_contents.append(cursor.value)

        # increment the cursor 1 since we already have that value
        cursor = cursor.next

        # until the cursor equals the head, append items from our buffer
        while cursor is not self.storage.head:
            list_buffer_contents.append(cursor.value)

            # if cursor.next equals None our buffer is smaller than max so just break the loop
            if cursor.next is None:
                break
            cursor = cursor.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------

"""
The main disadvantage I see to this is that the buffer must be contiguous in memory. 

The big advantage is the implementation is much simpler. 

I think the disadvante in arrays this overcomes is needing to copy the array to a new portion of memory when we add or remove items

"""


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(capacity)]
        self.cursor = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.cursor] = item
            if self.cursor == self.capacity - 1:
                self.cursor = 0
            else:
                self.cursor += 1
        else:
            self.storage.append(item)
            self.cursor += 1

    def get(self):
        return [i for i in self.storage if i]
