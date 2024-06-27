class Stack:
    def __init__(self, capacity):
        # Số lượng phần tử tối đa mà stack có thể chứa
        self.capacity = capacity
        # Danh sách để lưu trữ các phần tử trong stack
        self.stack = [] 
    
    # Phương thức kiểm tra xem stack có rỗng không
    def is_empty(self):
        return len(self.stack) == 0
    # Phương thức kiểm tra xem stack có đầy không
    def is_full(self):
        return len(self.stack) == self.capacity
    # Phương thức loại bỏ và trả về phần tử trên cùng của stack
    def pop(self):

        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    # Phương thức thêm một phần tử vào stack
    def push(self, value):
        if self.is_full():
            raise OverflowError("push to full stack")
        self.stack.append(value)
    # Phương thức trả về phần tử trên cùng của stack
    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self.stack[-1]




stack = Stack(5)  # Khởi tạo stack với capacity là 3
print(stack.is_empty())  # True, stack đang rỗng
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.is_full())  # False, stack chưa đầy
print(stack.top())  # 4, phần tử trên cùng của stack
print(stack.pop())  # 4, loại bỏ và trả về phần tử trên cùng
print(stack.top())  # 3, phần tử trên cùng mới của stack
print(stack.is_full())  # False, stack chưa đầy
print(stack.is_empty())  # False, stack không rỗng
