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
        if (self.is_empty() == False): # it made big change!!!
            element = self.Elements.pop()
            print("function get ", element, "item to stock")
            self.tail += 1
            if (self.tail >= self.list_size):
                self.tail = 0
        else:
            print("queue is empty")
    # putting in first empty place specific element
    def put(self, item):
        if (self.head != self.tail or self.is_empty()):
            self.Elements.insert(self.head, item)
            print("function put ", item, " item to queue")
            self.head += 1
            if (self.head >= self.list_size):
                self.head = 0

Queue = Fifo_queue()
Queue.put(1)
Queue.put(2)
Queue.get()





