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
            val =  current_item.data  
            current_item = current_item.next  
            yield val

    def search_item(self, val):
        for node in self.iterate_items():
            if val == node:
                return True 
        return False
    
def main ():
    linkedlist = SinglyLinkedList()

    subjects_list = ["LOGPROG", "PROGSDATS", "PHCI", "OPSYSFUN", "DSAL"]

    for x in subjects_list:
        linkedlist.append_item(x)
    
    while True:
        search_subj = input("Enter the subject: ").upper().strip()
        if not search_subj:
            print("Invalid input. Please try again.")
            continue
        
        if linkedlist.search_item(search_subj):
            print("TRUE")
        else:
            print("FALSE")

        choice = input("Do you want to input again [Y/N]? : ").upper().strip()
        if choice == "Y":
            continue
        elif choice == "N":
            break
        else: 
            print("Invalid input.")
            break

if __name__ == "__main__":
    main()