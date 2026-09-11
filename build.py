# -*- coding: utf-8 -*-
"""
Sinh các trang HTML tĩnh cho bwtbarrier.com.vn.
Chạy:  python build.py
Sửa nội dung/sản phẩm ở phần DỮ LIỆU rồi chạy lại là xong.
"""
import io, os, re, html, json, hashlib, datetime
from articles import ARTICLES

ROOT = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# DỮ LIỆU CHUNG
# ============================================================
SITE_NAME = "Trung tâm bảo hành BWT Barrier"
DOMAIN = "https://bwtbarrier.com.vn"

# >>> THÔNG TIN LIÊN HỆ — sửa 3 dòng dưới đây là đổi toàn site <<<
HOTLINE_TEXT = "0896 613 768"
HOTLINE_TEL = "0896613768"
ADDRESS = "90 Đinh Thị Thi, Hiệp Bình, Hồ Chí Minh"
MAP_LINK = "https://maps.app.goo.gl/h5tJqBYY9ZJqJzLB9"
MAP_EMBED = ("https://www.google.com/maps?q=10.845839,106.712965"
             "&amp;hl=vi&amp;z=17&amp;output=embed")

NAV = [
    ("index.html", "Trang chủ"),
    ("san-pham.html", "Sản phẩm"),
    ("ve-chung-toi.html", "Về chúng tôi"),
    ("bai-viet.html", "Bài viết"),
    ("lien-he.html", "Liên hệ"),
]

