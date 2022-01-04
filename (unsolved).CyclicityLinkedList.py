def has_cycle(head): 
    def cycle_len(end):
        start, step = end, 0 
        while True:
            step += 1
            if start.next:
                start = start.next 
            else:
                break
            if start is end:
                return step
    
    fast = slow = head

    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
        # Finds the start of the cycle.
            cycle_len_advanced_iter = head
        for _ in range(cycle_len(slow)):
            cycle_len_advanced_iter = cycle_len_advanced_iter.next
    
        it = head
        # Both iterators advance in tandem.
        while it is not cycle_len_advanced_iter: 
            it = it.next
            cycle_len_advanced_iter = cycle_len_advanced_iter.next 
        return it # iter is the start of cycle.
    return None # No cycle

class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data 
        self.next = next_node
    

# Test cases
n = [3,3,2,0,-4] 
nodes = []
for i in range(len(n)):
    nodes.append(ListNode(n[i], None))

for i in range(len(n)):
    if i == len(n)-1:
        nodes[i].next = None
    else:
        nodes[i].next = nodes[i+1]
    
print(nodes)

print(has_cycle(nodes[1]))
print(has_cycle(nodes[0]))