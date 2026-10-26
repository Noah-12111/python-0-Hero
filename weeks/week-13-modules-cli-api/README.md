# Tuần 13 — Module, Package, CLI và API/HTTP

Tuần này học cách chia code thành file có trách nhiệm rõ ràng, nhận lệnh từ terminal và hiểu cách chương trình trao đổi dữ liệu qua HTTP.

## Học theo thứ tự

1. Đọc [lý thuyết và ví dụ đời sống](notes.md).
2. Hoàn thành ba bài trong [exercises](exercises/README.md).
3. Xem package mẫu trong `bot_course/`.
4. Chạy [mini-project](mini-project/README.md).
5. Chạy lệnh kiểm tra.

## Lệnh chạy nhanh

```bash
cd weeks/week-13-modules-cli-api
python -m exercises.ex01_modules
python -m exercises.ex02_cli --turn 3
python -m exercises.ex03_http
cd ../..
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
python weeks/week-13-modules-cli-api/checks/check_week.py
```

Bài HTTP dùng response fixture; không yêu cầu kết nối mạng.

## Ôn chung Week 13 và Week 14

Mời đọc tài liệu [tổng hợp hai tuần bằng ví dụ ứng dụng quản lý việc học](../week-13-14-review.md). Tài liệu giải thích cách module/package và CLI của Week 13 kết hợp với class/object, composition và inheritance của Week 14.