# ============================================================
# SẢN PHẨM
# ============================================================
PRODUCTS = [
    # ---------------- Máy lọc nước ----------------
    {
        "slug": "may-loc-nuoc-bwt-barrier-m",
        "name": "Máy lọc nước BWT Barrier M",
        "short": "Giàu dưỡng chất Mg+ và Zn, giữ khoáng tự nhiên, không dùng điện và không xả nước thải.",
        "cat": "may-loc",
        "cat_label": "Máy lọc nước",
        "price": "Liên hệ",
        "price_note": "Gọi hotline để nhận báo giá",
        "sibling": ("may-loc-nuoc-bwt-barrier-m-co-bo-dem", "Bản kèm bộ đếm Water Meter"),
        "images": [
            ("assets/img/bwt-barrier-m-hero.webp", "Máy lọc nước BWT Barrier M — bộ 3 lõi và vòi nước"),
        ],
        "usps": [
            "Công nghệ Magnesium Mineralizer bổ sung Mg+ theo bằng sáng chế châu Âu EP 2094611B1",
            "Giữ lại khoáng chất có lợi Ca, Mg, Zn thay vì lọc sạch trơ như công nghệ RO",
            "Không dùng điện, không nước thải — tiết kiệm điện nước và thân thiện môi trường",
            "Lõi đúc nguyên khối Smart Lock chống rò rỉ và tái nhiễm khuẩn",
            "Công nghệ One Touch: tự thay lõi tại nhà chỉ với một thao tác",
            "Lắp âm dưới chậu rửa, chỉ chiếm 240 x 150 x 330 mm",
        ],
        "specs": [
            ("Thương hiệu", "BWT Barrier"),
            ("Công nghệ lọc", "Ion-Exchange ByPass+, Magnesium Mineralizer, Nano Plus, Than hoạt tính tẩm bạc"),
            ("Công suất lọc định mức", "8.000 lít (khoảng 12 tháng sử dụng)"),
            ("Tốc độ tạo nước", "2 lít/phút"),
            ("Bộ đếm Water Meter", "Không kèm theo"),
            ("Điện áp", "Không sử dụng điện"),
            ("Nước thải", "Không có"),
            ("Kích thước (D x R x C)", "240 x 150 x 330 mm"),
            ("Trọng lượng", "3,334 kg"),
            ("Kiểu lắp đặt", "Âm dưới chậu rửa / trong tủ bếp"),
            ("Bảo hành", "36 tháng"),
        ],
        "intro": [
            "BWT Barrier M là mẫu máy lọc nước gia đình phổ biến của dòng BWT Barrier tại Việt Nam. "
            "Thay vì loại bỏ cả khoáng chất như màng RO, BWT Barrier M giữ lại canxi, magie và kẽm ở hàm lượng "
            "tối ưu, đồng thời bổ sung thêm Mg+ qua công nghệ Magnesium Mineralizer được cấp bằng sáng chế châu Âu.",
            "Cụm lọc được đúc nguyên khối và gắn nhanh theo cơ chế One Touch, nên bạn có thể tự thay lõi "
            "tại nhà trong chưa đầy một phút mà không cần dụng cụ, không lo rò rỉ hay nhiễm khuẩn ngược.",
        ],
        "best_for": "Hộ gia đình dùng nước máy đô thị, muốn nước uống giàu khoáng, lắp gọn trong tủ bếp.",
    },
    {
        "slug": "may-loc-nuoc-bwt-barrier-l",
        "name": "Máy lọc nước BWT Barrier L",
        "short": "Bản nâng cấp của dòng BWT Barrier: lõi 10.000 lít, dùng bền hơn khoảng 25% so với BWT Barrier M.",
        "cat": "may-loc",
        "cat_label": "Máy lọc nước",
        "price": "Liên hệ",
        "price_note": "Gọi hotline để nhận báo giá",
        "sibling": ("may-loc-nuoc-bwt-barrier-l-co-bo-dem", "Bản kèm bộ đếm Water Meter"),
        "images": [
            ("assets/img/bwt-barrier-l-hero.webp", "Máy lọc nước BWT Barrier L — bộ 3 lõi và vòi nước"),
        ],
        "usps": [
            "Tuổi thọ lõi 10.000 lít — dài hơn khoảng 25% so với bản BWT Barrier M",
            "Bộ lõi Ion-Exchange ByPass Plus + Nano Plus + than hoạt tính tẩm bạc",
            "Bổ sung magie, giữ vi khoáng có lợi, loại bỏ clo, kim loại nặng, vi khuẩn",
            "Không dùng điện, không nước thải, không cần bình áp",
            "Thay lõi One Touch, khoá Smart Lock chống rò rỉ",
            "Thiết kế âm tủ gọn gàng, chỉ chiếm 240 x 150 x 330 mm",
        ],
        "specs": [
            ("Thương hiệu", "BWT Barrier"),
            ("Công nghệ lọc", "Ion-Exchange ByPass Plus, Nano Plus, Silver-Impregnated Carbon"),
            ("Công suất lọc định mức", "10.000 lít (khoảng 12 tháng sử dụng)"),
            ("Tốc độ tạo nước", "2 lít/phút"),
            ("Bộ đếm Water Meter", "Không kèm theo"),
            ("Điện áp", "Không sử dụng điện"),
            ("Nước thải", "Không có"),
            ("Kích thước (D x R x C)", "240 x 150 x 330 mm"),
            ("Trọng lượng", "3,334 kg"),
            ("Kiểu lắp đặt", "Âm dưới chậu rửa / trong tủ bếp"),
            ("Bảo hành", "36 tháng"),
        ],
        "intro": [
            "BWT Barrier L là bản nâng cấp của dòng máy lọc nước âm tủ BWT Barrier. Cùng triết lý “lọc sạch nhưng "
            "giữ khoáng”, BWT Barrier L nâng tuổi thọ lõi lên 10.000 lít — tương đương khoảng 12 tháng cho hộ gia đình "
            "4 người, dài hơn bản BWT Barrier M khoảng một phần tư.",
            "Đây là lựa chọn phù hợp cho gia đình đông người hoặc văn phòng nhỏ, nơi lượng nước tiêu thụ mỗi ngày "
            "cao nên chi phí thay lõi theo năm là khoản đáng cân nhắc.",
        ],
        "best_for": "Gia đình đông người hoặc văn phòng nhỏ, cần lõi bền và ít phải thay.",
    },
    {
        "slug": "may-loc-nuoc-bwt-barrier-h",
        "name": "Máy lọc nước BWT Barrier H",
        "short": "Chuyên cho nước cứng: làm mềm nước, hạn chế cáu cặn canxi mà vẫn giữ khoáng Ca – Mg – K cân bằng.",
        "cat": "may-loc",
        "cat_label": "Máy lọc nước",
        "price": "Liên hệ",
        "price_note": "Gọi hotline để nhận báo giá",
        "sibling": ("may-loc-nuoc-bwt-barrier-h-co-bo-dem", "Bản kèm bộ đếm Water Meter"),
        "images": [
            ("assets/img/bwt-barrier-h-hero.webp", "Máy lọc nước BWT Barrier H — bộ 3 lõi làm mềm nước cứng"),
        ],
        "usps": [
            "Lõi Softening chuyên làm mềm nước cứng, hạn chế cáu cặn canxi",
            "Công nghệ Ion-Exchange ByPass+ giữ lại Ca, Mg, K ở ngưỡng có lợi thay vì khử sạch",
            "Loại bỏ clo dư, mùi vị lạ, kim loại nặng và vi khuẩn nhờ Nano-Plus và than hoạt tính tẩm bạc",
            "Bảo vệ ấm siêu tốc, bình đun, thiết bị gia dụng khỏi lớp cặn trắng bám đáy",
            "Không dùng điện, không nước thải, tốc độ 2 lít/phút",
            "Được trung tâm tiếp nhận bảo hành và hỗ trợ thay lõi tại nhà",
        ],
        "specs": [
            ("Thương hiệu", "BWT Barrier"),
            ("Công nghệ lọc", "Ion-Exchange ByPass+, Softening, Nano-Plus, Than hoạt tính tẩm bạc (Ag)"),
            ("Công suất lọc định mức", "8.000 lít (khoảng 12 tháng sử dụng)"),
            ("Tốc độ tạo nước", "2 lít/phút"),
            ("Bộ đếm Water Meter", "Không kèm theo"),
            ("Điện áp", "Không sử dụng điện"),
            ("Nước thải", "Không có"),
            ("Kích thước (D x R x C)", "240 x 150 x 330 mm"),
            ("Trọng lượng", "3,5 kg"),
            ("Kiểu lắp đặt", "Âm dưới chậu rửa / trong tủ bếp"),
            ("Bảo hành", "36 tháng"),
        ],
        "intro": [
            "Nhiều khu vực tại Việt Nam dùng nước giếng khoan hoặc nước máy có độ cứng cao: ấm đun đóng cặn trắng, "
            "nước pha trà nổi váng, thiết bị gia dụng nhanh hỏng. BWT Barrier H được thiết kế riêng cho tình huống này.",
            "Lõi số 2 Softening sử dụng hạt trao đổi ion kết hợp cơ chế ByPass+ — thay vì khử hết ion canxi và "
            "magie làm nước trở nên trơ, hệ thống chỉ đưa độ cứng về ngưỡng an toàn và giữ lại phần khoáng có lợi cho cơ thể.",
        ],
        "best_for": "Khu vực nước cứng, nước giếng khoan, hộ gia đình hay bị cáu cặn canxi ở ấm đun và vòi nước.",
    },

    # ---------------- Máy lọc nước có bộ đếm ----------------
    {
        "slug": "may-loc-nuoc-bwt-barrier-m-co-bo-dem",
        "name": "Máy lọc nước BWT Barrier M có bộ đếm",
        "short": "BWT Barrier M kèm bộ đếm Water Meter — hiển thị lượng nước đã lọc và thời điểm cần thay lõi.",
        "cat": "co-bo-dem",
        "cat_label": "Có bộ đếm",
        "price": "Liên hệ",
        "price_note": "Gọi hotline để nhận báo giá",
        "sibling": ("may-loc-nuoc-bwt-barrier-m", "Bản không kèm bộ đếm"),
        "images": [
            ("assets/img/bwt-barrier-m-meter-hero.webp", "Máy lọc nước BWT Barrier M kèm bộ đếm Water Meter"),
        ],
        "usps": [
            "Bộ đếm Water Meter đo lưu lượng thực tế, báo phần trăm tuổi thọ lõi còn lại",
            "Không phải nhớ ngày thay lõi — thiết bị nhắc theo lượng nước đã dùng",
            "Giữ nguyên bộ lõi 8.000 lít và công nghệ Magnesium Mineralizer của BWT Barrier M",
            "Giữ lại khoáng chất có lợi Ca, Mg, Zn thay vì lọc sạch trơ như công nghệ RO",
            "Không dùng điện, không nước thải, tốc độ 2 lít/phút",
            "Lắp âm dưới chậu rửa, thay lõi One Touch tại nhà",
        ],
        "specs": [
            ("Thương hiệu", "BWT Barrier"),
            ("Công nghệ lọc", "Ion-Exchange ByPass+, Magnesium Mineralizer, Nano Plus, Than hoạt tính tẩm bạc"),
            ("Công suất lọc định mức", "8.000 lít (khoảng 12 tháng sử dụng)"),
            ("Tốc độ tạo nước", "2 lít/phút"),
            ("Bộ đếm Water Meter", "Có — Cartridge Lifetime Monitor, gắn trên đường nước vào"),
            ("Điện áp", "Không sử dụng điện (bộ đếm dùng pin)"),
            ("Nước thải", "Không có"),
            ("Kích thước (D x R x C)", "240 x 150 x 330 mm"),
            ("Trọng lượng", "3,334 kg (chưa gồm bộ đếm)"),
            ("Kiểu lắp đặt", "Âm dưới chậu rửa / trong tủ bếp"),
            ("Bảo hành", "36 tháng"),
        ],
        "intro": [
            "Đây là bản BWT Barrier M đi kèm bộ đếm Water Meter — thiết bị đo lưu lượng gắn trực tiếp trên đường nước "
            "vào máy. Màn hình hiển thị lượng nước đã lọc và phần tuổi thọ lõi còn lại, thay cho việc phải nhớ "
            "ngày lắp và ước lượng bằng cảm tính.",
            "Thay lõi muộn là lỗi thường gặp khiến nước đầu ra không còn đạt chất lượng như thiết kế. Với hộ gia "
            "đình dùng nước không đều giữa các tháng, bộ đếm giúp canh đúng thời điểm thay hơn là đếm theo lịch.",
        ],
        "best_for": "Hộ gia đình muốn theo dõi tuổi thọ lõi tự động, dùng nước không đều giữa các tháng.",
    },
    {
        "slug": "may-loc-nuoc-bwt-barrier-l-co-bo-dem",
        "name": "Máy lọc nước BWT Barrier L có bộ đếm",
        "short": "BWT Barrier L lõi 10.000 lít kèm bộ đếm Water Meter theo dõi tuổi thọ lõi theo thời gian thực.",
        "cat": "co-bo-dem",
        "cat_label": "Có bộ đếm",
        "price": "Liên hệ",
        "price_note": "Gọi hotline để nhận báo giá",
        "sibling": ("may-loc-nuoc-bwt-barrier-l", "Bản không kèm bộ đếm"),
        "images": [
            ("assets/img/bwt-barrier-l-meter-hero.webp", "Máy lọc nước BWT Barrier L kèm bộ đếm Water Meter"),
        ],
        "usps": [
            "Cấu hình đầy đủ của dòng BWT Barrier: lõi 10.000 lít cộng bộ đếm Water Meter",
            "Bộ đếm hiển thị chính xác lượng nước đã lọc và thời điểm cần thay lõi",
            "Bộ lõi Ion-Exchange ByPass Plus + Nano Plus + than hoạt tính tẩm bạc",
            "Bổ sung magie, giữ vi khoáng có lợi, loại bỏ clo, kim loại nặng, vi khuẩn",
            "Không dùng điện, không nước thải, không cần bình áp",
            "Thiết kế âm tủ gọn gàng, chỉ chiếm 240 x 150 x 330 mm",
        ],
        "specs": [
            ("Thương hiệu", "BWT Barrier"),
            ("Công nghệ lọc", "Ion-Exchange ByPass Plus, Nano Plus, Silver-Impregnated Carbon"),
            ("Công suất lọc định mức", "10.000 lít (khoảng 12 tháng sử dụng)"),
            ("Tốc độ tạo nước", "2 lít/phút"),
            ("Bộ đếm Water Meter", "Có — Cartridge Lifetime Monitor, gắn trên đường nước vào"),
            ("Điện áp", "Không sử dụng điện (bộ đếm dùng pin)"),
            ("Nước thải", "Không có"),
            ("Kích thước (D x R x C)", "240 x 150 x 330 mm"),
            ("Trọng lượng", "3,334 kg (chưa gồm bộ đếm)"),
            ("Kiểu lắp đặt", "Âm dưới chậu rửa / trong tủ bếp"),
            ("Bảo hành", "36 tháng"),
        ],
        "intro": [
            "BWT Barrier L có bộ đếm là cấu hình đầy đủ của dòng máy lọc nước âm tủ BWT Barrier: lõi tuổi thọ "
            "10.000 lít đi cùng bộ đếm Water Meter gắn trực tiếp trên đường nước.",
            "Với gia đình đông người hoặc văn phòng nhỏ, lượng nước tiêu thụ mỗi ngày cao và việc theo dõi tuổi "
            "thọ lõi bằng cảm tính dễ dẫn tới thay muộn — bộ đếm giải quyết đúng điểm này.",
        ],
        "best_for": "Gia đình đông người hoặc văn phòng nhỏ, cần lõi bền và muốn theo dõi tuổi thọ lõi tự động.",
    },
    {
        "slug": "may-loc-nuoc-bwt-barrier-h-co-bo-dem",
        "name": "Máy lọc nước BWT Barrier H có bộ đếm",
        "short": "BWT Barrier H làm mềm nước cứng, kèm bộ đếm Water Meter báo thời điểm thay lõi.",
        "cat": "co-bo-dem",
        "cat_label": "Có bộ đếm",
        "price": "Liên hệ",
        "price_note": "Gọi hotline để nhận báo giá",
        "sibling": ("may-loc-nuoc-bwt-barrier-h", "Bản không kèm bộ đếm"),
        "images": [
            ("assets/img/bwt-barrier-h-meter-hero.webp", "Máy lọc nước BWT Barrier H kèm bộ đếm Water Meter"),
        ],
        "usps": [
            "Lõi Softening chuyên làm mềm nước cứng, hạn chế cáu cặn canxi",
            "Bộ đếm Water Meter báo thời điểm thay lõi theo lượng nước thực tế",
            "Ion-Exchange ByPass+ giữ lại Ca, Mg, K ở ngưỡng có lợi thay vì khử sạch",
            "Loại bỏ clo dư, mùi vị lạ, kim loại nặng và vi khuẩn",
            "Bảo vệ ấm siêu tốc, bình đun, thiết bị gia dụng khỏi lớp cặn trắng bám đáy",
            "Không dùng điện, không nước thải, tốc độ 2 lít/phút",
        ],
        "specs": [
            ("Thương hiệu", "BWT Barrier"),
            ("Công nghệ lọc", "Ion-Exchange ByPass+, Softening, Nano-Plus, Than hoạt tính tẩm bạc (Ag)"),
            ("Công suất lọc định mức", "8.000 lít (khoảng 12 tháng sử dụng)"),
            ("Tốc độ tạo nước", "2 lít/phút"),
            ("Bộ đếm Water Meter", "Có — Cartridge Lifetime Monitor, gắn trên đường nước vào"),
            ("Điện áp", "Không sử dụng điện (bộ đếm dùng pin)"),
            ("Nước thải", "Không có"),
            ("Kích thước (D x R x C)", "240 x 150 x 330 mm"),
            ("Trọng lượng", "3,5 kg (chưa gồm bộ đếm)"),
            ("Kiểu lắp đặt", "Âm dưới chậu rửa / trong tủ bếp"),
            ("Bảo hành", "36 tháng"),
        ],
        "intro": [
            "Bản BWT Barrier H đi kèm bộ đếm Water Meter. Với nguồn nước cứng, lõi làm mềm chịu tải nặng hơn bình "
            "thường nên tuổi thọ thực tế có thể ngắn hơn con số 8.000 lít trên lý thuyết.",
            "Bộ đếm đo lưu lượng thật đi qua máy, nhờ đó bạn biết chính xác khi nào cần thay lõi thay vì ước "
            "lượng theo lịch — điều khá quan trọng ở khu vực nước giếng khoan.",
        ],
        "best_for": "Khu vực nước cứng, nước giếng khoan, muốn theo dõi tuổi thọ lõi bằng số liệu thực tế.",
    },

    # ---------------- Bộ tiền xử lý ----------------
    {
        "slug": "bo-tien-xu-ly-bwt-barrier-ion-m",
        "name": "Bộ tiền xử lý nước BWT Barrier ion M",
        "short": "Bộ tiền lọc chuyên dụng cho máy điện giải ion kiềm — cân bằng pH và chống bám cặn điện cực.",
        "cat": "tien-xu-ly",
        "cat_label": "Bộ tiền xử lý",
        "price": "Liên hệ",
        "price_note": "Gọi hotline để nhận báo giá",
        "sibling": None,
        "images": [
            ("assets/img/ion-m-hero.webp", "Hộp bộ tiền xử lý nước BWT Barrier ion M"),
        ],
        "usps": [
            "Cân bằng pH nước đầu vào, giúp máy điện giải đạt hiệu suất điện phân cao hơn tới 3 lần",
            "Công nghệ iON-Exchange ByPass Plus chống bám cặn trên tấm điện cực, tăng tuổi thọ máy gấp 3 lần",
            "Tối ưu hàm lượng khoáng Canxi, Magie, Kẽm cho nước ion kiềm đầu ra",
            "Nano Plus và than hoạt tính tẩm bạc loại bỏ clo dư, vi khuẩn, vi rút",
            "Không dùng điện, không nước thải, lắp âm dưới chậu hoặc trong tủ",
            "One Touch thay lõi nhanh, Smart Lock chống rò rỉ",
        ],
        "specs": [
            ("Thương hiệu", "BWT Barrier"),
            ("Công nghệ lọc", "iON-Exchange ByPass Plus, Nano Plus, Silver Impregnated Carbon, iON-Exchange Fiber"),
            ("Công suất lọc định mức", "10.000 lít (khoảng 12 tháng sử dụng)"),
            ("Điện áp", "Không sử dụng điện"),
            ("Nước thải", "Không có"),
            ("Kích thước (D x R x C)", "240 x 150 x 330 mm"),
            ("Trọng lượng", "3,334 kg"),
            ("Kiểu lắp đặt", "Âm dưới chậu / trong tủ / cạnh bồn"),
            ("Tương thích", "Hầu hết máy lọc nước ion kiềm phổ biến trên thị trường"),
            ("Bảo hành", "36 tháng"),
        ],
        "intro": [
            "Máy điện giải ion kiềm chỉ hoạt động tốt khi nguồn nước đầu vào đủ sạch và có độ pH phù hợp. Nếu nước "
            "đầu vào còn clo dư, cặn canxi hay độ cứng cao, tấm điện cực sẽ đóng cặn rất nhanh — hiệu suất điện phân "
            "giảm dần và chi phí sửa chữa buồng điện phân là khoản đắt nhất của một chiếc máy ion kiềm.",
            "Bộ tiền xử lý BWT Barrier ion M giải quyết đúng điểm này: xử lý nguồn nước trước khi vào máy, cân bằng pH, "
            "chống bám cặn điện cực, đồng thời vẫn giữ lại nhóm khoáng Ca – Mg – Zn cần thiết cho quá trình điện phân.",
        ],
        "best_for": "Nhà đang dùng máy lọc nước ion kiềm với nguồn nước máy đô thị, muốn bảo vệ buồng điện phân.",
    },
    {
        "slug": "bo-tien-xu-ly-bwt-barrier-ion-h",
        "name": "Bộ tiền xử lý nước BWT Barrier ion H",
        "short": "Phiên bản dành cho khu vực nước cứng — làm mềm nước trước khi vào máy điện giải ion kiềm.",
        "cat": "tien-xu-ly",
        "cat_label": "Bộ tiền xử lý",
        "price": "Liên hệ",
        "price_note": "Gọi hotline để nhận báo giá",
        "sibling": None,
        "images": [
            ("assets/img/ion-h-hero.webp", "Hộp bộ tiền xử lý nước BWT Barrier ion H"),
        ],
        "usps": [
            "Làm mềm nước cứng trước khi vào máy điện giải — chống cáu cặn canxi trên buồng điện phân",
            "iON-Exchange ByPass Plus giữ lại khoáng tự nhiên thay vì khử sạch làm nước trơ",
            "Nano Plus và than hoạt tính tẩm bạc loại bỏ clo, vi khuẩn, vi rút",
            "Cân bằng pH nước đầu vào, tăng cường hiệu suất điện phân tạo nước giàu hydro",
            "Nâng tuổi thọ máy điện giải lên gấp khoảng 3 lần",
            "Không dùng điện, không nước thải, thiết kế nguyên khối âm tủ",
        ],
        "specs": [
            ("Thương hiệu", "BWT Barrier"),
            ("Công nghệ lọc", "iON-Exchange ByPass Plus, Softening, Nano Plus, Silver Impregnated Carbon"),
            ("Công suất lọc định mức", "10.000 lít (khoảng 12 tháng sử dụng)"),
            ("Điện áp", "Không sử dụng điện"),
            ("Nước thải", "Không có"),
            ("Kích thước (D x R x C)", "240 x 150 x 330 mm"),
            ("Trọng lượng", "3,5 kg"),
            ("Kiểu lắp đặt", "Âm dưới chậu / trong tủ / cạnh bồn"),
            ("Tương thích", "Hầu hết máy lọc nước ion kiềm phổ biến trên thị trường"),
            ("Bảo hành", "36 tháng"),
        ],
        "intro": [
            "BWT Barrier ion H là bản “nước cứng” của bộ tiền xử lý BWT Barrier. Cấu hình lõi được thay đổi để ưu tiên "
            "làm mềm nước — phù hợp với các khu vực dùng nước giếng khoan hoặc nước máy có độ cứng cao, nơi buồng "
            "điện phân của máy ion kiềm rất nhanh đóng cặn trắng.",
            "Sau khi qua bộ tiền xử lý, nước vào máy điện giải đã được khử clo, giảm độ cứng về ngưỡng an toàn và "
            "cân bằng pH, nhưng vẫn còn nguyên nhóm khoáng cần thiết để quá trình điện phân diễn ra hiệu quả.",
        ],
        "best_for": "Khu vực nước cứng, nước giếng khoan đang dùng máy điện giải ion kiềm.",
    },
]

