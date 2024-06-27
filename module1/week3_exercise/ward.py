from datetime import datetime

# Lớp Ward đại diện cho một khu vực chứa nhiều người


class Ward:
    def __init__(self, name):
        self._name = name  # Tên của khu vực
        self._people = []  # Danh sách các người trong khu vực

    # Phương thức thêm một người vào khu vực
    def add_person(self, person):
        self._people.append(person)

    # Phương thức mô tả thông tin của khu vực và tất cả người trong khu vực
    def describe(self):
        print(f"Ward: {self._name}")
        for person in self._people:
            print(person.describe())

    # Phương thức đếm số lượng bác sĩ trong khu vực
    def count_doctors(self):
        count = 0
        for person in self._people:
            if isinstance(person, Doctor):
                count += 1
        print(f"Amount of doctors: {count}")

    # Phương thức sắp xếp người trong khu vực theo năm sinh tăng dần
    def sort_age(self):
        def get_age(person):
            return person.get_age()
        self._people.sort(key=get_age, reverse=True)
        for person in self._people:
            print(person.describe())

    # Phương thức tính năm sinh trung bình của các giáo viên trong khu vực
    def compute_average_age(self):
        total_age = 0
        total_people = 0
        for person in self._people:
            if isinstance(person, Teacher):
                total_people += 1
                total_age += person._yob
        average_age = total_age / total_people
        print(f"Average age of teachers: {average_age}")


# Lớp Person đại diện cho một người


class Person:
    def __init__(self, name, yob):
        self._name = name  # Tên của người
        self._yob = yob    # Năm sinh của người

    # Phương thức mô tả thông tin của người
    def describe(self):
        return f"Name: {self._name}, Year of Birth: {self._yob}"

    # Phương thức tính tuổi của người
    def get_age(self):
        current_year = datetime.now().year
        return current_year - self._yob

# Lớp Student đại diện cho một sinh viên, kế thừa từ lớp Person


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade  # Lớp của sinh viên

    # Phương thức mô tả thông tin của sinh viên
    def describe(self):
        return f"Student - {super().describe()}, Grade: {self._grade}"

# Lớp Teacher đại diện cho một giáo viên, kế thừa từ lớp Person


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject  # Môn học của giáo viên

    # Phương thức mô tả thông tin của giáo viên
    def describe(self):
        return f"Teacher - {super().describe()}, Subject: {self._subject}"

# Lớp Doctor đại diện cho một bác sĩ, kế thừa từ lớp Person


class Doctor(Person):
    def __init__(self, name, yob, specialty):
        super().__init__(name, yob)
        self._specialty = specialty  # Chuyên môn của bác sĩ

    # Phương thức mô tả thông tin của bác sĩ
    def describe(self):
        return f"Doctor - {super().describe()}, Specialty: {self._specialty}"


# Tạo các đối tượng sinh viên, giáo viên và bác sĩ
student1 = Student("John", 2000, 12)
teacher1 = Teacher("Jane", 1995, "Math")
teacher2 = Teacher("Joe", 1969, "Science")
doctor1 = Doctor("James", 1970, "Cardiology")
doctor2 = Doctor("Jill", 1975, "Neurology")

# Tạo đối tượng Ward và thêm các đối tượng vào khu vực
a = Ward("A")
a.add_person(student1)
a.add_person(teacher1)
a.add_person(teacher2)
a.add_person(doctor1)
a.add_person(doctor2)

# Mô tả thông tin của tất cả các đối tượng trong khu vực
a.describe()

# Đếm số lượng bác sĩ trong khu vực
a.count_doctors()

# Sắp xếp người trong khu vực theo tuổi giảm dần và in ra thông tin
a.sort_age()

# Tính tuổi trung bình của các giáo viên trong khu vực
a.compute_average_age()
