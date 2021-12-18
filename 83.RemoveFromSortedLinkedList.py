
def deleteDuplicates(head):
    seen = set()
    prev = None
    start = head
    while head is not None:
        # Visit the next node
        if head.val not in seen:
            seen.add(head.val)
            prev = head
            head = head.next
        # Time to remove
        else:
            # Delete seen node
            prev.next = head.next
            head = head.next
    print(seen)
    return start