PRODUCT_BY_SLUG = dict((p["slug"], p) for p in PRODUCTS)


# ============================================================
# ICON SVG
# ============================================================
IC = {
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1l-2.3 2.2z"/></svg>',
    "search": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 3a7 7 0 105.3 11.6l4.6 4.6 1.4-1.4-4.6-4.6A7 7 0 0010 3zm0 2a5 5 0 110 10 5 5 0 010-10z"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 5.9 2 10.7c0 2.7 1.4 5.1 3.7 6.7L5 22l4.4-2.3c.8.2 1.7.3 2.6.3 5.5 0 10-3.9 10-8.7S17.5 2 12 2z"/></svg>',
    "up": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5l7 7-1.4 1.4L13 8.8V20h-2V8.8l-4.6 4.6L5 12z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9-4.8-.7-8-4.5-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/></svg>',
    "drop": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3c3.5 4 6 7.2 6 10a6 6 0 11-12 0c0-2.8 2.5-6 6-10z"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4C10 4 4 8 4 15c0 2 .6 3.6 1.6 5C9 14 13 11 18 10c-4 2.5-7 5.5-9 10 8 1 11-4 11-16z"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2L4 14h6l-1 8 9-12h-6z"/></svg>',
    "tool": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.7 6.3a4 4 0 01-5.4 5.4L4 17v3h3l5.3-5.3a4 4 0 015.4-5.4l-2.4 2.4-1.6-1.6 2.4-2.4z"/></svg>',
    "award": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="9" r="6"/><path d="M9 14l-2 8 5-3 5 3-2-8"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14 0 18-3-4-3-14.5 0-18z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6.3 7-11a7 7 0 10-14 0c0 4.7 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/></svg>',
    "box": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8"/><path d="M12 13v8"/></svg>',
    "filter": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18l-7 8v6l-4 2v-8z"/></svg>',
    "chevron": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>',
    "cal": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
    "flask": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 2v7.31L4.14 20.3A2 2 0 005.86 23h12.28a2 2 0 001.72-2.7L14 9.31V2h-4zM8.5 2h7M7 16h10"/></svg>',
    "clipboard": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 4h2a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V6a2 2 0 012-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>',
    "sparkles": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.4 7.2L22 12l-7.6 2.8L12 22l-2.4-7.2L2 12l7.6-2.8z"/></svg>',
}

def logo_img(white=False):
    """Logo BARRIER chính thức. white=True dùng cho nền tối (footer)."""
    f = "barrier-logo-white.webp" if white else "barrier-logo.webp"
    return ('<img class="logo__img" src="assets/img/{f}" width="1200" height="225" '
            'alt="BARRIER — BWT Water Filters">').format(f=f)


# ============================================================
# KHUNG TRANG
# ============================================================
_DIMS = {}


def dims(src):
    """Tra ve width/height that cua anh de tranh CLS. Dung Pillow neu co."""
    if src not in _DIMS:
        try:
            from PIL import Image as _I
            with _I.open(os.path.join(ROOT, src.replace("/", os.sep))) as im:
                _DIMS[src] = ' width="%d" height="%d"' % im.size
        except Exception:
            _DIMS[src] = ""
    return _DIMS[src]


_VER = {}


def v(path):
    """?v=<hash noi dung> cho CSS/JS — de cache 1 nam ma van cap nhat ngay khi sua."""
    if path not in _VER:
        try:
            with open(os.path.join(ROOT, path.replace("/", os.sep)), "rb") as f:
                _VER[path] = "?v=" + hashlib.md5(f.read()).hexdigest()[:8]
        except Exception:
            _VER[path] = ""
    return path + _VER[path]


def head(title, desc, canonical, extra=""):
    return """<!doctype html>
<html lang="vi" data-base="">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{domain}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{domain}/assets/img/og-image.jpg">
<meta property="og:url" content="{domain}/{canonical}">
<meta property="og:locale" content="vi_VN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{domain}/assets/img/og-image.jpg">
<meta name="theme-color" content="#0B2A5B">
<link rel="icon" href="{fav_ico}" sizes="any">
<link rel="icon" href="{fav_png}" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{fav_apple}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{css}">
{extra}
</head>
<body>
<a class="skip" href="#main">Bỏ qua và tới nội dung chính</a>
""".format(title=html.escape(title), desc=html.escape(desc), canonical=canonical,
           domain=DOMAIN, site=SITE_NAME, extra=extra, css=v("assets/css/style.css"),
           fav_ico=v("assets/img/favicon.ico"),
           fav_png=v("assets/img/favicon-32.png"),
           fav_apple=v("assets/img/apple-touch-icon.png"))


def topbar():
    return """<div class="topbar">
  <div class="wrap topbar__in">
    <a class="topbar__hot" href="tel:{tel}">{ic}<span>Hotline CSKH: {hot}</span></a>
  </div>
</div>
""".format(tel=HOTLINE_TEL, hot=HOTLINE_TEXT, ic=IC["phone"])


def header(active):
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if href == active else ""
        items += '<li><a href="{h}"{c}>{l}</a></li>'.format(h=href, c=cur, l=label)
    return """<header class="hdr">
  <div class="wrap hdr__in">
    <a class="logo" href="index.html" aria-label="BWT Barrier — trang chủ">{logo}</a>

    <div class="search">
      <form class="search__form" role="search" action="tim-kiem.html" method="get">
        <label class="visually-hidden" for="q">Tìm sản phẩm BWT Barrier</label>
        <input class="search__input" id="q" name="q" type="search" placeholder="Tìm sản phẩm: BWT Barrier M, có bộ đếm, nước cứng…"
               autocomplete="off" aria-controls="search-results">
        <button class="search__btn" type="submit" aria-label="Tìm kiếm">{ic}</button>
      </form>
      <div class="search__results" id="search-results" role="listbox" hidden></div>
    </div>

    <button class="burger" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Mở menu">
      <span></span>
    </button>

    <nav class="nav" id="site-nav" aria-label="Điều hướng chính">
      <div class="nav__head">
        <span class="nav__title">Menu</span>
        <button class="nav__close" type="button" aria-label="Đóng menu">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>
        </button>
      </div>
      <ul class="nav__list">{items}</ul>
    </nav>
  </div>
</header>
""".format(logo=logo_img(), ic=IC["search"], items=items)


def crumb(trail):
    """Breadcrumb hien thi + schema BreadcrumbList cho Google."""
    lis = '<li><a href="index.html">Trang chủ</a></li>'
    for i, (href, label) in enumerate(trail):
        last = i == len(trail) - 1
        if last:
            lis += '<li><span aria-current="page">{l}</span></li>'.format(l=html.escape(label))
        else:
            lis += '<li><a href="{h}">{l}</a></li>'.format(h=href, l=html.escape(label))
    return '<nav class="crumb" aria-label="Đường dẫn"><ol>{lis}</ol></nav>'.format(lis=lis)


# ============================================================
# SCHEMA.ORG — mot @graph cho moi trang, cac thuc the tro nhau qua @id
# ============================================================
ORG_ID = DOMAIN + "/#organization"
SITE_ID = DOMAIN + "/#website"
LOGO_ID = DOMAIN + "/#logo"


def abs_url(path):
    return DOMAIN + "/" + path.lstrip("/")


def ld(*objs):
    """Goi cac thuc the vao mot khoi JSON-LD @graph."""
    graph = [o for o in objs if o]
    doc = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">\n'
            + json.dumps(doc, ensure_ascii=False, indent=2) + "\n</script>")


def ld_org():
    return {
        "@type": "Organization",
        "@id": ORG_ID,
        "name": SITE_NAME,
        "alternateName": "BWT Barrier",
        "url": DOMAIN + "/",
        "description": "Trung tâm bảo hành và chăm sóc khách hàng cho máy lọc nước "
                       "BWT Barrier tại Việt Nam.",
        "logo": {
            "@type": "ImageObject", "@id": LOGO_ID,
            "url": abs_url("assets/img/barrier-logo.webp"),
            "width": 1200, "height": 225, "caption": "BWT Barrier",
        },
        "image": {"@id": LOGO_ID},
        "telephone": HOTLINE_TEL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "90 Đinh Thị Thi",
            "addressLocality": "Phường Hiệp Bình",
            "addressRegion": "Thành phố Hồ Chí Minh",
            "addressCountry": "VN",
        },
        "areaServed": {"@type": "Country", "name": "Việt Nam"},
        "contactPoint": [{
            "@type": "ContactPoint",
            "telephone": HOTLINE_TEL,
            "contactType": "customer service",
            "areaServed": "VN",
            "availableLanguage": ["vi"],
        }],
        "brand": {"@type": "Brand", "name": "BWT Barrier"},
    }


