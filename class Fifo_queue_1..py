class Fifo_queue:
    # constructor 
    def __init__(self):
        # we will start with empty list named "Elements" 
        self.head = 0
        self.tail = 0
        self.Elements = []
        # defining what maximum number of items our queue can contain
        self.list_size = 8
        # finding out if queue is empty
    def is_empty(self):
        return self.Elements == []
    # getting out last item from queue
    def get(self):
        if (self.head != self.tail):
            element = self.Elements.pop()
            if (self.tail >= self.list_size):
                self.tail = 0
            else:
                self.tail += 1
            print("function get ", element, "item to stock")
        else:
            print("queue is empty")
    # putting in first empty place specific element
    def put(self, item):
        if (self.head != self.tail or self.is_empty()):
            self.Elements.insert(self.head, item)
            print("function put ", item, " item to queue")
            if (self.tail >= self.list_size):
                self.head = 0
            else:
                self.head += 1
Queue = Fifo_queue()
Queue.put(1)
Queue.put(2)
Queue.get()





