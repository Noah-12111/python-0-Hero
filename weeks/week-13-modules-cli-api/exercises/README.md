# Chạy exercises Week 13

Mở terminal ở thư mục gốc repository, sau đó chạy:

```bash
cd weeks/week-13-modules-cli-api
python -m exercises.ex01_modules
python -m exercises.ex02_cli --turn 3
python -m exercises.ex03_http
```

Dùng `python -m` vì các bài import package `bot_course` nằm ở cùng tuần. Cách này giúp Python tìm đúng package mà không cần sửa `sys.path` trong từng bài.

## Kết quả mong đợi

- Bài 1: in ra action `right` khi position là 1 và goal là 4.
- Bài 2: in ra `Current turn: 3`. Nếu không truyền `--turn`, argparse báo thiếu tham số.
- Bài 3: đọc JSON fixture thành dictionary rồi xử lý status 500 bằng `ValueError`. Các bài này **không gọi mạng**.

Sau đó quay lại thư mục gốc để chạy lệnh kiểm tra:

```bash
python weeks/week-13-modules-cli-api/checks/check_week.py
```