def ld_website():
    return {
        "@type": "WebSite",
        "@id": SITE_ID,
        "url": DOMAIN + "/",
        "name": SITE_NAME,
        "inLanguage": "vi-VN",
        "publisher": {"@id": ORG_ID},
        "potentialAction": {
            "@type": "SearchAction",
            "target": {"@type": "EntryPoint",
                       "urlTemplate": DOMAIN + "/tim-kiem.html?q={search_term_string}"},
            "query-input": "required name=search_term_string",
        },
    }


def ld_faq(items):
    return {
        "@type": "FAQPage",
        "@id": abs_url("index.html") + "#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a,
                },
            }
            for q, a in items
        ],
    }


def ld_page(url, name, desc, image=None, ptype="WebPage", has_crumb=True, main=None):
    d = {
        "@type": ptype,
        "@id": abs_url(url) + "#webpage",
        "url": abs_url(url),
        "name": name,
        "description": desc,
        "inLanguage": "vi-VN",
        "isPartOf": {"@id": SITE_ID},
        "about": {"@id": ORG_ID},
    }
    if image:
        d["primaryImageOfPage"] = {"@type": "ImageObject", "url": abs_url(image)}
    if has_crumb:
        d["breadcrumb"] = {"@id": abs_url(url) + "#breadcrumb"}
    if main:
        d["mainEntity"] = {"@id": main}
    return d


def ld_crumb(url, trail):
    items = [("Trang chủ", "index.html")] + [(lb, hf) for hf, lb in trail]
    return {
        "@type": "BreadcrumbList",
        "@id": abs_url(url) + "#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": nm, "item": abs_url(hf)}
            for i, (nm, hf) in enumerate(items)
        ],
    }


def _spec(p, key):
    for k, v in p["specs"]:
        if k == key:
            return v
    return None


def ld_product(p):
    url = abs_url(p["slug"] + ".html")
    d = {
        "@type": "Product",
        "@id": url + "#product",
        "name": p["name"],
        "description": p["short"],
        "url": url,
        "image": [abs_url(src) for src, _ in p["images"]],
        "brand": {"@type": "Brand", "name": "BWT Barrier"},
        "category": "Máy lọc nước" if p["cat"] in ("may-loc", "co-bo-dem") else "Bộ tiền xử lý nước",
        "additionalProperty": [
            {"@type": "PropertyValue", "name": k, "value": v} for k, v in p["specs"]
        ],
    }

    # kich thuoc "240 x 150 x 330 mm" -> depth x width x height
    kt = _spec(p, "Kích thước (D x R x C)")
    if kt:
        try:
            nums = [int(x) for x in kt.replace("mm", "").split("x")]
            for key, val in zip(("depth", "width", "height"), nums):
                d[key] = {"@type": "QuantitativeValue", "value": val, "unitCode": "MMT"}
        except Exception:
            pass

    tl = _spec(p, "Trọng lượng")
    if tl:
        try:
            d["weight"] = {"@type": "QuantitativeValue",
                           "value": float(tl.split("kg")[0].strip().replace(",", ".")),
                           "unitCode": "KGM"}
        except Exception:
            pass

    # Gia dang de "Lien he" nen khong khai bao Offer — Google yeu cau co price.
    # Khi co bang gia chinh thuc, dien "price" vao PRODUCTS roi bat lai khoi Offer.

    if p.get("sibling"):
        sl = p["sibling"][0]
        sib = PRODUCT_BY_SLUG.get(sl)
        if sib:
            d["isSimilarTo"] = {"@type": "Product", "name": sib["name"],
                                "url": abs_url(sl + ".html")}
    return d


def ld_itemlist():
    return {
        "@type": "ItemList",
        "@id": abs_url("san-pham.html") + "#itemlist",
        "name": "Sản phẩm BWT Barrier",
        "numberOfItems": len(PRODUCTS),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": x["name"],
             "url": abs_url(x["slug"] + ".html")}
            for i, x in enumerate(PRODUCTS)
        ],
    }


def ld_store():
    return {
        "@type": "LocalBusiness",
        "@id": abs_url("lien-he.html") + "#business",
        "name": SITE_NAME,
        "url": abs_url("lien-he.html"),
        "image": abs_url("assets/img/og-image.jpg"),
        "telephone": HOTLINE_TEL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "90 Đinh Thị Thi",
            "addressLocality": "Phường Hiệp Bình",
            "addressRegion": "Thành phố Hồ Chí Minh",
            "addressCountry": "VN",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 10.845839, "longitude": 106.712965},
        "hasMap": MAP_LINK,
        "areaServed": {"@type": "Country", "name": "Việt Nam"},
        "parentOrganization": {"@id": ORG_ID},
    }


def dock():
    return """<div class="dock">
  <a class="dock__btn dock__btn--call" href="tel:{tel}" aria-label="Gọi hotline {hot}">
    {phone}<span class="dock__label">Gọi ngay: {hot}</span>
  </a>
  <button class="dock__btn dock__btn--top" type="button" aria-label="Lên đầu trang">{up}</button>
</div>

<nav class="mbar" aria-label="Liên hệ nhanh">
  <a class="is-call" href="tel:{tel}">{phone}<span>CSKH: {hot}</span></a>
  <a href="lien-he.html">{mail}<span>Liên hệ</span></a>
</nav>
""".format(tel=HOTLINE_TEL, hot=HOTLINE_TEXT, phone=IC["phone"], up=IC["up"], mail=IC["mail"])


def footer():
    return """<footer class="ftr">
  <div class="wrap">
    <div class="ftr__grid">
      <div>
        <a class="logo logo--ftr" href="index.html">{logo}</a>
        <p class="ftr__about">
          Trung tâm bảo hành và chăm sóc khách hàng cho máy lọc nước BWT Barrier:
          tiếp nhận bảo hành, thay lõi chính hãng và hỗ trợ kỹ thuật trên toàn quốc.
        </p>
      </div>
      <div>
        <p class="ftr__h">Thông tin</p>
        <ul>
          <li><a href="ve-chung-toi.html">Về chúng tôi</a></li>
          <li><a href="san-pham.html">Danh mục sản phẩm</a></li>
          <li><a href="lien-he.html">Liên hệ</a></li>
          <li><a href="lien-he.html#bao-hanh">Chính sách bảo hành</a></li>
        </ul>
      </div>
      <div>
        <p class="ftr__h">Hotline CSKH</p>
        <ul>
          <li>Hotline CSKH: <a href="tel:{tel}"><strong>{hot}</strong></a></li>
          <li>{addr}</li>
        </ul>
      </div>
    </div>
  </div>
</footer>
""".format(logo=logo_img(True), tel=HOTLINE_TEL, hot=HOTLINE_TEXT,
           addr=html.escape(ADDRESS))


def tail(extra=""):
    return """{extra}
<script src="{idx}"></script>
<script src="{js}"></script>
<script src="https://app.2pm.space/widget.js" data-id="7070b23c-82cc-4860-9bf0-847e88250197"></script>
</body>
</html>
""".format(extra=extra, idx=v("assets/js/search-index.js"), js=v("assets/js/main.js"))


# ============================================================
# THÀNH PHẦN DÙNG LẠI
# ============================================================
def product_card(p):
    metas = "".join("<li>{}</li>".format(html.escape(m)) for m in p["usps"][:3])
    return """<article class="pcard" data-cat="{cat}">
  <div class="pcard__media">
    <span class="pcard__tag">{catlabel}</span>
    <img src="{img}" alt="{alt}" loading="lazy"{dim}>
  </div>
  <div class="pcard__body">
    <h3 class="pcard__title"><a href="{slug}.html">{name}</a></h3>
    <ul class="pcard__meta">{metas}</ul>
    <div class="pcard__foot">
      <span class="price">{price}<small>{note}</small></span>
      <a class="btn btn--primary btn--sm" href="{slug}.html">Chi tiết</a>
    </div>
  </div>
</article>""".format(
        cat=p["cat"], catlabel=html.escape(p["cat_label"]),
        img=p["images"][0][0], alt=html.escape(p["images"][0][1]), dim=dims(p["images"][0][0]),
        slug=p["slug"], name=html.escape(p["name"]), metas=metas,
        price=p["price"], note=html.escape(p["price_note"]))


def feature(icon, title, text):
    return """<div class="fcard">
  <div class="fcard__ic">{ic}</div>
  <h3>{t}</h3>
  <p>{p}</p>
</div>""".format(ic=IC[icon], t=html.escape(title), p=html.escape(text))


def cta_band():
    return """<section class="sec">
  <div class="wrap">
    <div class="cta">
      <div>
        <h2>Trung tâm bảo hành BWT Barrier</h2>
        <p>Tiếp nhận đăng ký bảo hành, cung cấp cụm lõi thay thế định kỳ và tư vấn xử lý kỹ thuật cho dòng máy lọc nước BWT Barrier.</p>
      </div>
      <div class="cta__act">
        <a class="btn btn--light" href="lien-he.html">Xem thông tin liên hệ</a>
      </div>
    </div>
  </div>
</section>"""


# Dữ liệu Câu hỏi thường gặp (FAQ) — 100% từ thông tin hiện có trên website
FAQS_INDEX = [
    (
        "Bao lâu thì gia đình nên thay lõi lọc BWT Barrier một lần?",
        "Chu kỳ thay lõi định kỳ khuyến nghị là 12 tháng hoặc theo định mức 8.000 lít (BWT Barrier M) và 10.000 lít (BWT Barrier L). Với các model có bộ đếm Water Meter, thiết bị sẽ hiển thị phần trăm tuổi thọ lõi còn lại theo lượng nước đã dùng thực tế.",
    ),
    (
        "Máy lọc nước BWT Barrier có dùng điện và xả nước thải không?",
        "BWT Barrier chạy bằng chính áp lực nước trong đường ống nên không cần điện và không xả nước thải, giúp tiết kiệm điện nước và bảo vệ môi trường.",
    ),
    (
        "Nước sau lọc qua máy BWT Barrier có uống trực tiếp được không?",
        "Nước sau lọc uống trực tiếp tại vòi. Hệ thống loại bỏ clo, gỉ sét, kim loại nặng, vi khuẩn nhưng giữ lại và bổ sung khoáng chất canxi, magie, kẽm có lợi cho cơ thể thay vì lọc sạch trơ.",
    ),
    (
        "Chính sách bảo hành và đổi trả của BWT Barrier quy định như thế nào?",
        "Thân máy được bảo hành chính hãng 36 tháng, đổi trả theo quy định trong 7 ngày nếu lỗi từ nhà sản xuất. Đội ngũ kỹ thuật hướng dẫn lắp đặt, thay lõi tại nhà và theo dõi lịch thay lõi định kỳ 12 tháng.",
    ),
    (
        "Nguồn nước có cặn trắng canxi (nước cứng) thì chọn model nào?",
        "Đối với nguồn nước giếng khoan hoặc nước máy có độ cứng cao hay đóng cặn canxi ở ấm đun, model BWT Barrier H được trang bị lõi Softening chuyên làm mềm nước cứng, hạn chế cáu cặn canxi và giữ lại khoáng chất có lợi.",
    ),
]


