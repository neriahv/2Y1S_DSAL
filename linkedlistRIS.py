class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1 

    def iterate_items(self):
        current_item = self.tail  
        while current_item:
            yield current_item.data  
            current_item = current_item.next

    def insert_item(self, data, position):
        node = Node(data)
        if position < 0 or position > self.count:
            print("Invalid position.")
            return

        if position == 0:
            node.next = self.tail
            self.tail = node
            if self.count == 0:
                self.head = node
        else:
            current = self.tail
            prev = None
            for _ in range(position):
                prev = current
                current = current.next
            
            prev.next = node
            node.next = current
            
            if current is None:  # Insert at the end
                self.head = node
            
        self.count += 1

    def search_item(self, val):
        for node in self.iterate_items():
            if val == node:
                return True 
        return False

def main():
    linkedlist = SinglyLinkedList()

    subjects_list = ["LOGPROG", "PROGSDATS", "PHCI", "OPSYSFUN", "DSAL"]

    for x in subjects_list:
        linkedlist.append_item(x)

    while True:
        action = input("Do you want to search, remove, insert, or print the list? (search/remove/insert/print): ").lower().strip()

        if action == "search":
            search_subj = input("Enter the subject to search: ").upper().strip()
            if linkedlist.search_item(search_subj):
                print(f"{search_subj} is in the list.")
            else:
                print(f"{search_subj} is not in the list.")

        elif action == "remove":
            remove_subj = input("Enter the subject to remove: ").upper().strip()
            if linkedlist.remove_item(remove_subj):
                print(f"{remove_subj} has been removed.")
            else:
                print(f"{remove_subj} not found in the list.")
        
        elif action == "insert":
            insert_subj = input("Enter the subject to insert: ").upper().strip()
            position = int(input("Enter the position to insert at (0 for beginning): "))
            linkedlist.insert_item(insert_subj, position)
            print(f"{insert_subj} has been inserted at position {position}.")

        elif action == "print":
            # Collect all items into a list and print using join
            items = list(linkedlist.iterate_items())
            if items:
                print("->".join(items))
            else:
                print("The list is empty.")

        else:
            print("Invalid action.")

        choice = input("Do you want to continue [Y/N]? : ").upper().strip()
        if choice == "Y":
            continue
        elif choice == "N":
            break
        else: 
            print("Invalid input.")
            break

if __name__ == "__main__":
    main()
