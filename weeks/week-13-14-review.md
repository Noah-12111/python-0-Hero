# Tổng hợp Week 13 + Week 14 — dùng Python làm ứng dụng quản lý việc học

Tài liệu này gộp hai tuần bằng **một ví dụ gần đời sống: ứng dụng quản lý việc cần làm khi học đại học**. Mục tiêu không phải viết ứng dụng lớn, mà hiểu từng kiến thức dùng vào đâu.

## 1. Ứng dụng thực tế trông như thế nào?

Ví dụ bạn muốn ghi lại:
- Ôn Python — chưa xong.
- Làm bài OOP — chưa xong.
- Nộp bài SQL — đã xong.

Bạn muốn thêm công việc từ terminal, xem danh sách và đánh dấu đã hoàn thành.

**Week 13** giúp chia chương trình thành file, nhận lệnh từ terminal và hiểu cách một ứng dụng trao đổi dữ liệu với máy chủ. **Week 14** giúp mô tả từng công việc thành object, gom các công việc vào một đối tượng quản lý, và tạo loại công việc đặc biệt bằng kế thừa.

## 2. Week 13 — chia chương trình và nhận lệnh

### Module và package

- **Module**: một file `.py`.
- **Package**: thư mục chứa các module liên quan.
- **Import**: dùng code đã có trong file khác.
- **`__init__.py`**: đánh dấu/cấu hình package.
- **Main guard**: `if __name__ == "__main__":` giúp phần chạy chính chỉ chạy khi file được thực thi như chương trình.

Ví dụ cấu trúc của ứng dụng việc học:

```text
study_app/
├── __init__.py
├── models.py   # định nghĩa Task
├── manager.py  # quản lý danh sách Task
├── storage.py  # lưu/đọc JSON
└── cli.py      # đọc lệnh người dùng
```

Sơ đồ luồng chạy:

```text
Bạn gõ lệnh
    ↓
cli.py       nhận lệnh add/list/done
    ↓
manager.py   thêm hoặc hoàn thành công việc
    ↓
models.py    chứa dữ liệu và hành vi của từng công việc
    ↓
storage.py   lưu dữ liệu để lần sau vẫn còn
```

Tại sao tách file? Nếu sau này đổi cách lưu từ JSON sang cơ sở dữ liệu, ta chủ yếu sửa phần lưu dữ liệu, không cần nhét tất cả logic vào một file duy nhất.

### CLI và `argparse`

CLI là cách điều khiển ứng dụng bằng lệnh thay vì bấm nút trên cửa sổ.

Ví dụ trong ứng dụng việc học:

```bash
python -m study_app.cli add "Ôn Python"
python -m study_app.cli list
python -m study_app.cli done 1
```

- `add`: thêm công việc.
- `list`: xem danh sách.
- `done 1`: đánh dấu công việc số 1 đã hoàn thành.

`argparse` đọc chữ bạn gõ, tách thành lệnh và tham số. Nó cũng báo lỗi nếu thiếu tham số bắt buộc hoặc tham số số không hợp lệ.

### Môi trường ảo và dependency

- **venv** tạo môi trường Python riêng cho dự án.
- **pip** cài các thư viện cần dùng.
- **pyproject.toml** lưu cấu hình và khai báo công cụ/dependency của dự án.

Đây là cách bắt đầu dự án nhỏ mà không làm lẫn thư viện của các dự án khác:

```bash
python -m venv .venv
python -m pip install --upgrade pip
```

Ứng dụng ví dụ trong repository chỉ dùng thư viện chuẩn Python, nên không cần cài thư viện ngoài để chạy.

### HTTP, request/response và JSON

Khi ứng dụng cần lấy thời khóa biểu từ máy chủ, luồng trao đổi có thể là:

```text
Ứng dụng -- GET request --> Máy chủ thời khóa biểu
Ứng dụng <-- status + JSON body -- Máy chủ
```

- **Request** là yêu cầu gửi đi.
- **Response** là câu trả lời.
- **GET** thường dùng để lấy dữ liệu.
- **JSON** là định dạng dữ liệu phổ biến giữa các hệ thống.
- **Status 200** thường biểu thị thành công; **404** là không tìm thấy; **500** là lỗi phía máy chủ.
- Lỗi mạng/timeout và JSON không hợp lệ phải được xử lý, không nên giả sử mọi request đều thành công.

Ví dụ parse một response JSON có sẵn (không kết nối mạng):

```python
from bot_course.http_foundation import parse_json_response

body = b'{"subject": "Python", "room": "A101"}'
data = parse_json_response(200, body)

print(data["subject"])  # Python
print(data["room"])     # A101
```

Các bài Week 13 dùng fixture ngoại tuyến để dễ kiểm tra. Chúng không gọi dịch vụ sản xuất hay đòi endpoint, token hoặc tài khoản thật.

## 3. Week 14 — mô hình hóa dữ liệu với OOP