# ============================================================
# TRANG CHỦ
# ============================================================
def page_index():
    org_ld = ld(
        ld_org(), ld_website(),
        ld_page("index.html", "Trung tâm bảo hành BWT Barrier",
                "Tiếp nhận bảo hành chính hãng, cung cấp cụm lõi định kỳ và kiểm tra kỹ thuật máy lọc nước "
                "BWT Barrier.",
                image="assets/img/og-image.jpg", ptype="WebPage", has_crumb=False,
                main=abs_url("san-pham.html") + "#itemlist"),
        ld_faq(FAQS_INDEX),
    )

    feats = "".join([
        feature("drop", "Giữ khoáng, không lọc trơ",
                "Công nghệ Ion-Exchange ByPass+ chỉ loại bỏ chất có hại và giữ lại Ca, Mg, Zn ở hàm lượng có lợi."),
        feature("box", "Lõi đúc nguyên khối",
                "Thiết kế độc quyền bao kín cụm lõi thành một khối liền, chống nhiễm khuẩn ngược và rò rỉ."),
        feature("filter", "8 công nghệ lọc",
                "Hạt trao đổi ion, sợi trao đổi ion, nano tăng cường, than hoạt tính, màng sợi rỗng và cân bằng khoáng."),
        feature("award", "An toàn vật liệu BPA Free",
                "Toàn bộ chi tiết tiếp xúc với dòng nước đều sử dụng nhựa nguyên sinh cao cấp, đáp ứng tiêu chuẩn an toàn thực phẩm."),
        feature("clock", "Tuổi thọ lõi 12 tháng",
                "Lõi 8.000 – 10.000 lít, bộ đếm Water Meter báo chính xác thời điểm cần thay."),
        feature("bolt", "Vận hành không dùng điện",
                "Hệ thống hoạt động dựa trên áp lực nước tự nhiên trong đường ống, không tốn điện, không gây tiếng ồn và không xả nước thải."),
        feature("tool", "Lắp âm tủ gọn gàng",
                "Kích thước 240 x 150 x 330 mm, lắp dưới chậu rửa hoặc trong tủ bếp, không chiếm mặt bàn."),
        feature("sparkles", "Công nghệ One Touch",
                "Thiết kế tháo lắp thông minh giúp việc thay thế cụm lõi tại nhà trở nên đơn giản chỉ với một thao tác xoay."),
    ])

    faq_html = "".join(
        """<div class="faq-item" data-open="{is_open}">
  <button class="faq-btn" type="button" aria-expanded="{is_exp}">
    <span>{q}</span>
    {chevron}
  </button>
  <div class="faq-panel">
    <p>{a}</p>
  </div>
</div>""".format(
            is_open="true" if i == 0 else "false",
            is_exp="true" if i == 0 else "false",
            q=html.escape(q),
            a=html.escape(a),
            chevron=IC["chevron"],
        )
        for i, (q, a) in enumerate(FAQS_INDEX)
    )

    return (
        head("Trung tâm bảo hành BWT Barrier Art AI Series",
             "Trung tâm bảo hành BWT Barrier: tiếp nhận bảo hành chính hãng, cung cấp cụm lõi và kiểm tra "
             "kỹ thuật cho máy lọc nước BWT Barrier và Art AI Series.",
             "index.html", org_ld)
        + topbar() + header("index.html")
        + """
<main id="main">

<section class="hero">
  <div class="wrap hero__in">
    <div>
      <h1>Trung tâm bảo hành<br><em>BWT Barrier</em></h1>
      <p class="hero__lead">
        Tiếp nhận bảo hành chính hãng, cung cấp cụm lõi định kỳ và kiểm tra kỹ thuật máy lọc nước BWT Barrier trên phạm vi toàn quốc.
      </p>

      <div class="hero__stats">
        <div class="hero__stat"><b>12 tháng</b><span>chu kỳ thay lõi</span></div>
        <div class="hero__stat"><b>Toàn quốc</b><span>mạng lưới phục vụ</span></div>
      </div>
    </div>
    <div class="hero__media hero__media--photo">
      <img class="hero__photo" src="assets/img/bwt-barrier-service.jpg" width="1500" height="1001"
           alt="Kỹ thuật viên trung tâm bảo hành BWT Barrier kiểm tra máy lọc nước tại nhà khách hàng"
           fetchpriority="high">
    </div>
  </div>
</section>

<!-- 1. Dịch vụ khách hàng trọng tâm (Bento Showcase Layout) -->
<section class="sec" id="dich-vu">
  <div class="wrap">
    <div class="sec__head">
      <span class="eyebrow">Dịch vụ khách hàng</span>
      <h2>Dịch vụ bảo hành &amp; kỹ thuật chính hãng</h2>
      <p>Chính sách bảo hành chính hãng và các dịch vụ kỹ thuật định kỳ dành cho gia đình sử dụng máy lọc nước BWT Barrier.</p>
    </div>

    <div class="svc-bento">
      <!-- Cột trái: Thẻ dịch vụ bảo hành chính hãng nổi bật -->
      <div class="svc-bento__lead">
        <div class="svc-bento__badge">{ic_shield} Bảo hành chính hãng 36 tháng</div>
        <h3>Trung tâm tiếp nhận bảo hành chính hãng</h3>
        <p class="svc-bento__desc">
          Thân máy lọc nước BWT Barrier được bảo hành chính hãng 36 tháng trên toàn quốc.
          Chính sách đổi trả theo quy định trong 7 ngày nếu có lỗi từ nhà sản xuất.
        </p>
        <ul class="checklist svc-bento__checklist">
          <li>{chk}<span>Bảo hành chính hãng 36 tháng cho thân máy</span></li>
          <li>{chk}<span>Đổi trả theo quy định trong 7 ngày nếu lỗi từ nhà sản xuất</span></li>
          <li>{chk}<span>Tiếp nhận và xử lý kỹ thuật tận nơi trên toàn quốc</span></li>
        </ul>
      </div>

      <!-- Cột phải: 3 dịch vụ dạng danh sách xếp lớp thanh lịch (thuần thông tin) -->
      <div class="svc-bento__stack">
        <div class="svc-item">
          <div class="svc-item__ic">{ic_award}</div>
          <div class="svc-item__body">
            <div class="svc-item__meta">
              <h4>Thay lõi lọc chính hãng</h4>
              <span class="svc-item__tag">Chính hãng</span>
            </div>
            <p>Cung cấp cụm lõi thay thế chính hãng BWT Barrier M, L, H. Công nghệ One Touch tự thay lõi chỉ một thao tác xoay hoặc có kỹ thuật viên thay giúp tại nhà.</p>
          </div>
        </div>

        <div class="svc-item">
          <div class="svc-item__ic">{ic_tool}</div>
          <div class="svc-item__body">
            <div class="svc-item__meta">
              <h4>Kiểm tra &amp; Xử lý kỹ thuật</h4>
              <span class="svc-item__tag">Toàn quốc</span>
            </div>
            <p>Kỹ thuật viên kiểm tra áp lực nước, vận hành thiết bị và xử lý sự cố trực tiếp tại nhà khách hàng trên phạm vi toàn quốc.</p>
          </div>
        </div>

        <div class="svc-item">
          <div class="svc-item__ic">{ic_clock}</div>
          <div class="svc-item__body">
            <div class="svc-item__meta">
              <h4>Lắp đặt &amp; Theo dõi chu kỳ</h4>
              <span class="svc-item__tag">Chu kỳ 12 tháng</span>
            </div>
            <p>Lắp đặt máy âm dưới chậu rửa hoặc trong tủ bếp (240 x 150 x 330 mm), kết hợp theo dõi nhắc lịch thay lõi định kỳ 12 tháng hoặc qua bộ đếm Water Meter.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 2. Quy trình tiếp nhận dịch vụ 4 bước (Connected Flowline Timeline) -->
<section class="sec sec--tint" id="quy-trinh">
  <div class="wrap">
    <div class="sec__head">
      <span class="eyebrow">Quy trình phục vụ</span>
      <h2>Quy trình tiếp nhận &amp; xử lý dịch vụ</h2>
      <p>Các bước từ tiếp nhận yêu cầu đến khi hoàn tất kiểm tra vận hành và bàn giao thiết bị.</p>
    </div>

    <div class="flow-track">
      <div class="flow-step">
        <div class="flow-step__marker">01</div>
        <div class="flow-step__card">
          <div class="flow-step__ic">{ic_clipboard}</div>
          <h4>Tiếp nhận yêu cầu</h4>
          <p>Ghi nhận thông tin bảo hành, kiểm tra kỹ thuật hoặc nhu cầu thay lõi lọc.</p>
        </div>
      </div>

      <div class="flow-step">
        <div class="flow-step__marker">02</div>
        <div class="flow-step__card">
          <div class="flow-step__ic">{ic_cal}</div>
          <h4>Tư vấn &amp; Hẹn lịch</h4>
          <p>Kỹ thuật viên đối soát thông tin nguồn nước và xác nhận lịch hẹn kiểm tra phù hợp.</p>
        </div>
      </div>

      <div class="flow-step">
        <div class="flow-step__marker">03</div>
        <div class="flow-step__card">
          <div class="flow-step__ic">{ic_tool}</div>
          <h4>Kiểm tra tại nhà</h4>
          <p>Kỹ thuật viên kiểm tra vận hành máy, lắp đặt hoặc thay cụm lõi chính hãng.</p>
        </div>
      </div>

      <div class="flow-step">
        <div class="flow-step__marker">04</div>
        <div class="flow-step__card">
          <div class="flow-step__ic">{ic_sparkles}</div>
          <h4>Bàn giao &amp; Nhắc lịch</h4>
          <p>Bàn giao thiết bị vận hành ổn định và cập nhật thông tin chu kỳ thay lõi định kỳ 12 tháng.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 3. Cầu nối Dòng sản phẩm BWT Barrier -->
<section class="sec">
  <div class="wrap">
    <div class="split">
      <div class="split__media">
        <img src="assets/img/bwt-giau-duong-chat.webp" width="1200" height="800" loading="lazy"
             alt="Sơ đồ công nghệ lọc BWT Barrier: loại bỏ tạp chất, giữ lại khoáng chất có lợi">
      </div>
      <div class="split__body">
        <span class="eyebrow">Dòng sản phẩm BWT Barrier</span>
        <h2>Công nghệ lọc nước giàu dưỡng chất BWT Barrier</h2>
        <p>
          BWT Barrier là dòng máy lọc nước lắp âm tủ cao cấp, vận hành bằng chính áp lực nước trong
          đường ống — không cắm điện, không xả nước thải và bổ sung vi khoáng Magie, Kẽm có lợi cho tim mạch.
        </p>
        <ul class="checklist">
          <li>{chk}<span>Lõi đúc nguyên khối độc quyền — chống nhiễm khuẩn ngược và rỉ nước</span></li>
          <li>{chk}<span>Loại bỏ clo, kim loại nặng, vi khuẩn nhưng không làm nước mất khoáng trơ</span></li>
          <li>{chk}<span>Công nghệ One Touch: tự thay cụm lõi tại nhà dễ dàng chỉ với một thao tác xoay</span></li>
        </ul>
        <p style="margin-top:26px">
          <a class="btn btn--primary" href="san-pham.html">Khám phá các dòng máy BWT Barrier &rarr;</a>
        </p>
      </div>
    </div>
  </div>
</section>

<!-- 4. Vì sao chọn BWT Barrier -->
<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec__head">
      <span class="eyebrow">Vì sao chọn BWT Barrier</span>
      <h2>Sạch nhưng không mất đi khoáng chất</h2>
      <p>Điểm khác biệt của BWT Barrier nằm ở triết lý lọc: không khử sạch trơ,
         mà đưa nguồn nước về đúng thành phần khoáng có lợi cho cơ thể.</p>
    </div>
    <div class="fgrid">{feats}</div>
  </div>
</section>

<!-- 5. Câu hỏi thường gặp (Split 2 Cột: Sidebar thuần nội dung + Accordion List) -->
<section class="sec" id="hoi-dap">
  <div class="wrap">
    <div class="faq-layout">
      <!-- Cột trái: Sidebar thuần thông tin -->
      <div class="faq-sidebar">
        <span class="eyebrow">Giải đáp thắc mắc</span>
        <h2>Câu hỏi thường gặp</h2>
        <p>Những giải đáp chi tiết về dịch vụ bảo hành, thay lõi và đặc tính kỹ thuật máy lọc nước BWT Barrier.</p>
      </div>

      <!-- Cột phải: Accordion list -->
      <div class="faq-accordion-list">
        {faq}
      </div>
    </div>
  </div>
</section>

{cta}

</main>
""".format(tel=HOTLINE_TEL, hot=HOTLINE_TEXT, ic_phone=IC["phone"],
           ic_award=IC["award"], ic_shield=IC["shield"], ic_tool=IC["tool"],
           ic_clock=IC["clock"], ic_clipboard=IC["clipboard"], ic_cal=IC["cal"],
           ic_sparkles=IC["sparkles"], chk=IC["check"], feats=feats,
           faq=faq_html, cta=cta_band())
        + footer() + tail()
    )


