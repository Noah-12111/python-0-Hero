"""Exercise: class, object and methods."""

class Progress:
    def __init__(self, completed, total):
        if total <= 0:
            raise ValueError("total phải lớn hơn 0")

        self.completed = completed
        self.total = total

    def percentage(self):
        return self.completed / self.total * 100

    def __str__(self):
        return f"Tiến độ: {self.completed}/{self.total} ({self.percentage():.1f}%)"


class DienThoai:
    def __init__(self, mamay, tenmay, hangsanxuat, dungluongpin, giaban):
        self.MaMay = mamay
        self.TenMay = tenmay
        self.HangSanXuat = hangsanxuat
        self.DungLuongPin = dungluongpin
        self.GiaBan = giaban

    def thongtindienthoai(self):
        print("Mã máy:", self.MaMay)
        print("Tên máy:", self.TenMay)
        print("Hãng sản xuất:", self.HangSanXuat)
        print("Dung lượng pin:", self.DungLuongPin, "mAh")
        print("Giá bán:", f"{self.GiaBan:,} VND")
        print()


# Ví dụ 1: tạo object Progress và in tiến độ.
progress = Progress(3, 4)
print(progress)
print("Phần trăm hoàn thành:", f"{progress.percentage():.1f}%")
print()

# Ví dụ 2: tạo hai object DienThoai.
dt01 = DienThoai("DT01", "iPhone 15 Pro", "Apple", 3274, 28990000)
dt02 = DienThoai("DT02", "Galaxy S24 Ultra", "Samsung", 5000, 29990000)

dt01.thongtindienthoai()
dt02.thongtindienthoai()
