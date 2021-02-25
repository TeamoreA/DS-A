class Queue:
    def __init__(self):
        self.queue_l = []
    
    def is_empty(self):
        if self.queue_l == []:
            return True
        return False

    def __str__(self):
        return '\n'.join(self.queue_l)
    
    def enqueue(self, value):
        self.queue_l.append(str(value))
        return value

    def peek(self):
        if self.is_empty():
            return "The queue is empty"
        return self.queue_l[0]

    def dequeue(self):
        if self.is_empty():
            return "The queue is empty"
        
        return self.queue_l.pop(0)

    def delete(self):
        self.queue_l = []
        return "The queue has been emptied"



q = Queue()
print("+++print+++")
print(q.enqueue(1))
print("+++print+++")
print(q.enqueue(2))
print("+++print+++")
print(q.enqueue(3))
print("+++dequeue+++")
print(q.dequeue())
print("+++peek+++")
print(q.peek())
print("+++delete+++")
print(q.delete())
print("+++print+++")
print(q)