# ============================================================
# TRANG DANH MỤC
# ============================================================
def page_products():
    cards = "".join(product_card(p) for p in PRODUCTS)
    return (
        head("Sản phẩm BWT Barrier — Máy lọc nước & bộ tiền xử lý",
             "Máy lọc nước BWT Barrier M, L, H (bản thường và bản kèm bộ đếm Water Meter) "
             "cùng bộ tiền xử lý ion M, ion H — thông số kỹ thuật và tư vấn chọn model.",
             "san-pham.html",
             ld(ld_org(), ld_website(),
                ld_page("san-pham.html", "Sản phẩm BWT Barrier",
                        "Danh mục máy lọc nước và bộ tiền xử lý nước BWT Barrier.",
                        ptype="CollectionPage",
                        main=abs_url("san-pham.html") + "#itemlist"),
                ld_crumb("san-pham.html", [("san-pham.html", "Sản phẩm")]),
                ld_itemlist()))
        + topbar() + header("san-pham.html")
        + crumb([("san-pham.html", "Sản phẩm")])
        + """
<main id="main">
<section class="phead">
  <div class="wrap">
    <h1>Sản phẩm BWT Barrier</h1>
    <p>Các sản phẩm BWT Barrier đang phân phối tại Việt Nam. Chọn nhóm bên dưới để lọc nhanh
       giữa máy lọc nước uống trực tiếp, bản kèm bộ đếm Water Meter và bộ tiền xử lý cho máy điện giải.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="tabs" role="tablist" aria-label="Lọc theo nhóm sản phẩm">
      <button class="tab" type="button" role="tab" data-filter="all" aria-selected="true">Tất cả ({n_all})</button>
      <button class="tab" type="button" role="tab" data-filter="may-loc" aria-selected="false">Máy lọc nước ({n_ml})</button>
      <button class="tab" type="button" role="tab" data-filter="co-bo-dem" aria-selected="false">Có bộ đếm ({n_bd})</button>
      <button class="tab" type="button" role="tab" data-filter="tien-xu-ly" aria-selected="false">Bộ tiền xử lý ({n_tx})</button>
    </div>
    <h2 class="visually-hidden">Danh sách sản phẩm BWT Barrier</h2>
    <div class="pgrid">{cards}</div>
  </div>
</section>

{cta}
</main>
""".format(cards=cards, cta=cta_band(),
           n_all=len(PRODUCTS),
           n_ml=sum(1 for x in PRODUCTS if x["cat"] == "may-loc"),
           n_bd=sum(1 for x in PRODUCTS if x["cat"] == "co-bo-dem"),
           n_tx=sum(1 for x in PRODUCTS if x["cat"] == "tien-xu-ly"))
        + footer() + tail()
    )


# ============================================================
# TRANG CHI TIẾT SẢN PHẨM
# ============================================================
def meta_desc(p):
    """Mo ta ~110-165 ky tu cho the description."""
    d = p["short"]
    for extra in (" Hàng chính hãng, bảo hành 36 tháng. Gọi %s để được tư vấn." % HOTLINE_TEXT,
                  " Hàng chính hãng, bảo hành 36 tháng. Hotline %s." % HOTLINE_TEXT,
                  " Hàng chính hãng, bảo hành chính hãng 36 tháng."):
        if len(d) + len(extra) <= 165:
            return d + extra
    return d


def page_product(p):
    thumbs = ""
    for i, (src, alt) in enumerate(p["images"] if len(p["images"]) > 1 else []):
        thumbs += ('<button class="pd__thumb" type="button" data-src="{s}" data-alt="{a}" '
                   'aria-selected="{sel}" aria-label="Xem ảnh {n}">'
                   '<img src="{s}" alt="" loading="lazy"{d}></button>').format(
            s=src, a=html.escape(alt), sel="true" if i == 0 else "false", n=i + 1, d=dims(src))
    if thumbs:
        thumbs = '<div class="pd__thumbs">' + thumbs + "</div>"

    usps = "".join("<li>{ic}<span>{t}</span></li>".format(ic=IC["check"], t=html.escape(u)) for u in p["usps"])
    specs = "".join('<tr><th scope="row">{k}</th><td>{v}</td></tr>'.format(
        k=html.escape(k), v=html.escape(v)) for k, v in p["specs"])
    intro = "".join("<p>{}</p>".format(html.escape(t)) for t in p["intro"])

    variants = ""
    if p.get("sibling"):
        sl, lb = p["sibling"]
        variants = (
            '<a class="pd__variant pd__variant--link" href="{sl}.html">'
            '<b>{lb}</b><span class="pd__variant__go">Xem bản này &rsaquo;</span></a>'
        ).format(sl=sl, lb=html.escape(lb))

    related = "".join(product_card(x) for x in PRODUCTS if x["slug"] != p["slug"])

    slug_url = p["slug"] + ".html"
    ld_block = ld(
        ld_org(), ld_website(),
        ld_page(slug_url, p["name"], meta_desc(p), image=p["images"][0][0],
                ptype="ItemPage", main=abs_url(slug_url) + "#product"),
        ld_crumb(slug_url, [("san-pham.html", "Sản phẩm"), (slug_url, p["name"])]),
        ld_product(p),
    )

    return (
        head(p["name"] + " — Chính hãng", meta_desc(p), slug_url, ld_block)
        + topbar() + header("san-pham.html")
        + crumb([("san-pham.html", "Sản phẩm"), (p["slug"] + ".html", p["name"])])
        + """
<main id="main">
<div class="wrap">
  <div class="pd">
    <div class="pd__gal">
      <div class="pd__main">
        <img id="pd-main-img" src="{img}" alt="{alt}"{dim0} fetchpriority="high">
      </div>
      {thumbs}
    </div>

    <div>
      <p class="pd__brand">{catlabel} · BWT Barrier</p>
      <h1>{name}</h1>
      <p style="color:var(--muted);font-size:1.03rem">{short}</p>

      <div class="pd__price">
        <span class="now">{price}</span>
        <span class="note">{note}</span>
      </div>
      {variants}

      <div class="pd__cta">
        <a class="btn btn--primary" href="tel:{tel}">{ic} Đặt hàng: <span class="nb">{hot}</span></a>
        <a class="btn btn--ghost" href="lien-he.html">Bảo hành &amp; liên hệ</a>
      </div>

      <ul class="pd__usp">{usps}</ul>

      <p style="font-size:.9rem;color:var(--muted);border-left:3px solid var(--cyan);padding-left:14px">
        <strong style="color:var(--navy)">Phù hợp với:</strong> {best}
      </p>
    </div>
  </div>
</div>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="split">
      <div class="split__body prose">
        <span class="eyebrow">Giới thiệu</span>
        <h2>Về {name}</h2>
        {intro}
      </div>
      <div class="split__media">
        <h3>Thông số kỹ thuật</h3>
        <div class="tblwrap">
          <table class="spec"><tbody>{specs}</tbody></table>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec__head">
      <span class="eyebrow">Sản phẩm khác</span>
      <h2>Có thể bạn quan tâm</h2>
    </div>
    <div class="pgrid">{related}</div>
  </div>
</section>

{cta}
</main>
""".format(img=p["images"][0][0], alt=html.escape(p["images"][0][1]),
           dim0=dims(p["images"][0][0]), thumbs=thumbs,
           catlabel=html.escape(p["cat_label"]), name=html.escape(p["name"]),
           short=html.escape(p["short"]), price=p["price"], note=html.escape(p["price_note"]),
           variants=variants, tel=HOTLINE_TEL, hot=HOTLINE_TEXT, ic=IC["phone"],
           slug=p["slug"], usps=usps, best=html.escape(p["best_for"]),
           intro=intro, specs=specs, related=related, cta=cta_band())
        + footer() + tail()
    )


