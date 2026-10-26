# Week 13 — Module, package, CLI và HTTP (dễ hiểu)

Hãy lấy ví dụ **một ứng dụng nhắc việc học**. Ứng dụng có thể cần lưu thông tin công việc, nhận lệnh từ người dùng và sau này đồng bộ dữ liệu với một dịch vụ khác.

## 1. Module và package

- **Module**: một file Python `.py`.
- **Package**: một thư mục gom các module liên quan; thường có file `__init__.py`.
- **Import**: dùng code đã viết ở module khác thay vì chép lại.

Ví dụ cấu trúc:

```text
study_app/
├── __init__.py
├── tasks.py      # xử lý công việc học tập
├── storage.py    # đọc/ghi dữ liệu
└── cli.py        # nhận lệnh từ người dùng
```

Sơ đồ đời sống:

```text
Bạn gõ lệnh → cli.py → tasks.py → trả kết quả
                         ↕
                      storage.py
```

Tách file giúp khi sửa cách lưu dữ liệu, ta không cần viết lại toàn bộ phần nhận lệnh.

Ví dụ import:

```python
from bot_course.core import choose_action

print(choose_action(position=1, goal=4))  # right
```

## 2. `if __name__ == "__main__"`

Dùng để chỉ chạy phần demo khi chạy file trực tiếp theo cách module phù hợp. Khi file được import, đoạn bên trong guard không tự chạy.

```python
def main():
    print("Study app is ready")


if __name__ == "__main__":
    main()
```

## 3. Môi trường ảo và thư viện

Môi trường ảo giúp các dự án dùng những bộ thư viện riêng, tránh làm lẫn phiên bản.

```bash
python -m venv .venv
python -m pip install --upgrade pip
```

Trên Windows, bật môi trường ảo bằng `.venv\\Scripts\\activate`. Trên macOS/Linux, dùng `source .venv/bin/activate`.

- `pip`: cài thư viện Python.
- `pyproject.toml`: ghi cấu hình dự án và công cụ.
- `python -m pip`: chạy pip thuộc đúng Python interpreter đang dùng.

## 4. CLI — điều khiển chương trình bằng lệnh

CLI là giao diện dòng lệnh. Nó tiện khi muốn chạy một tác vụ nhanh, tự động hóa hoặc viết script.

Ví dụ:

```bash
python -m exercises.ex02_cli --turn 3
```

Kết quả:

```text
Current turn: 3
```

Trong ứng dụng đời sống, CLI có thể nhận `--task "Ôn Python"`, `--date 2026-10-26` hoặc `--turn 3`. `argparse` giúp chuyển chuỗi người dùng gõ thành giá trị có kiểu rõ ràng, ví dụ `int`.

## 5. HTTP — cách hai chương trình trao đổi dữ liệu

Ví dụ ứng dụng lịch học hỏi một máy chủ về thời khóa biểu:

```text
Ứng dụng của bạn -- GET request --> Máy chủ
Ứng dụng của bạn <-- status + JSON response -- Máy chủ
```

- **Request**: yêu cầu gửi đi.
- **Response**: phản hồi nhận về.
- **GET**: thường dùng để lấy dữ liệu.
- **Status code**: cho biết kết quả yêu cầu.
- **JSON**: định dạng dữ liệu phổ biến để trao đổi giữa các hệ thống.

Một vài status dễ nhớ:

| Status | Hiểu đơn giản |
|---|---|
| `200` | Thành công |
| `404` | Không tìm thấy tài nguyên |
| `500` | Máy chủ gặp lỗi |

JSON sau khi parse có thể thành dictionary Python:

```python
from bot_course.http_foundation import parse_json_response

body = b'{"subject": "Python", "room": "A101"}'
data = parse_json_response(200, body)

print(data["subject"])  # Python
```

Bài học dùng dữ liệu mẫu để kiểm tra offline; **không cần kết nối mạng**. Ứng dụng thật cần chuẩn bị cho timeout, lỗi kết nối, status ngoài 2xx và JSON sai định dạng. Không nên giả định rằng mọi request đều thành công.

## 6. Tách phần xử lý chính khỏi giao tiếp bên ngoài

```text
CLI / HTTP adapter → Bot Core → kết quả
```

Core là phần xử lý quyết định. CLI giúp người dùng chạy chương trình; HTTP adapter giúp giao tiếp qua mạng. Hai lớp giao tiếp có thể thay đổi mà không cần viết lại quyết định lõi.

Trong bài của khóa học, `bot_course/core.py` chỉ nhận vị trí và mục tiêu rồi trả `left`, `right` hoặc `wait`. Ví dụ này là **hợp đồng riêng của khóa học**, không phải API sản xuất của một dịch vụ bên ngoài.

## 7. Chạy các bài Week 13

Chạy từ thư mục gốc repository:

```bash
cd weeks/week-13-modules-cli-api
python -m exercises.ex01_modules
python -m exercises.ex02_cli --turn 3
python -m exercises.ex03_http
cd ../..
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
python weeks/week-13-modules-cli-api/checks/check_week.py
```

Tóm lại: **module/package chia code thành phần nhỏ; CLI nhận lệnh; HTTP giúp trao đổi dữ liệu giữa các chương trình.**