### Class, object, attribute và method

Hãy nghĩ về **class như bản thiết kế công việc**, còn **object là một công việc cụ thể**.

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True

    def __str__(self):
        status = "xong" if self.done else "chưa xong"
        return f"{self.title}: {status}"


task = Task("Ôn Python")
print(task)          # Ôn Python: chưa xong
task.complete()
print(task)          # Ôn Python: xong
```

Cách hiểu:
- `Task` là class.
- `Task("Ôn Python")` tạo một object.
- `title` và `done` là attribute.
- `complete()` là method.
- `__init__` khởi tạo dữ liệu khi tạo object.
- `self` là object hiện tại.
- `__str__` điều khiển cách object hiển thị khi `print()`.

### Encapsulation — đặt dữ liệu và hành động đúng chỗ

Thông tin tên công việc và trạng thái hoàn thành cùng nằm trong `Task`; cách đánh dấu hoàn thành cũng ở đó. Điều này giúp tránh việc xử lý trạng thái rải rác khắp chương trình.

### Composition — một object quản lý các object khác

Một `TaskManager` có thể chứa danh sách các `Task`. Đây là quan hệ “có/đang sử dụng” (has-a/uses-a):

```python
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def show_all(self):
        for task in self.tasks:
            print(task)


manager = TaskManager()
manager.add(Task("Ôn Python"))
manager.add(Task("Làm bài OOP"))
manager.show_all()
```

`TaskManager` không cần kế thừa từ `Task`: nó không phải là một công việc, mà **quản lý các công việc**. Đây là ví dụ đời sống rõ ràng của composition.

### Inheritance — tạo một loại công việc cụ thể

Giả sử bài tập về nhà cần lưu thêm tên môn học. `HomeworkTask` là một loại `Task`, nên có thể kế thừa:

```python
class HomeworkTask(Task):
    def __init__(self, title, subject):
        super().__init__(title)
        self.subject = subject

    def __str__(self):
        return f"[{self.subject}] {super().__str__()}"


homework = HomeworkTask("Làm bài số 3", "Python")
print(homework)
```

- `HomeworkTask(Task)`: class con kế thừa từ `Task`.
- `super().__init__(title)`: gọi phần khởi tạo của class cha.
- `subject`: dữ liệu riêng của bài tập.

**Mẹo nhớ:** “một công việc quản lý nhiều công việc” là composition; “bài tập về nhà là một loại công việc” là inheritance.

## 4. Khi ghép hai tuần, chương trình hoạt động ra sao?

```text
Người dùng chạy CLI (Week 13)
        ↓
CLI phân tích tham số bằng argparse (Week 13)
        ↓
Tạo Task object hoặc gọi TaskManager (Week 14)
        ↓
TaskManager thêm/đánh dấu công việc (Week 14)
        ↓
Storage lưu JSON (module riêng, Week 13)
        ↓
CLI in kết quả
```

Nếu sau này muốn đồng bộ danh sách với máy chủ, có thể thêm một HTTP adapter (Week 13). Phần mô hình `Task` và logic quản lý công việc vẫn có thể được giữ riêng.

## 5. Bảng ôn nhanh

| Tuần | Khái niệm | Ứng dụng trong app việc học |
|---|---|---|
| 13 | Module | Tách mã thành `cli.py`, `models.py`, `storage.py` |
| 13 | Package | Gom các file vào `study_app/` |
| 13 | Import | Dùng `Task` từ `models.py` ở file khác |
| 13 | Main guard | Chạy CLI đúng lúc, không tự chạy khi import |
| 13 | venv/pip | Quản lý môi trường và thư viện |
| 13 | CLI/argparse | Nhận lệnh `add`, `list`, `done` |
| 13 | HTTP/JSON | Trao đổi hoặc đồng bộ dữ liệu với máy chủ |
| 14 | Class/Object | Mô tả một công việc cụ thể |
| 14 | `__init__`/`self` | Khởi tạo và lưu thông tin công việc |
| 14 | Method | Đánh dấu công việc hoàn thành |
| 14 | `__str__` | In công việc thành dòng dễ đọc |
| 14 | Composition | `TaskManager` chứa nhiều `Task` |
| 14 | Inheritance | `HomeworkTask` là một loại `Task` |

## 6. Chạy thử bài học

Từ thư mục gốc repository:

```bash
python weeks/week-13-modules-cli-api/exercises/ex01_modules.py
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
python weeks/week-13-modules-cli-api/checks/check_week.py
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
python weeks/week-14-oop-essentials/checks/check_week.py
```

Với các bài trong thư mục `exercises` của Week 13, làm theo hướng dẫn ở [README bài tập](week-13-modules-cli-api/exercises/README.md) để chạy bằng `python -m`.

**Chỉ cần nhớ:** Week 13 dạy cách chia chương trình và giao tiếp với bên ngoài; Week 14 dạy cách tổ chức dữ liệu và hành vi bên trong chương trình.