# ============================================================
# TRANG VỀ CHÚNG TÔI
# ============================================================
def page_about():
    return (
        head("Về chúng tôi — BWT Barrier | Nguồn Nước Trong Lành, Giàu Khoáng Chất",
             "BWT Barrier hướng tới chuẩn mực mới về nước uống tại vòi: không chỉ làm sạch tạp chất "
             "mà còn bảo toàn và bổ sung các vi khoáng tự nhiên thiết yếu như Magie và Kẽm, "
             "nâng cao chất lượng sống và thân thiện với môi trường.",
             "ve-chung-toi.html",
             ld(ld_org(), ld_website(),
                ld_page("ve-chung-toi.html", "Về chúng tôi — BWT Barrier",
                        "BWT Barrier – Nguồn Nước Trong Lành, Giàu Khoáng Chất Cho Cả Gia Đình. "
                        "Chuyên nghiên cứu và phát triển các giải pháp lọc nước chất lượng cao.",
                        image="assets/img/cong-nghe-loc-nuoc.webp",
                        ptype="AboutPage", main=ORG_ID),
                ld_crumb("ve-chung-toi.html", [("ve-chung-toi.html", "Về chúng tôi")])))
        + topbar() + header("ve-chung-toi.html")
        + crumb([("ve-chung-toi.html", "Về chúng tôi")])
        + """
<main id="main">
<!-- 1. Hero Banner: Thông điệp chủ đạo -->
<section class="hero">
  <div class="wrap hero__in">
    <div>
      <span class="hero__eyebrow">{ic_drop} BWT Barrier · Chuẩn mực nước uống</span>
      <h1>Nguồn Nước Trong Lành,<br><em>Giàu Khoáng Chất</em></h1>
      <p class="hero__lead">
        Chuẩn mực nước uống tại vòi: lọc sạch tạp chất, bổ sung vi khoáng Magie &amp; Kẽm tự nhiên, nâng cao chất lượng sống cho cả gia đình.
      </p>
      <div class="hero__cta">
        <a class="btn btn--primary" href="san-pham.html">{ic_filter} Khám phá sản phẩm</a>
      </div>
    </div>
    <div class="hero__media">
      <img class="hero__photo" src="assets/img/nha-may-bwrbarrier.webp" width="1540" height="846"
           alt="Nhà máy sản xuất BWT Barrier hiện đại đạt tiêu chuẩn quốc tế" fetchpriority="high">
    </div>
  </div>
</section>

<!-- 2. Câu chuyện thương hiệu (Brand Story) -->
<section class="sec" id="cau-chuyen">
  <div class="wrap">
    <div class="split">
      <div class="split__media">
        <img src="assets/img/cong-nghe-loc-nuoc.webp" width="1540" height="1371" loading="lazy"
             alt="Sơ đồ công nghệ lọc nước phức hợp BWT Barrier">
      </div>
      <div class="split__body prose">
        <span class="eyebrow">Câu chuyện thương hiệu</span>
        <h2>Nguồn nước tương lai</h2>
        <p>
          <strong>Về BWT Barrier:</strong> Chuyên nghiên cứu và phát triển các giải pháp lọc nước dân dụng và thương mại chất lượng cao.
        </p>
        <p>
          <strong>Định hướng phát triển:</strong> BWT Barrier kết hợp công nghệ kỹ thuật tiên tiến cùng kinh nghiệm xử lý các đặc tính nguồn nước phức tạp trên thế giới. Thương hiệu tập trung vào giải pháp nước uống có lợi cho sức khỏe, cân bằng giữa khả năng lọc sạch và việc duy trì dưỡng chất tự nhiên trong nước.
        </p>
        <div class="trust__it" style="background:var(--sky-2);border-radius:14px;padding:16px 20px;margin-top:20px;border:1px solid var(--line)">
          {ic_award}
          <div>
            <b style="font-size:1rem;color:var(--navy)">Công nghệ vì sức khỏe gia đình</b>
            <span style="font-size:.9rem;color:var(--muted)">Đột phá với khả năng bổ sung dưỡng chất tự nhiên và bảo vệ môi trường sống xanh.</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 3. Tầm nhìn & Sứ mệnh (Vision & Mission) -->
<section class="sec sec--tint" id="tam-nhin-su-menh">
  <div class="wrap">
    <div class="sec__head">
      <span class="eyebrow">Mục tiêu &amp; Tôn chỉ hành động</span>
      <h2>Tầm nhìn &amp; Sứ mệnh</h2>
      <p>Kiến tạo thói quen sống khỏe, sử dụng nguồn nước uống chất lượng cao và đồng hành cùng lối sống xanh</p>
    </div>
    <div class="fgrid fgrid--2">
      <div class="fcard" style="border-top:4px solid var(--blue)">
        <div class="fcard__ic">{ic_globe}</div>
        <h3 style="font-size:1.22rem;color:var(--navy);margin-bottom:12px">Tầm nhìn chiến lược</h3>
        <p style="font-size:1rem;line-height:1.65;color:var(--ink)">
          Định hình thói quen sử dụng nguồn nước uống có lợi cho sức khỏe tại các hộ gia đình, thúc đẩy lối sống xanh và giảm phát thải nhựa ra môi trường.
        </p>
      </div>
      <div class="fcard" style="border-top:4px solid var(--cyan)">
        <div class="fcard__ic">{ic_leaf}</div>
        <h3 style="font-size:1.22rem;color:var(--navy);margin-bottom:12px">Sứ mệnh phụng sự</h3>
        <ul class="checklist" style="margin:0">
          <li>
            {ic_check}
            <span>Cung cấp nguồn nước uống an toàn, giàu khoáng chất ngay tại vòi cho người dùng.</span>
          </li>
          <li>
            {ic_check}
            <span>Ứng dụng các công nghệ lọc không dùng điện năng và hạn chế tối đa việc xả thải nước thừa, góp phần tiết kiệm tài nguyên thiên nhiên.</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- 4. Trụ cột giá trị & Điểm nổi bật (Key Pillars) -->
<section class="sec" id="tru-cot-gia-tri">
  <div class="wrap">
    <div class="sec__head">
      <span class="eyebrow">Giá trị vượt trội</span>
      <h2>Trụ cột giá trị &amp; Điểm nổi bật</h2>
      <p>Bốn thế mạnh công nghệ tạo nên sự khác biệt cho các giải pháp lọc nước BWT Barrier</p>
    </div>
    <div class="fgrid">
      <div class="fcard">
        <div class="fcard__ic">{ic_drop}</div>
        <h3>Bổ sung vi khoáng Magie &amp; Kẽm</h3>
        <p>Làm giàu vi khoáng tự nhiên giúp tăng đề kháng, hỗ trợ tuần hoàn và mang lại vị nước thanh mát tự nhiên.</p>
      </div>
      <div class="fcard">
        <div class="fcard__ic">{ic_leaf}</div>
        <h3>Lọc thân thiện môi trường</h3>
        <p>Vận hành bằng áp lực nước tự nhiên: không cắm điện, không nước thải, tối ưu chi phí và tài nguyên nước.</p>
      </div>
      <div class="fcard">
        <div class="fcard__ic">{ic_box}</div>
        <h3>Lõi đúc nguyên khối SmartLock</h3>
        <p>Lõi đúc kín chống tái nhiễm khuẩn và rò rỉ, cơ chế One-Touch giúp tự thay lõi tại nhà dễ dàng.</p>
      </div>
      <div class="fcard">
        <div class="fcard__ic">{ic_shield}</div>
        <h3>Tương thích máy ion kiềm</h3>
        <p>Bảo toàn khoáng chất dẫn điện (Canxi, Magie), bảo vệ tấm điện cực máy điện giải hoạt động bền bỉ.</p>
      </div>
    </div>
  </div>
</section>

<!-- 5. Cam kết với khách hàng (Our Commitments) -->
<section class="sec" id="cam-ket">
  <div class="wrap">
    <div class="split split--rev">
      <div class="split__media">
        <img src="assets/img/bwt-barrier-m-box.webp" width="900" height="900" loading="lazy"
             alt="Hộp máy lọc nước BWT Barrier — Cam kết an toàn vật liệu và đồng hành dài hạn">
      </div>
      <div class="split__body prose">
        <span class="eyebrow">Trách nhiệm &amp; Phụng sự</span>
        <h2>Cam kết với khách hàng</h2>
        <p>
          BWT Barrier cam kết bảo vệ sức khỏe gia đình bạn bằng dịch vụ chăm sóc trọn vòng đời sản phẩm:
        </p>
        <div style="display:flex;flex-direction:column;gap:20px;margin:24px 0">
          <div style="display:flex;gap:16px;align-items:flex-start">
            <div class="fcard__ic" style="flex:none;margin:0">{ic_clock}</div>
            <div>
              <h3 style="margin:0 0 6px;font-size:1.1rem;color:var(--navy)">Đồng hành dài hạn</h3>
              <p style="margin:0;font-size:.95rem;color:var(--muted)">Cung cấp dịch vụ chăm sóc khách hàng chu đáo, giải pháp theo dõi và nhắc lịch thay thế lõi lọc định kỳ nhằm duy trì chất lượng nước ổn định trong suốt quá trình sử dụng.</p>
            </div>
          </div>
        </div>
        <div style="margin-top:28px">
          <a class="btn btn--primary" href="lien-he.html">{ic_phone} Trung tâm hỗ trợ &amp; CSKH</a>
        </div>
      </div>
    </div>
  </div>
</section>

{cta}
</main>
""".format(
            ic_drop=IC["drop"],
            ic_filter=IC["filter"],
            ic_phone=IC["phone"],
            ic_award=IC["award"],
            ic_globe=IC["globe"],
            ic_leaf=IC["leaf"],
            ic_check=IC["check"],
            ic_box=IC["box"],
            ic_shield=IC["shield"],
            ic_tool=IC["tool"],
            ic_clock=IC["clock"],
            tel=HOTLINE_TEL,
            hot=HOTLINE_TEXT,
            cta=cta_band()
        )
        + footer() + tail()
    )


# ============================================================
# TRANG LIÊN HỆ
# ============================================================
def page_contact():
    return (
        head("Liên hệ BWT Barrier Việt Nam — Tư vấn, lắp đặt, bảo hành",
             "Hotline " + HOTLINE_TEXT + " — tư vấn chọn máy lọc nước BWT Barrier phù hợp "
             "với nguồn nước gia đình bạn, hỗ trợ lắp đặt và bảo hành chính hãng.",
             "lien-he.html",
             ld(ld_org(), ld_website(),
                ld_page("lien-he.html", "Liên hệ BWT Barrier Việt Nam",
                        "Hotline %s — tư vấn chọn máy lọc nước BWT Barrier, "
                        "lắp đặt và bảo hành." % HOTLINE_TEXT,
                        ptype="ContactPage",
                        main=abs_url("lien-he.html") + "#business"),
                ld_crumb("lien-he.html", [("lien-he.html", "Liên hệ")]),
                ld_store()))
        + topbar() + header("lien-he.html")
        + crumb([("lien-he.html", "Liên hệ")])
        + """
<main id="main">
<section class="phead">
  <div class="wrap">
    <h1>Liên hệ &amp; tư vấn</h1>
    <p>Gọi hotline và cho chúng tôi biết nguồn nước nhà bạn là nước máy hay giếng khoan, có bị
       cáu cặn không — kỹ thuật viên sẽ gợi ý model phù hợp và báo giá ngay trong cuộc gọi.</p>
    <p style="margin-top:26px">
      <a class="btn btn--light btn--lg" href="tel:{tel}">{phone} Gọi ngay <span class="nb">{hot}</span></a>
    </p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cgrid cgrid--even">
      <div class="panel">
        <h2>Thông tin liên hệ</h2>
        <ul class="cinfo">
          <li>
            <span class="cinfo__ic">{phone}</span>
            <span><b>Hotline CSKH</b><a href="tel:{tel}" class="cinfo__big">{hot}</a>
              <span>Tư vấn chọn model, báo giá và đặt hàng</span></span>
          </li>
          <li>
            <span class="cinfo__ic">{pin}</span>
            <span><b>Địa chỉ</b><span>{addr}</span>
              <span><a href="{maplink}" target="_blank" rel="noopener">Xem đường đi</a></span></span>
          </li>
        </ul>
      </div>

      <div class="panel">
        <h2 id="bao-hanh">Chính sách bảo hành</h2>
        <ul class="checklist">
          <li>{chk}<span>Bảo hành chính hãng 36 tháng cho thân máy</span></li>
          <li>{chk}<span>Hỗ trợ lắp đặt và hướng dẫn thay lõi tại nhà</span></li>
          <li>{chk}<span>Nhắc lịch thay lõi định kỳ 12 tháng</span></li>
          <li>{chk}<span>Đổi trả theo quy định trong 7 ngày nếu lỗi từ nhà sản xuất</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec__head">
      <span class="eyebrow">Hệ thống phân phối</span>
      <h2>Mua hàng chính hãng ở đâu?</h2>
      <p>Sản phẩm BWT Barrier được phân phối qua hệ thống showroom và các chuỗi bán lẻ lớn trên toàn quốc.
         Gọi hotline để nhận báo giá và được hướng dẫn tới điểm bán gần bạn nhất.</p>
    </div>
    <div class="map">
      <iframe src="{map}" title="Bản đồ tới {addr}"
              loading="lazy" referrerpolicy="no-referrer-when-downgrade"
              allowfullscreen></iframe>
    </div>
    <p style="text-align:center;margin:18px 0 0;color:var(--muted);font-size:.92rem">
      <strong style="color:var(--navy)">{addr}</strong> ·
      <a href="{maplink}" target="_blank" rel="noopener">Mở trong Google Maps</a>
    </p>
  </div>
</section>

{cta}
</main>
""".format(phone=IC["phone"], pin=IC["pin"], chk=IC["check"],
           tel=HOTLINE_TEL, hot=HOTLINE_TEXT, addr=html.escape(ADDRESS),
           map=MAP_EMBED, maplink=MAP_LINK, cta=cta_band())
        + footer() + tail()
    )


# ============================================================
# BÀI VIẾT
# ============================================================
def fmt_date(iso):
    y, m, d = iso.split("-")
    return "%s/%s/%s" % (d, m, y)


