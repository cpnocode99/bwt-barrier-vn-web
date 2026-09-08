# bwtbarrier.com.vn — website tĩnh

Website giới thiệu thương hiệu và sản phẩm **BWT Barrier iMaster** tại Việt Nam.
Trang tĩnh: chỉ HTML + CSS + JS, không cần server, không database, không build tool ngoài Python.

---

## Chạy thử

```bash
cd d:/Project/web_bwt
python serve.py            # http://127.0.0.1:8000
```

Dùng `serve.py` chứ **đừng** dùng `python -m http.server`: site chạy đường dẫn không có
đuôi `.html` (`/san-pham` thay vì `/san-pham.html`) giống hệt Vercel, `http.server`
thường sẽ trả 404. `serve.py` cũng trả đúng trang `404.html`.

---

## Cấu trúc

```
index.html                          Trang chủ
san-pham.html                       Danh mục 8 sản phẩm + tab lọc nhóm
may-loc-nuoc-imaster-m.html         ─┐
may-loc-nuoc-imaster-l.html          │
may-loc-nuoc-imaster-h.html          │
may-loc-nuoc-imaster-m-co-bo-dem.html├─ 8 trang chi tiết sản phẩm
may-loc-nuoc-imaster-l-co-bo-dem.html│
may-loc-nuoc-imaster-h-co-bo-dem.html│
bo-tien-xu-ly-imaster-ion-m.html     │
bo-tien-xu-ly-imaster-ion-h.html    ─┘
ve-chung-toi.html                   Giới thiệu thương hiệu BWT Barrier
lien-he.html                        Liên hệ + form đăng ký tư vấn
tim-kiem.html                       Trang kết quả tìm kiếm
404.html                            Trang lỗi
sitemap.xml, robots.txt

assets/css/style.css                Toàn bộ CSS
assets/js/search-index.js           Chỉ mục tìm kiếm (data)
assets/js/main.js                   Menu, search, tab lọc, gallery, form
assets/img/barrier-logo.png         Logo BARRIER (xanh, dùng ở header)
assets/img/barrier-logo-white.png   Logo BARRIER (trắng, dùng ở footer)
assets/img/favicon.ico              Favicon (16/32/48) + favicon-32.png
assets/img/apple-touch-icon.png     Icon 180px cho iOS
assets/img/*-hero.webp              Ảnh sản phẩm đã tách nền (WebP trong suốt)
assets/img/*-meter-hero.webp        Bản kèm bộ đếm Water Meter
assets/img/og-image.jpg             Ảnh chia sẻ mạng xã hội

build.py                            Bộ sinh HTML — sửa nội dung ở đây rồi chạy lại
```

**Mọi file `.html` đều do `build.py` sinh ra.** Đừng sửa tay file HTML — sửa
`build.py` rồi chạy `python build.py`, nếu không thay đổi sẽ bị ghi đè ở lần build sau.

---

## Sửa thông tin liên hệ

Mở `build.py`, sửa khối ngay đầu file rồi chạy `python build.py`:

```python
HOTLINE_TEXT = "0896 613 768"                          # số hiển thị
HOTLINE_TEL  = "+84896613768"                          # số cho link tel:
ADDRESS      = "90 Đinh Thị Thi, Hiệp Bình, Hồ Chí Minh"
```

Số hotline xuất hiện ở: topbar, nút gọi cố định góc phải, thanh hành động dưới màn hình
điện thoại, khối CTA, trang chi tiết sản phẩm, trang liên hệ và footer — tất cả đều lấy
từ hằng số trên nên chỉ cần sửa một chỗ.

Website hiện chỉ dùng **một kênh liên hệ là điện thoại** — không có email, Zalo hay
Messenger. Muốn thêm lại, khai báo hằng số mới trong `build.py` và chèn vào `topbar()`,
`dock()` hoặc `page_contact()`.

---

## Sửa / thêm sản phẩm

