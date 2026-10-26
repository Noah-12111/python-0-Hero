# Week 14 — OOP cơ bản (lý thuyết dễ nhớ)

Tuần này học cách gom **dữ liệu** và **hành động liên quan** vào object. Chỉ cần nắm 5 ý: class, object, `__init__`/`self`, method/`__str__`, composition và inheritance.

## 1. Class và object

Hãy tưởng tượng **class là bản vẽ**, còn **object là đồ vật được tạo từ bản vẽ**.

- **Class**: mô tả object có dữ liệu gì và làm được gì.
- **Object**: một đối tượng cụ thể được tạo từ class.
- **Attribute**: dữ liệu của object.
- **Method**: hành động hoặc phép tính liên quan đến object.

Ví dụ: `Dog` là bản vẽ chung; `Dog("Milo")` là một chú chó cụ thể.

## 2. `__init__` và `self`

- `__init__` chạy khi tạo object, thường dùng để lưu dữ liệu ban đầu.
- `self` chỉ **object hiện tại**. Viết `self.name = name` nghĩa là lưu giá trị `name` vào object này.

```python
class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Milo")
dog2 = Dog("Luna")

print(dog1.name)  # Milo
print(dog2.name)  # Luna
```

Hai object cùng class nhưng có dữ liệu riêng:

```text
Dog("Milo")  -> name = "Milo"
Dog("Luna")  -> name = "Luna"
```

## 3. Method và `__str__`

Method là hàm được viết bên trong class. `__str__` cho biết nên hiển thị object thế nào khi dùng `print()`.

```python
class Progress:
    def __init__(self, completed, total):
        self.completed = completed
        self.total = total

    def percentage(self):
        return self.completed / self.total * 100

    def __str__(self):
        return f"{self.completed}/{self.total} bài"

progress = Progress(3, 4)
print(progress.percentage())  # 75.0
print(progress)               # 3/4 bài
```

Đọc dòng `Progress(3, 4)` như sau: đã hoàn thành 3 bài trên tổng số 4 bài. Phần trăm là **3 / 4 × 100 = 75%**.

## 4. Encapsulation — gom những thứ có liên quan

Encapsulation ở mức cơ bản có thể hiểu là **để dữ liệu và hành động liên quan ở cùng một nơi**.

Trong ví dụ trên, `Progress` giữ `completed`, `total` và phép tính `percentage()`. Ta không phải viết phép tính tiến độ rải rác ở nhiều chỗ.

## 5. Composition — object sử dụng object/hành vi khác

Composition nghĩa là một object **có hoặc sử dụng** một thành phần khác. Ví dụ, `Bot` nhận một strategy (hàm quyết định hành động).

```python
class Bot:
    def __init__(self, strategy):
        self.strategy = strategy

    def choose_action(self, state):
        return self.strategy(state)

def go_right(state):
    return "right"

bot = Bot(go_right)
print(bot.choose_action({}))  # right
```

Sơ đồ:

```text
Bot
 └── strategy (hàm được truyền vào)
       └── quyết định action
```

Muốn đổi hành vi thì truyền hàm khác vào: `Bot(go_right)`, `Bot(defensive)`... Không cần viết lại class `Bot`.

Trong bài arena của khóa học, ba action hợp lệ là `left`, `right`, `wait`. Strategy di chuyển phải xem cả `position` và `goal`:

```text
position = 1, goal = 4  -> right
position = 3, goal = 0  -> left
position = 2, goal = 2  -> wait
```

Đừng cố định luôn `"right"`: bot có thể cần đi về đầu bên trái.

## 6. Inheritance — kế thừa khi thật sự là “một loại”

Inheritance cho class con nhận dữ liệu/hành vi từ class cha. Chỉ dùng khi quan hệ **is-a** hợp lý.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name}: woof"

dog = Dog("Milo")
print(dog.speak())             # Milo: woof
print(isinstance(dog, Animal)) # True
```

`Dog` là một loại `Animal`, nên kế thừa phù hợp. Ngược lại, không nên dùng inheritance chỉ để tái sử dụng vài dòng code.

## 7. Phân biệt nhanh

| Khái niệm | Hỏi dễ nhớ | Ví dụ |
|---|---|---|
| Class | Bản vẽ là gì? | `Dog` |
| Object | Đối tượng cụ thể nào? | `Dog("Milo")` |
| Attribute | Object lưu gì? | `self.name` |
| Method | Object làm gì? | `speak()` |
| Composition | Object sử dụng thành phần nào? | `Bot` sử dụng `strategy` |
| Inheritance | Object là một loại gì? | `Dog` là `Animal` |

**Mẹo chọn thiết kế:** “has-a / uses-a” thường gợi ý composition; “is-a” rõ ràng mới cân nhắc inheritance.

## 8. Chạy bài và tự kiểm tra

Chạy từng bài từ thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
python weeks/week-14-oop-essentials/mini-project/bot_demo.py
python weeks/week-14-oop-essentials/checks/check_week.py
```

Kết quả của lệnh cuối cần là `Week 14 solution checks: PASS`. Bài học tuần này không yêu cầu multiple inheritance, metaclass hay kiến trúc phức tạp.
