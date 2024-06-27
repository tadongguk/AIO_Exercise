class Queue:
    def __init__(self, capacity):

        # Số lượng phần tử tối đa mà queue có thể chứa
        self.capacity = capacity
        # Danh sách để lưu trữ các phần tử trong queue
        self.queue = []

    # Phương thức kiểm tra xem queue có rỗng không
    def is_empty(self):
        return len(self.queue) == 0
    # Phương thức kiểm tra xem queue có đầy không

    def is_full(self):
        return len(self.queue) == self.capacity
    # Phương thức loại bỏ và trả về phần tử đầu tiên của queue

    def dequeue(self):

        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)
    # Phương thức thêm một phần tử vào queue

    def enqueue(self, value):

        if self.is_full():
            # Ném ra ngoại lệ nếu queue đầy
            raise OverflowError("enqueue to full queue")
        self.queue.append(value)
    # Phương thức trả về phần tử đầu tiên của queue

    def front(self):

        if self.is_empty():
            # Ném ra ngoại lệ nếu queue rỗng
            raise IndexError("front from empty queue")
        return self.queue[0]


queue = Queue(5)  # Khởi tạo queue với capacity là 3
print(queue.is_empty())  # True, queue đang rỗng
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.is_full())  # False, queue chưa đầy
print(queue.front())  # 1, phần tử đầu tiên của queue
print(queue.dequeue())  # 1, loại bỏ và trả về phần tử đầu tiên
print(queue.front())  # 2, phần tử đầu tiên mới của queue
print(queue.is_full())  # False, queue chưa đầy
print(queue.is_empty())  # False, queue không rỗng