def reading_time(html_body):
    words = len(re.sub(r"<[^>]+>", " ", html_body).split())
    return max(1, round(words / 220))


def post_card(a):
    return """<article class="post-card" data-cat="{cat}">
  <a class="post-card__media" href="{slug}.html">
    <img src="{cover}" alt="{alt}" loading="lazy"{dim}>
  </a>
  <div class="post-card__body">
    <span class="post-card__topic">{topic}</span>
    <h3 class="post-card__title"><a href="{slug}.html">{title}</a></h3>
    <p class="post-card__excerpt">{excerpt}</p>
    <div class="post-card__meta"><time datetime="{date}">{date_vi}</time> · {rt} phút đọc</div>
  </div>
</article>""".format(cat=a["topic"], slug=a["slug"], cover=a["cover"], alt=html.escape(a["cover_alt"]), dim=dims(a["cover"]),
                     topic=html.escape(a["topic_label"]), title=html.escape(a["title"]),
                     excerpt=html.escape(a["excerpt"]), date=a["date"], date_vi=fmt_date(a["date"]),
                     rt=reading_time(a["body"]))


def ld_article(a):
    url = abs_url(a["slug"] + ".html")
    return {
        "@type": "BlogPosting",
        "@id": url + "#article",
        "headline": a["title"],
        "description": a["desc"],
        "image": abs_url(a["cover"]),
        "datePublished": a["date"],
        "dateModified": a["date"],
        "inLanguage": "vi-VN",
        "articleSection": a["topic_label"],
        "wordCount": len(re.sub(r"<[^>]+>", " ", a["body"]).split()),
        "author": {"@id": ORG_ID},
        "publisher": {"@id": ORG_ID},
        "mainEntityOfPage": {"@id": url + "#webpage"},
        "isPartOf": {"@id": abs_url("bai-viet.html") + "#blog"},
    }


def page_blog():
    cards = "".join(post_card(a) for a in ARTICLES)
    topics = []
    for a in ARTICLES:
        if a["topic"] not in [t[0] for t in topics]:
            topics.append((a["topic"], a["topic_label"]))
    tabs = '<button class="tab" type="button" role="tab" data-filter="all" aria-selected="true">Tất cả ({})</button>'.format(len(ARTICLES))
    for key, label in topics:
        cnt = sum(1 for a in ARTICLES if a["topic"] == key)
        tabs += '<button class="tab" type="button" role="tab" data-filter="{k}" aria-selected="false">{l} ({c})</button>'.format(k=key, l=html.escape(label), c=cnt)
    blog_ld = {
        "@type": "Blog",
        "@id": abs_url("bai-viet.html") + "#blog",
        "name": "Bài viết — " + SITE_NAME,
        "url": abs_url("bai-viet.html"),
        "publisher": {"@id": ORG_ID},
        "blogPost": [{"@id": abs_url(a["slug"] + ".html") + "#article"} for a in ARTICLES],
    }
    return (
        head("Bài viết — Kiến thức lọc nước đầu nguồn và máy lọc nước",
             "Bài viết về lọc nước đầu nguồn, xử lý nước giếng khoan, cách chọn máy lọc nước gia đình và "
             "chu kỳ thay lõi — từ trung tâm bảo hành BWT Barrier.",
             "bai-viet.html",
             ld(ld_org(), ld_website(),
                ld_page("bai-viet.html", "Bài viết",
                        "Kiến thức về lọc nước đầu nguồn và máy lọc nước gia đình.",
                        ptype="CollectionPage", main=abs_url("bai-viet.html") + "#blog"),
                ld_crumb("bai-viet.html", [("bai-viet.html", "Bài viết")]),
                blog_ld))
        + topbar() + header("bai-viet.html")
        + crumb([("bai-viet.html", "Bài viết")])
        + """
<main id="main">
<section class="phead">
  <div class="wrap">
    <h1>Bài viết</h1>
    <p>Kiến thức thực tế về lọc nước đầu nguồn, xử lý nước giếng khoan, chọn máy lọc nước và bảo trì lõi lọc.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="tabs" role="tablist" aria-label="Lọc theo chủ đề">{tabs}</div>
    <h2 class="visually-hidden">Danh sách bài viết</h2>
    <div class="post-grid">{cards}</div>
  </div>
</section>

{cta}
</main>
""".format(tabs=tabs, cards=cards, cta=cta_band())
        + footer() + tail()
    )


def page_article(a):
    slug_url = a["slug"] + ".html"
    others = [x for x in ARTICLES if x["slug"] != a["slug"]][:3]
    related = "".join(post_card(x) for x in others)
    return (
        head(a.get("seo_title") or a["title"], a["desc"], slug_url,
             ld(ld_org(), ld_website(),
                ld_page(slug_url, a["title"], a["desc"], image=a["cover"],
                        ptype="WebPage", main=abs_url(slug_url) + "#article"),
                ld_crumb(slug_url, [("bai-viet.html", "Bài viết"), (slug_url, a["title"])]),
                ld_article(a)))
        + topbar() + header("bai-viet.html")
        + crumb([("bai-viet.html", "Bài viết"), (slug_url, a["title"])])
        + """
<main id="main">
<article class="post">
  <header class="post__head">
    <div class="wrap wrap--narrow">
      <span class="post__topic">{topic}</span>
      <h1>{title}</h1>
      <p class="post__meta">
        <time datetime="{date}">{date_vi}</time> · {rt} phút đọc · {site}
      </p>
    </div>
  </header>
  <div class="wrap wrap--narrow">
    <figure class="post__cover">
      <img src="{cover}" alt="{alt}"{dim} fetchpriority="high">
    </figure>
    <div class="post__body prose">
{body}
    </div>
  </div>
</article>

<section class="sec sec--tint">
  <div class="wrap">
    <div class="sec__head">
      <span class="eyebrow">Đọc tiếp</span>
      <h2>Bài viết liên quan</h2>
    </div>
    <div class="post-grid">{related}</div>
  </div>
</section>

{cta}
</main>
""".format(topic=html.escape(a["topic_label"]), title=html.escape(a["title"]),
           date=a["date"], date_vi=fmt_date(a["date"]), rt=reading_time(a["body"]), site=SITE_NAME,
           cover=a["cover"], alt=html.escape(a["cover_alt"]), dim=dims(a["cover"]),
           body=a["body"].strip(), related=related, cta=cta_band())
        + footer() + tail()
    )


# ============================================================
# TRANG TÌM KIẾM + 404
# ============================================================
def page_search():
    return (
        head("Tìm kiếm — BWT Barrier Việt Nam",
             "Tìm nhanh sản phẩm máy lọc nước và bộ tiền xử lý nước BWT Barrier.",
             "tim-kiem.html",
             '<meta name="robots" content="noindex">'
             + ld(ld_org(), ld_website(),
                  ld_page("tim-kiem.html", "Tìm kiếm", "Tìm sản phẩm BWT Barrier.",
                          ptype="SearchResultsPage",
                          has_crumb=False)))
        + topbar() + header("san-pham.html")
        + crumb([("tim-kiem.html", "Tìm kiếm")])
        + """
<main id="main">
<section class="phead">
  <div class="wrap">
    <h1 id="search-page-title">Tìm kiếm</h1>
    <p>Gõ tên model (BWT Barrier M, L, H), nhóm sản phẩm hoặc vấn đề nguồn nước bạn đang gặp.</p>
    <form class="sform" action="tim-kiem.html" method="get" role="search">
      <label class="visually-hidden" for="search-page-input">Từ khoá</label>
      <input id="search-page-input" name="q" type="search" placeholder="Ví dụ: nước cứng, có bộ đếm">
      <button class="btn btn--light" type="submit">Tìm</button>
    </form>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="pgrid" id="search-page-results"></div>
  </div>
</section>

{cta}
</main>
""".format(cta=cta_band())
        + footer() + tail()
    )


def page_404():
    return (
        head("Không tìm thấy trang — BWT Barrier Việt Nam",
             "Đường dẫn bạn vừa mở không tồn tại hoặc đã đổi tên. Quay lại trang chủ BWT Barrier "
             "Việt Nam để xem máy lọc nước và bộ tiền xử lý nước BWT Barrier chính hãng.",
             "404.html", '<meta name="robots" content="noindex">')
        + topbar() + header("index.html")
        + """
<main id="main">
<section class="phead">
  <div class="wrap">
    <h1>404 — Không tìm thấy trang</h1>
    <p>Đường dẫn bạn vừa mở không tồn tại hoặc đã được đổi tên.</p>
    <p style="margin-top:24px">
      <a class="btn btn--light" href="index.html">Về trang chủ</a>
      <a class="btn btn--outline-light" href="san-pham.html">Xem sản phẩm</a>
    </p>
  </div>
</section>
</main>
"""
        + footer() + tail()
    )


# ============================================================
# FAVICON / SITEMAP / ROBOTS
# ============================================================
def sitemap():
    urls = ["index.html", "san-pham.html", "ve-chung-toi.html", "lien-he.html", "bai-viet.html"] + \
           [p["slug"] + ".html" for p in PRODUCTS] + \
           [a["slug"] + ".html" for a in ARTICLES]
    body = "".join(
        "  <url><loc>{d}/{u}</loc><lastmod>{lm}</lastmod>"
        "<changefreq>monthly</changefreq><priority>{pr}</priority></url>\n".format(
            d=DOMAIN, u=u, lm=datetime.date.today().isoformat(),
            pr="1.0" if u == "index.html" else "0.8")
        for u in urls)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' \
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n"


ROBOTS = "User-agent: *\nAllow: /\nDisallow: /tim-kiem\n\nSitemap: {}/sitemap.xml\n".format(DOMAIN)


# ============================================================
# CHẠY
# ============================================================
# ============================================================
# DUONG DAN SACH (Vercel cleanUrls): bo duoi .html, index.html -> /
# Dat CLEAN_URLS = False neu host khong ho tro; khi do link giu nguyen .html.
# ============================================================
CLEAN_URLS = True

_RE_LINK = re.compile(r'((?:href|action)=")([A-Za-z0-9._-]+)\.html((?:[?#][^"]*)?")')
_RE_ABS = re.compile(re.escape(DOMAIN) + r'/([A-Za-z0-9._-]+)\.html')


def clean_urls(text):
    """Doi moi link noi bo sang dang khong duoi .html."""
    if not CLEAN_URLS:
        return text

    def _link(m):
        pre, page, rest = m.groups()
        return pre + ("/" if page == "index" else "/" + page) + rest

    def _abs(m):
        page = m.group(1)
        return DOMAIN + ("/" if page == "index" else "/" + page)

    return _RE_ABS.sub(_abs, _RE_LINK.sub(_link, text))


def write(path, content):
    full = os.path.join(ROOT, path)
    d = os.path.dirname(full)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    if path.endswith((".html", ".xml")):
        content = clean_urls(content)
    with io.open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("  {:<38} {:>7,} bytes".format(path, len(content.encode("utf-8"))))


def main():
    print("Dang sinh trang tinh cho bwtbarrier.com.vn ...")
    write("index.html", page_index())
    write("san-pham.html", page_products())
    for p in PRODUCTS:
        write(p["slug"] + ".html", page_product(p))
    write("ve-chung-toi.html", page_about())
    write("lien-he.html", page_contact())
    write("tim-kiem.html", page_search())
    write("bai-viet.html", page_blog())
    for a in ARTICLES:
        write(a["slug"] + ".html", page_article(a))
    write("404.html", page_404())
    write("sitemap.xml", sitemap())
    write("robots.txt", ROBOTS)
    print("Xong.")


if __name__ == "__main__":
    main()