1. Sửa mảng `PRODUCTS` trong `build.py`. Mỗi sản phẩm gồm:

   | Khoá | Ý nghĩa |
   |---|---|
   | `slug` | tên file, ví dụ `may-loc-nuoc-imaster-m` → `may-loc-nuoc-imaster-m.html` |
   | `cat` | `may-loc`, `co-bo-dem` hoặc `tien-xu-ly` (dùng cho tab lọc) |
   | `price`, `price_note` | giá hiển thị và ghi chú dưới giá — hiện để `"Liên hệ"` cho mọi sản phẩm |
   | `sibling` | `(slug, nhãn)` của bản đối ứng — hiện thành ô liên kết ở trang chi tiết, để `None` nếu không có |
   | `images` | danh sách `(đường dẫn, alt)` — mỗi sản phẩm đang dùng **một ảnh**; thêm ảnh thứ hai thì dải ảnh nhỏ tự hiện lại |
   | `usps` | gạch đầu dòng điểm nổi bật (3 dòng đầu hiện trên thẻ sản phẩm) |
   | `specs` | bảng thông số `(tên, giá trị)` |
   | `intro`, `best_for` | đoạn giới thiệu và dòng "phù hợp với" |

2. Thêm bản ghi tương ứng vào `assets/js/search-index.js` để sản phẩm xuất hiện trong ô tìm kiếm.
   Trường `keys` là chuỗi từ khoá **không dấu**, viết thường.

3. Chạy `python build.py`. Số đếm trên các nút tab tự tính theo `cat` nên không cần sửa tay.

### Tách nền ảnh sản phẩm

