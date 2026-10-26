# Mini-project — Bot đổi strategy

Ví dụ nhỏ dùng **composition**: `Bot` nhận một hàm strategy khi tạo object. Mỗi strategy trả về một action trong ba action hợp lệ của bài: `left`, `right`, `wait`.

Chạy từ thư mục gốc repository:

```bash
python weeks/week-14-oop-essentials/mini-project/bot_demo.py
```

Chương trình sẽ minh họa:
- goal ở bên phải (`goal = 4`) thì bot di chuyển `right`;
- goal ở bên trái (`goal = 0`) thì bot di chuyển `left`;
- defensive đứng yên (`wait`) khi đối thủ ở ngay cạnh;
- đổi strategy bằng cách tạo `Bot(strategy)` mới, không sửa class `Bot`.

Đây là **line arena riêng của khóa học**, không phải cam kết về quy tắc của một dịch vụ bên ngoài.
