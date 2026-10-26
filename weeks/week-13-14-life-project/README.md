# Mini-project đời sống — Study Task Manager

Một ứng dụng nhỏ quản lý việc học, kết hợp kiến thức Week 13 và Week 14. Dự án chỉ dùng thư viện chuẩn Python, không cần mạng và không cần cài thêm dependency.

## Chức năng

- Thêm công việc học tập.
- Thêm bài tập có kèm tên môn học.
- Xem danh sách công việc.
- Đánh dấu công việc hoàn thành.
- Lưu dữ liệu vào file JSON trong thư mục home của người dùng để chạy lần sau vẫn giữ dữ liệu.

## Chạy

Từ thư mục gốc repository:

```bash
cd weeks/week-13-14-life-project
python -m study_app.cli add "Ôn OOP"
python -m study_app.cli add "Làm bài số 3" --subject Python
python -m study_app.cli list
python -m study_app.cli done 1
python -m study_app.cli list
```

Ví dụ kết quả có thể tương tự:

```text
1. [ ] Ôn OOP
2. [Python] [ ] Làm bài số 3
Marked task 1 as complete.
1. [x] Ôn OOP
2. [Python] [ ] Làm bài số 3
```

## Week 13 nằm ở đâu?

- `study_app/` là package.
- `models.py`, `manager.py`, `storage.py`, `cli.py` là các module.
- `argparse` đọc lệnh.
- `storage.py` đọc/ghi JSON bằng thư viện chuẩn Python.
- `if __name__ == "__main__"` chạy CLI khi gọi module.

## Week 14 nằm ở đâu?

- `Task` là class; mỗi công việc cụ thể là object.
- `__init__` lưu tiêu đề và trạng thái; `self` là object hiện tại.
- `complete()` là method và `__str__` tạo nội dung dễ đọc.
- `TaskManager` chứa nhiều `Task` — composition.
- `HomeworkTask` là một loại `Task` — inheritance.

Đây là chương trình học tập mẫu để thực hành, không phải ứng dụng production.