Ảnh sản phẩm đều là PNG nền trong suốt, tách bằng [rembg](https://github.com/danielgatis/rembg):

```bash
pip install rembg onnxruntime
```

Script tách nền và ghép ảnh "có bộ đếm" nằm ngoài repo; muốn tách nền ảnh mới:

```python
from rembg import remove, new_session
from PIL import Image
img = Image.open("anh-goc.png").convert("RGB")
out = remove(img, session=new_session("u2net"), post_process_mask=True).convert("RGBA")
out.crop(out.split()[-1].getbbox()).save("anh-da-tach-nen.png")
```

Sau khi tách nền, chuyển sang WebP để nhẹ hơn khoảng 85%:

```python
Image.open("anh-da-tach-nen.png").convert("RGBA").save(
    "anh.webp", "WEBP", quality=88, method=6)
```

Rồi thêm đường dẫn `.webp` vào `images` trong `build.py` và `img` trong
`assets/js/search-index.js`.

---

## Tìm kiếm

Tìm kiếm chạy hoàn toàn phía client trên `window.BWT_INDEX`:

- không phân biệt hoa thường và **không phân biệt dấu** — gõ `nuoc cung` vẫn ra `iMaster H`;
- gợi ý dropdown ngay dưới ô tìm kiếm ở mọi trang;
- Enter chuyển sang `tim-kiem.html?q=...` hiển thị đầy đủ kết quả.

---

## Trang liên hệ

Trang liên hệ **không có form** — theo yêu cầu, kênh nhận khách là hotline.
Trang gồm: nút gọi lớn ở đầu trang, thẻ thông tin liên hệ (hotline + địa chỉ + link chỉ đường),
thẻ chính sách bảo hành, và bản đồ Google Maps.

Nếu sau này muốn thêm form, cần một nơi nhận dữ liệu vì đây là site tĩnh — Formspree,
Google Apps Script hoặc một Vercel Serverless Function trong thư mục `api/`.

---

## SEO

Đã xử lý sẵn:

- `<title>` và `<meta description>` riêng cho từng trang, không trùng lặp, độ dài trong
  ngưỡng Google hiển thị
- `canonical`, `og:*` (kèm `og:locale=vi_VN`), `twitter:card` + `twitter:image`
- Đúng một `<h1>` mỗi trang, không nhảy bậc tiêu đề
- Mọi `<img>` có `alt` và `width`/`height` thật (CLS = 0), ảnh dưới màn hình đầu dùng
  `loading="lazy"`
- `sitemap.xml` có `lastmod`, chỉ liệt kê trang được index; `robots.txt` chặn `/tim-kiem`
- `tim-kiem` và `404` gắn `noindex`
- Ảnh WebP: tổng thư mục ảnh 592 KB

### Schema.org

Mỗi trang xuất một khối `<script type="application/ld+json">` chứa `@graph`, các thực thể
tham chiếu nhau bằng `@id` thay vì lặp lại dữ liệu:

| Thực thể | Có ở đâu | Nội dung chính |
|---|---|---|
| `Organization` (`#organization`) | mọi trang | tên, logo `ImageObject`, hotline, địa chỉ, `contactPoint`, `areaServed` |
| `WebSite` (`#website`) | mọi trang | `publisher` → Organization, `SearchAction` trỏ `/tim-kiem?q=` |
| `WebPage` / `ItemPage` / `CollectionPage` / `AboutPage` / `ContactPage` / `SearchResultsPage` | theo từng trang | `isPartOf`, `breadcrumb`, `primaryImageOfPage`, `mainEntity` |
| `BreadcrumbList` | 11 trang con | khớp đúng breadcrumb hiển thị |
| `Product` | 8 trang sản phẩm | ảnh, `brand`, `manufacturer`, `additionalProperty` (toàn bộ bảng thông số), `width`/`height`/`depth`/`weight` tự tách từ specs, `isSimilarTo` trỏ bản đối ứng |
| `ItemList` | trang chủ + danh mục | 8 sản phẩm theo thứ tự |
| `Store` | trang liên hệ | địa chỉ, `geo` toạ độ, `hasMap`, `parentOrganization` |

**Không khai `Offer`**: giá đang để "Liên hệ", mà Google bắt buộc `Offer` phải có `price`.
Khai một Offer thiếu giá chỉ tạo cảnh báo trong Search Console. Khi có bảng giá chính thức,
điền `price` vào `PRODUCTS` rồi bật lại khối `Offer` trong hàm `ld_product()` — chỗ đó còn
ghi chú sẵn.

Các hàm sinh schema nằm trong `build.py`: `ld()`, `ld_org()`, `ld_website()`, `ld_page()`,
`ld_crumb()`, `ld_product()`, `ld_itemlist()`, `ld_store()`.

### Kiểm tra nhanh sau khi build

```bash
grep -c "BreadcrumbList" *.html          # 11 trang con phải có
grep -o "<title>[^<]*</title>" *.html    # không được trùng, dưới 65 ký tự
```

Sau khi lên domain thật, dán URL vào [Rich Results Test](https://search.google.com/test/rich-results)
và [Schema Markup Validator](https://validator.schema.org/) để xác nhận lần cuối.

---

## Bản đồ

Trang liên hệ nhúng Google Maps qua iframe không cần API key. Sửa `MAP_EMBED` và
`MAP_LINK` ở đầu `build.py`; `MAP_EMBED` theo mẫu:

```
https://www.google.com/maps?q=<vĩ độ>,<kinh độ>&amp;hl=vi&amp;z=17&amp;output=embed
```

Toạ độ hiện tại `10.845839,106.712965` lấy từ link rút gọn
[maps.app.goo.gl/h5tJqBYY9ZJqJzLB9](https://maps.app.goo.gl/h5tJqBYY9ZJqJzLB9).

---
## Triển khai lên Vercel qua GitHub

1. Push thư mục này lên một repo GitHub.
2. Vercel → **Add New Project** → chọn repo đó.
3. Framework Preset để **Other**, Build Command và Output Directory **để trống**
   (site đã là HTML tĩnh, Vercel chỉ việc phục vụ thẳng thư mục gốc).
4. Deploy.

### Đường dẫn sạch — không có `index.html`

`vercel.json` đã bật `cleanUrls: true` và `trailingSlash: false`, nên:

| Trang | URL |
|---|---|
| Trang chủ | `https://tenmien.com/` |
| Danh mục | `https://tenmien.com/san-pham` |
| Sản phẩm | `https://tenmien.com/may-loc-nuoc-imaster-m` |
| Liên hệ | `https://tenmien.com/lien-he` |

Toàn bộ link nội bộ, `canonical`, `og:url`, JSON-LD và `sitemap.xml` đều đã sinh ra ở
dạng này — không còn chuỗi `.html` nào. Việc bỏ đuôi do hàm `clean_urls()` trong
`build.py` xử lý lúc ghi file; đổi `CLEAN_URLS = False` nếu chuyển sang host không hỗ trợ.

`vercel.json` cũng đặt cache 1 năm cho `/assets/*` và vài header bảo mật cơ bản.

### Sau khi gắn domain thật

Kiểm tra `DOMAIN` trong `build.py` (đang là `https://bwtbarrier.com.vn`) — giá trị này
dùng cho `canonical`, Open Graph và `sitemap.xml`. Đổi xong nhớ chạy lại `python build.py`.
Nếu chạy trên `*.vercel.app` mà chưa gắn domain, canonical sẽ trỏ sai; nên gắn domain
trước khi gửi sitemap cho Google.

---

## Nguồn nội dung & hình ảnh

- Thông tin thương hiệu: [Dân trí — "BWT Barrier iMaster: Máy lọc nước nổi tiếng thế giới đã đến Việt Nam"](https://dantri.com.vn/doi-song/bwt-barrier-imaster-may-loc-nuoc-noi-tieng-the-gioi-da-den-viet-nam-20220225145502887.htm)
- Thông số kỹ thuật: các trang sản phẩm trên thegioidiengiai.com (nhà phân phối)
- Ảnh sản phẩm: tải từ CDN nhà phân phối, đã **cắt bỏ watermark và logo nhà bán lẻ**
  để dùng cho website thương hiệu.
- Logo BARRIER: bản tiếng Anh lấy từ website chính thức barrier.ph, đã tách nền và
  đổi màu sang xanh thương hiệu (`#1F4E9C`) cho bản dùng trên nền sáng.
- Favicon: cắt phần giọt nước từ ảnh logo do khách cung cấp.
- Ảnh "có bộ đếm" của iMaster M và H: ghép bộ đếm Water Meter (tách từ ảnh iMaster L)
  cạnh cụm lõi tương ứng — **nên thay bằng ảnh chụp thật khi có**.

> ⚠️ **Cần bổ sung trước khi công bố:**
> - Toàn bộ 8 sản phẩm đang để giá **"Liên hệ"**. Khi có bảng giá chính thức, điền
>   `price` trong `PRODUCTS` và bật lại khối `Offer` trong `ld_product()`.
> - Ảnh "có bộ đếm" của iMaster M và H là ảnh ghép — nên thay bằng ảnh chụp thật.

---

## Quy ước nội dung

Khi viết thêm nội dung cho site, giữ hai quy tắc sau:

1. **Không dùng từ ngữ tuyệt đối** — tránh "số 1", "nhất", "duy nhất", "100%", "hoàn toàn",
   "triệt để", "hàng đầu"… Viết theo hướng mô tả sự thật kiểm chứng được.
2. **Luôn viết đủ "BWT Barrier"**, không để "BWT" đứng một mình. Khi nói về tập đoàn thì
   dùng "BWT Group".

Kiểm tra nhanh sau khi build:

```bash
grep -ohiE "(nhất|số 1|100%|hoàn toàn|triệt để|hàng đầu|duy nhất)" *.html
grep -ohP "BWT(?!\s(?:Barrier|Group|BARRIER|WATER|Water))" *.html
```
