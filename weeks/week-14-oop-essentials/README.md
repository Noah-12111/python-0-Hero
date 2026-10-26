# Tuần 14 — OOP cơ bản, Composition và Inheritance

Mục tiêu là gom dữ liệu và hành động có liên quan vào object, sau đó biết cách thay đổi hành vi mà không phải sửa class chính.

## Học theo thứ tự

1. Đọc [lý thuyết tiếng Việt, có ví dụ](notes.md).
2. Xem ví dụ trong [examples](examples/).
3. Làm ba bài trong [exercises](exercises/).
4. Chạy [mini-project Bot đổi strategy](mini-project/README.md).
5. Kiểm tra lời giải mẫu bằng [machine check](checks/README.md).

## Nội dung cần nhớ

- **Class** là bản vẽ; **object** là đối tượng tạo ra từ class.
- `__init__` khởi tạo dữ liệu; `self` là object hiện tại.
- **Method** là hàm bên trong class; `__str__` giúp `print(object)` dễ đọc hơn.
- **Composition**: một object sử dụng thành phần/hành vi khác.
- **Inheritance**: class con là một loại class cha, như `Dog` là `Animal`.

## Ôn cùng Week 13 bằng một ứng dụng đời sống

- [Tổng hợp lý thuyết Week 13 + Week 14](../week-13-14-review.md) — dùng ví dụ quản lý việc học để hiểu từng khái niệm được ứng dụng như thế nào.
- [Study Task Manager](../week-13-14-life-project/README.md) — chương trình mẫu kết hợp module/package, CLI, JSON, class/object, composition và inheritance.

## Chạy bài tập

Chạy các lệnh sau từ thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
python weeks/week-14-oop-essentials/mini-project/bot_demo.py
python weeks/week-14-oop-essentials/checks/check_week.py
```

Nếu các phần được cài đặt đúng, lệnh kiểm tra cuối in ra `Week 14 solution checks: PASS`.

Không cần học kiến trúc phức tạp: ưu tiên ví dụ nhỏ, dễ chạy và dễ giải thích.
