# -*- coding: utf-8 -*-
"""
Bài viết kiến thức — dữ liệu cho build.py.

Mỗi bài là một dict:
  slug      tên file / URL, ví dụ "loc-nuoc-dau-nguon-la-gi" -> /loc-nuoc-dau-nguon-la-gi
  title     tiêu đề H1 (cũng là <title> nếu không có seo_title)
  seo_title <title> riêng cho Google, dưới 65 ký tự
  desc      meta description 110-165 ký tự
  topic     "loc-dau-nguon" hoặc "may-loc-nuoc" (dùng để lọc trên trang danh sách)
  topic_label
  date      YYYY-MM-DD
  cover     ảnh 16:9 trong assets/img
  cover_alt
  excerpt   1-2 câu hiện trên thẻ bài viết
  body      HTML nội dung, bắt đầu từ <p> hoặc <h2> (H1 do template sinh)
  keys      từ khoá không dấu cho ô tìm kiếm

Quy ước nội dung (xem README): không dùng từ tuyệt đối, không nhắc "BWT" đứng một mình,
không nêu chứng nhận. Link ra đối tác để nguyên dofollow (không rel="nofollow").
"""

TGLT = 'href="https://thegioiloctong.com/" target="_blank" rel="noopener"'
TGDG = 'href="https://thegioidiengiai.com/" target="_blank" rel="noopener"'

ARTICLES = [
    # ================================================================== 1
    {
        "slug": "loc-nuoc-dau-nguon-la-gi",
        "title": "Lọc nước đầu nguồn là gì? Khi nào gia đình nên lắp hệ thống lọc tổng",
        "seo_title": "Lọc nước đầu nguồn là gì? Khi nào nên lắp lọc tổng",
        "desc": "Lọc nước đầu nguồn (lọc tổng) xử lý nước ngay tại điểm cấp vào nhà. Dấu hiệu cần lắp, "
                "cấu tạo hệ thống và cách kết hợp với máy lọc nước uống ở bếp.",
        "topic": "loc-dau-nguon",
        "topic_label": "Lọc nước đầu nguồn",
        "date": "2026-09-11",
        "cover": "assets/img/bai-loc-nuoc-dau-nguon.webp",
        "cover_alt": "Hệ thống lọc nước đầu nguồn với các cột lọc và đường ống lắp ngoài trời",
        "excerpt": "Máy lọc ở bếp chỉ xử lý nước uống. Phần còn lại — nước tắm, giặt, rửa, nước vào bình nóng "
                   "lạnh — đi thẳng từ đường ống vào nhà. Lọc đầu nguồn là lớp bảo vệ cho phần đó.",
        "keys": "loc nuoc dau nguon loc tong he thong loc tong cot loc cat than hoat tinh gieng khoan nuoc may cau can",
        "body": """
<p>Khi nói tới "lọc nước", phần lớn gia đình nghĩ ngay đến chiếc máy lọc đặt ở bếp. Nhưng chiếc máy đó
chỉ xử lý vài lít nước uống mỗi ngày. Hàng trăm lít còn lại — nước tắm, giặt, rửa bát, nước cấp cho
bình nóng lạnh, máy giặt, vòi sen — đi thẳng từ đường ống vào nhà mà không qua bất kỳ lớp lọc nào.
<strong>Lọc nước đầu nguồn</strong> (còn gọi là <strong>lọc tổng</strong>) sinh ra để xử lý phần nước đó.</p>

<h2>Lọc nước đầu nguồn là gì?</h2>
<p>Đây là hệ thống lọc đặt tại điểm nước cấp vào nhà — thường ngay sau đồng hồ nước hoặc sau bồn chứa —
để toàn bộ nước sinh hoạt đều đi qua lọc trước khi tới bất kỳ vòi nào. Mục tiêu không phải là tạo ra nước
uống trực tiếp, mà là loại bỏ cặn lơ lửng, phèn sắt, mangan, clo dư và mùi lạ, đưa nước về mức "sạch cho
sinh hoạt" và bảo vệ thiết bị phía sau.</p>

<p>Một hệ thống lọc tổng dân dụng thường gồm hai đến bốn cột lọc nối tiếp, mỗi cột đảm nhiệm một việc:</p>
<ul>
  <li><strong>Cột lọc thô</strong> (cát thạch anh, sỏi): giữ lại cặn, bùn, rỉ sét có kích thước lớn.</li>
  <li><strong>Cột khử phèn / mangan</strong> (hạt Birm, cát mangan, Filox): oxy hoá và giữ lại sắt, mangan —
      nguyên nhân gây ố vàng thiết bị vệ sinh.</li>
  <li><strong>Cột than hoạt tính</strong>: hấp phụ clo dư, mùi, màu và một phần hợp chất hữu cơ.</li>
  <li><strong>Cột làm mềm</strong> (hạt trao đổi ion cation): giảm độ cứng, hạn chế cáu cặn canxi ở bình
      nóng lạnh, vòi sen và ấm đun.</li>
</ul>
<p>Không phải nguồn nước nào cũng cần đủ bốn cột. Cấu hình được chọn sau khi biết nguồn nước thực tế là gì —
nước máy đô thị, nước giếng khoan, hay nước mưa trữ bồn.</p>

<h2>Dấu hiệu gia đình nên lắp lọc đầu nguồn</h2>
<p>Nếu gặp từ hai trong các hiện tượng dưới đây, nguồn nước nhà bạn đang có vấn đề ở mức cần xử lý
từ đầu nguồn chứ không chỉ ở vòi uống:</p>
<ul>
  <li>Bồn cầu, lavabo, gạch nhà tắm <strong>ố vàng hoặc nâu</strong> dù vệ sinh thường xuyên — dấu hiệu
      của sắt (phèn) hoặc mangan.</li>
  <li>Vòi sen, ấm đun, bình nóng lạnh <strong>đóng cặn trắng</strong> — nước cứng, nhiều canxi và magie.</li>
  <li>Nước có <strong>mùi clo</strong> rõ, đặc biệt vào buổi sáng hoặc sau khi nhà máy nước súc rửa đường ống.</li>
  <li>Nước để lắng qua đêm thấy <strong>lớp cặn hoặc váng</strong> dưới đáy xô.</li>
  <li>Quần áo giặt xong nhanh xỉn màu, da khô hoặc ngứa sau khi tắm.</li>
  <li>Lõi thô của máy lọc ở bếp <strong>bẩn rất nhanh</strong>, phải thay sớm hơn khuyến nghị nhiều lần.</li>
</ul>
<p>Điểm cuối cùng đáng chú ý: lõi máy lọc uống hết hạn sớm là hệ quả trực tiếp của nước đầu vào quá bẩn.
Lắp lọc tổng phía trước giúp máy lọc uống phía sau chạy đúng tuổi thọ thiết kế, tiết kiệm chi phí thay lõi
về lâu dài.</p>

<h2>Lọc đầu nguồn và máy lọc nước uống: hai lớp, hai nhiệm vụ</h2>
<p>Hai hệ thống này không thay thế nhau. Lọc tổng làm sạch nước ở mức sinh hoạt cho cả nhà; máy lọc uống
ở bếp tinh lọc thêm một lần để đạt chuẩn uống trực tiếp. Cách kết hợp thường gặp:</p>
<ol>
  <li><strong>Lọc tổng</strong> tại điểm cấp vào nhà → xử lý phèn, cặn, clo, độ cứng cho toàn bộ nước.</li>
  <li><strong>Máy lọc uống</strong> tại bếp → lọc tinh, giữ hoặc bổ sung khoáng tuỳ công nghệ.</li>
  <li>Nếu dùng máy điện giải ion kiềm, thêm <strong>bộ tiền xử lý</strong> ngay trước máy để bảo vệ buồng
      điện phân.</li>
</ol>
<p>Với lớp thứ hai, bạn có thể tham khảo <a href="san-pham.html">dòng máy lọc nước BWT Barrier</a> lắp âm tủ
— lọc bằng áp lực nước, không dùng điện, không xả nước thải. Với máy điện giải ion kiềm, đơn vị chuyên về
mảng này là <a %(TGDG)s>Thế Giới Điện Giải</a>.</p>

<h2>Chi phí và bảo trì</h2>
<p>Hệ thống lọc tổng dân dụng có giá dao động rộng tuỳ lưu lượng (số vòi dùng đồng thời), loại vật liệu lọc
và có van tự động sục rửa hay không. Vật liệu lọc cần <strong>sục rửa định kỳ</strong> (van tự động làm việc
này theo lịch) và <strong>thay vật liệu</strong> sau khoảng 2–5 năm tuỳ chất lượng nước đầu vào.</p>
<p>Trước khi quyết định, nên lấy mẫu nước đi xét nghiệm hoặc nhờ đơn vị lắp đặt đo nhanh các chỉ số cơ bản
(sắt, độ cứng, pH, clo dư). Chọn cấu hình theo số liệu thật sẽ tránh được việc lắp thừa cột không cần
hoặc thiếu cột cần.</p>

<h2>Nên tìm đơn vị tư vấn ở đâu?</h2>
<p>Lọc tổng là hạng mục cần khảo sát tại chỗ: vị trí đặt, áp lực nước, đường thoát nước sục rửa, và quan
trọng là kết quả phân tích nguồn nước. <a %(TGLT)s>Thế Giới Lọc Tổng</a> là đơn vị chuyên về hệ thống lọc
nước đầu nguồn cho gia đình và công trình, có thể khảo sát và đề xuất cấu hình theo nguồn nước cụ thể
của bạn.</p>
<p>Còn phần máy lọc uống và bảo hành sau lắp đặt, trung tâm chúng tôi hỗ trợ qua
<a href="lien-he.html">hotline CSKH</a>.</p>
""",
    },

    # ================================================================== 2
    {
        "slug": "nuoc-gieng-khoan-nhiem-phen-xu-ly-the-nao",
        "title": "Nước giếng khoan nhiễm phèn, đá vôi: xử lý từ đầu nguồn hay lọc tại vòi?",
        "seo_title": "Nước giếng khoan nhiễm phèn, đá vôi: xử lý thế nào?",
        "desc": "Nước giếng khoan thường nhiễm phèn, mangan và đá vôi. Vì sao máy lọc ở bếp không đủ, "
                "lọc đầu nguồn cần những gì và kết hợp máy lọc uống, máy điện giải ra sao.",
        "topic": "loc-dau-nguon",
        "topic_label": "Lọc nước đầu nguồn",
        "date": "2026-09-11",
        "cover": "assets/img/bai-nuoc-gieng-khoan.webp",
        "cover_alt": "Bồn chứa nước trên mái nhà với đường ống dẫn xuống",
        "excerpt": "Nước giếng trong vắt lúc bơm lên nhưng để một lúc lại ngả vàng, đóng cặn, tanh mùi sắt. "
                   "Đó là chuyện của cả đường ống, không riêng gì vòi uống.",
        "keys": "nuoc gieng khoan nhiem phen sat mangan da voi nuoc cung xu ly loc tong loc dau nguon bo tien xu ly",
        "body": """
<p>Nhiều gia đình ở ngoại thành và các tỉnh vẫn dùng nước giếng khoan làm nguồn chính. Nước bơm lên nhìn
trong, nhưng để qua một buổi thì ngả vàng, có váng, tanh mùi sắt; ấm đun sau vài tuần đóng một lớp cặn
trắng cứng. Hai hiện tượng đó là <strong>nhiễm phèn</strong> (sắt, mangan) và <strong>nước cứng</strong>
(đá vôi — canxi, magie). Câu hỏi thường gặp: chỉ cần mua máy lọc nước tốt đặt ở bếp có đủ không?</p>

<h2>Vì sao máy lọc ở bếp không giải quyết được gốc vấn đề</h2>
<p>Máy lọc uống được thiết kế cho nước đầu vào đã tương đối sạch — thường là nước máy đô thị. Khi nối thẳng
vào nước giếng nhiễm phèn:</p>
<ul>
  <li>Lõi thô bám sắt kết tủa, <strong>tắc chỉ sau vài tuần</strong> thay vì 6–12 tháng.</li>
  <li>Cặn canxi phủ lên bề mặt các lõi phía sau, giảm lưu lượng và hiệu quả lọc.</li>
  <li>Với máy RO, màng lọc bị "đóng vảy" sớm; với máy điện giải ion kiềm, <strong>tấm điện cực bị bám cặn</strong>
      — bộ phận tốn kém khi phải thay.</li>
</ul>
<p>Quan trọng hơn: nước phèn và nước cứng vẫn đang chảy vào máy giặt, bình nóng lạnh, vòi sen, bồn cầu —
những nơi máy lọc uống không thể chạm tới. Thiết bị ố vàng, đóng cặn, giảm tuổi thọ là chi phí âm thầm
mà nhiều nhà không tính vào.</p>

<h2>Xử lý từ đầu nguồn: đúng chỗ, đúng thứ tự</h2>
<p>Với nước giếng, hệ thống lọc đầu nguồn thường được ghép theo thứ tự sau:</p>
<ol>
  <li><strong>Oxy hoá sắt</strong>: nước bơm lên được làm thoáng (giàn phun mưa, ejector, hoặc châm hoá chất
      oxy hoá) để sắt hoà tan chuyển thành kết tủa có thể lọc được.</li>
  <li><strong>Cột lọc phèn</strong>: vật liệu chuyên dụng (cát mangan, Birm, Filox) giữ lại sắt và mangan
      đã kết tủa.</li>
  <li><strong>Cột than hoạt tính</strong>: khử mùi tanh, màu vàng còn sót và hợp chất hữu cơ.</li>
  <li><strong>Cột làm mềm</strong> nếu độ cứng cao: hạt trao đổi ion giữ canxi, magie; tái sinh bằng muối
      theo chu kỳ.</li>
</ol>
<p>Tuỳ hàm lượng sắt, có nguồn chỉ cần cột phèn đơn giản, có nguồn phải làm thoáng kỹ và lắng trước.
Đây là lý do <strong>xét nghiệm nước trước khi lắp</strong> gần như là bắt buộc với giếng khoan — số liệu
sắt, mangan, độ cứng, pH quyết định cấu hình, không phải cảm quan.</p>

<h2>Sau lọc tổng, nước uống xử lý tiếp thế nào?</h2>
<p>Nước ra khỏi hệ thống lọc tổng đã hết phèn, giảm cứng, không mùi — đủ sạch cho sinh hoạt nhưng chưa
phải nước uống trực tiếp. Lớp thứ hai ở bếp có vài hướng:</p>
<ul>
  <li><strong>Máy lọc giữ khoáng</strong> như <a href="san-pham.html">BWT Barrier</a>: lọc tinh, giữ lại
      canxi, magie ở mức có lợi, không dùng điện, không nước thải. Với vùng nước cứng, bản
      <a href="may-loc-nuoc-bwt-barrier-h.html">BWT Barrier H</a> có lõi làm mềm riêng.</li>
  <li><strong>Máy điện giải ion kiềm</strong>: tạo nước kiềm giàu hydro. Với nước giếng, nên có thêm
      <a href="bo-tien-xu-ly-bwt-barrier-ion-h.html">bộ tiền xử lý</a> ngay trước máy để bảo vệ buồng điện
      phân. Tham khảo dòng máy và tư vấn tại <a %(TGDG)s>Thế Giới Điện Giải</a>.</li>
</ul>

<h2>Câu hỏi thường gặp</h2>
<h3>Nước giếng của tôi nhìn rất trong, có cần lọc tổng không?</h3>
<p>Sắt hoà tan (Fe²⁺) không màu; chỉ khi gặp không khí mới oxy hoá thành Fe³⁺ màu vàng. Nước "trong lúc bơm,
vàng khi để" chính là dấu hiệu nhiễm phèn. Để chắc, hãy xét nghiệm.</p>
<h3>Lọc tổng có làm giảm áp lực nước không?</h3>
<p>Hệ thống được chọn đúng lưu lượng sẽ không gây tụt áp đáng kể. Tụt áp thường xảy ra khi vật liệu lọc
đã bão hoà mà chưa sục rửa — dấu hiệu cần bảo trì.</p>
<h3>Bao lâu thay vật liệu lọc?</h3>
<p>Thường 2–4 năm với nước giếng, tuỳ tải phèn. Van tự động sục rửa giúp kéo dài tuổi thọ vật liệu.</p>

<h2>Bắt đầu từ đâu</h2>
<p>Khảo sát nguồn nước, chọn cấu hình lọc tổng phù hợp và thi công là việc của đơn vị chuyên về lọc đầu
nguồn — <a %(TGLT)s>Thế Giới Lọc Tổng</a> nhận khảo sát và tư vấn theo kết quả xét nghiệm thực tế.
Phần máy lọc uống, bộ tiền xử lý và bảo hành sau lắp đặt, bạn liên hệ trung tâm qua
<a href="lien-he.html">hotline CSKH</a>.</p>
""",
    },

    # ================================================================== 3
    {
        "slug": "chon-may-loc-nuoc-gia-dinh-ro-nano-hay-dien-giai",
        "title": "Chọn máy lọc nước gia đình: RO, Nano hay điện giải ion kiềm?",
        "seo_title": "Chọn máy lọc nước gia đình: RO, Nano hay điện giải?",
        "desc": "So sánh ba nhóm máy lọc nước — RO, lọc giữ khoáng và điện giải ion kiềm — theo nguồn nước, "
                "nhu cầu và chi phí vận hành, kèm gợi ý chọn theo hoàn cảnh gia đình.",
        "topic": "may-loc-nuoc",
        "topic_label": "Máy lọc nước",
        "date": "2026-09-11",
        "cover": "assets/img/bai-chon-may-loc-nuoc.webp",
        "cover_alt": "Máy lọc nước lắp âm tủ với bộ lõi ba cấp và vòi lấy nước",
        "excerpt": "Không có máy nào hợp với mọi nhà. Câu trả lời phụ thuộc vào nguồn nước đầu vào, bạn muốn nước "
                   "ra như thế nào, và sẵn sàng bỏ bao nhiêu cho điện, nước thải và lõi thay.",
        "keys": "chon may loc nuoc gia dinh ro nano dien giai ion kiem giu khoang so sanh khong dien nuoc thai",
        "body": """
<p>Thị trường máy lọc nước có ba nhóm công nghệ chính, và mỗi nhóm giải quyết một bài toán khác nhau.
Chọn sai không hỏng gì, nhưng bạn sẽ trả tiền cho thứ mình không cần — hoặc thiếu thứ mình cần.
Dưới đây là cách nhìn theo <strong>nguồn nước</strong> và <strong>nhu cầu</strong>, thay vì theo quảng cáo.</p>

<h2>Ba nhóm công nghệ, ba cách tiếp cận</h2>

<h3>1. Máy lọc RO (thẩm thấu ngược)</h3>
<p>Dùng bơm đẩy nước qua màng có lỗ cực nhỏ, giữ lại gần như mọi thứ — kể cả khoáng chất. Nước ra tinh
khiết, phù hợp nguồn nước đầu vào kém hoặc chưa rõ chất lượng. Đổi lại: <strong>cần điện</strong>,
<strong>xả nước thải</strong> (thường 1–3 phần nước thải cho 1 phần nước tinh), và nước ra "trơ" — nhiều
máy phải gắn thêm lõi bù khoáng.</p>

<h3>2. Máy lọc giữ khoáng (Nano / trao đổi ion)</h3>
<p>Không dùng màng RO mà kết hợp lõi cặn, than hoạt tính, hạt trao đổi ion và màng nano. Loại bỏ cặn,
clo, kim loại nặng, vi khuẩn nhưng <strong>giữ lại canxi, magie</strong>. Ưu điểm: không cần điện, không
nước thải, lắp gọn. Điều kiện: nước đầu vào cần tương đối sạch — nước máy đô thị, hoặc nước giếng đã qua
lọc đầu nguồn.</p>
<p>Dòng <a href="san-pham.html">BWT Barrier</a> thuộc nhóm này, với ba bản M / L / H tương ứng ba tình
huống nước: nước máy thông thường, hộ dùng nhiều nước, và nước cứng.</p>

<h3>3. Máy điện giải ion kiềm</h3>
<p>Lọc sạch rồi điện phân để tách thành nước kiềm (uống) và nước axit (dùng ngoài). Nước ra có pH cao,
giàu hydro hoà tan. Nhóm này có giá cao hơn hai nhóm trên và <strong>rất nhạy với chất lượng nước đầu
vào</strong>: clo dư, cặn canxi làm giảm hiệu suất và tuổi thọ tấm điện cực. Vì vậy máy điện giải gần như
luôn cần một <a href="bo-tien-xu-ly-bwt-barrier-ion-m.html">bộ tiền xử lý</a> đi kèm.</p>
<p>Đơn vị chuyên sâu về máy điện giải, có showroom trải nghiệm và đội kỹ thuật riêng là
<a %(TGDG)s>Thế Giới Điện Giải</a> — nếu bạn nghiêng về hướng này, nên tới xem máy chạy thực tế trước khi quyết.</p>

<h2>Bảng so sánh nhanh</h2>
<div class="tblwrap">
<table class="spec">
  <thead><tr><th scope="col">Tiêu chí</th><td><strong>RO</strong></td><td><strong>Giữ khoáng</strong></td><td><strong>Điện giải</strong></td></tr></thead>
  <tbody>
    <tr><th scope="row">Cần điện</th><td>Có</td><td>Không</td><td>Có</td></tr>
    <tr><th scope="row">Nước thải</th><td>Có</td><td>Không</td><td>Có (nước axit)</td></tr>
    <tr><th scope="row">Khoáng trong nước ra</th><td>Gần như không</td><td>Giữ lại</td><td>Giữ lại, pH kiềm</td></tr>
    <tr><th scope="row">Yêu cầu nước đầu vào</th><td>Chấp nhận nước kém</td><td>Cần tương đối sạch</td><td>Cần sạch, ổn định</td></tr>
    <tr><th scope="row">Chi phí đầu tư</th><td>Thấp – trung bình</td><td>Trung bình</td><td>Cao</td></tr>
    <tr><th scope="row">Chi phí vận hành</th><td>Điện + nước thải + lõi</td><td>Lõi</td><td>Điện + lõi + tiền xử lý</td></tr>
  </tbody>
</table>
</div>

<h2>Gợi ý chọn theo hoàn cảnh</h2>
<ul>
  <li><strong>Nước máy đô thị, gia đình 3–5 người, muốn gọn và ít tốn kém khi vận hành</strong> →
      máy giữ khoáng lắp âm tủ. Bản <a href="may-loc-nuoc-bwt-barrier-m.html">BWT Barrier M</a> là điểm
      bắt đầu hợp lý; hộ đông người cân nhắc bản L với lõi 10.000 lít.</li>
  <li><strong>Vùng nước cứng, ấm đun đóng cặn</strong> → bản <a href="may-loc-nuoc-bwt-barrier-h.html">BWT Barrier H</a>
      có lõi làm mềm, hoặc RO nếu nước đầu vào còn kém hơn thế.</li>
  <li><strong>Nước giếng khoan chưa xử lý</strong> → lắp lọc đầu nguồn trước, rồi mới chọn máy uống.
      Đơn vị làm lọc tổng: <a %(TGLT)s>Thế Giới Lọc Tổng</a>.</li>
  <li><strong>Quan tâm nước kiềm, sẵn ngân sách</strong> → máy điện giải + bộ tiền xử lý, tư vấn tại
      <a %(TGDG)s>Thế Giới Điện Giải</a>.</li>
</ul>

<h2>Ba điều nên hỏi trước khi mua</h2>
<ol>
  <li><strong>Nước nhà tôi là nước gì?</strong> Nếu chưa biết, xét nghiệm hoặc nhờ đo nhanh trước.</li>
  <li><strong>Lõi thay bao nhiêu tiền, bao lâu thay một lần, mua ở đâu?</strong> Chi phí lõi qua 3–5 năm
      thường lớn hơn giá máy.</li>
  <li><strong>Bảo hành ở đâu, ai tới nhà?</strong> Máy lọc là thiết bị lắp cố định — đơn vị bảo hành có
      kỹ thuật viên tận nơi quan trọng hơn nhiều so với máy để bàn.</li>
</ol>
<p>Với dòng BWT Barrier, trung tâm chúng tôi tiếp nhận bảo hành, cung cấp lõi và hỗ trợ kỹ thuật tận nơi —
xem <a href="lien-he.html#bao-hanh">chính sách bảo hành</a> hoặc gọi hotline CSKH.</p>
""",
    },

    # ================================================================== 4
    {
        "slug": "bao-lau-nen-thay-loi-may-loc-nuoc",
        "title": "Bao lâu nên thay lõi máy lọc nước? 5 dấu hiệu lõi đã hết hạn",
        "seo_title": "Bao lâu nên thay lõi máy lọc nước? 5 dấu hiệu lõi hết hạn",
        "desc": "Lõi lọc hết hạn không báo bằng mắt thường. Chu kỳ thay lõi theo từng loại, 5 dấu hiệu "
                "cần thay sớm, và vì sao nước đầu vào quyết định tuổi thọ lõi hơn số tháng.",
        "topic": "may-loc-nuoc",
        "topic_label": "Máy lọc nước",
        "date": "2026-09-11",
        "cover": "assets/img/bai-thay-loi-loc.webp",
        "cover_alt": "Bộ ba lõi lọc của máy lọc nước lắp âm tủ",
        "excerpt": "Lõi lọc là bộ phận hao mòn theo từng lít nước đi qua. Dùng quá hạn, "
                   "nước ra trông vẫn trong nhưng chất lượng đã không còn như thiết kế.",
        "keys": "thay loi may loc nuoc bao lau dau hieu loi het han chu ky thay loi tuoi tho loi bo dem water meter",
        "body": """
<p>Máy lọc nước không có bộ phận nào "hỏng" khi lõi hết hạn — nước vẫn chảy, vẫn trong. Đó chính là
điểm nguy hiểm: lõi bão hoà không giữ được thêm tạp chất nữa, thậm chí có thể nhả ngược lại những gì đã
tích tụ, mà người dùng không nhận ra bằng mắt. Vì vậy thay lõi đúng lúc quan trọng hơn chọn máy đắt tiền.</p>

<h2>Chu kỳ thay lõi theo từng loại</h2>
<p>Mỗi lõi trong máy có tuổi thọ khác nhau. Con số dưới đây là khuyến nghị phổ biến với <strong>nước máy
đô thị</strong>; nước giếng hoặc nước nhiều cặn sẽ rút ngắn đáng kể.</p>
<div class="tblwrap">
<table class="spec">
  <thead><tr><th scope="col">Loại lõi</th><td><strong>Nhiệm vụ</strong></td><td><strong>Chu kỳ tham khảo</strong></td></tr></thead>
  <tbody>
    <tr><th scope="row">Lõi cặn thô (PP / sediment)</th><td>Giữ cát, rỉ sét, cặn lơ lửng</td><td>3–6 tháng</td></tr>
    <tr><th scope="row">Lõi than hoạt tính</th><td>Khử clo, mùi, màu</td><td>6–12 tháng</td></tr>
    <tr><th scope="row">Lõi trao đổi ion / làm mềm</th><td>Giảm độ cứng, giữ khoáng có lợi</td><td>8.000–10.000 lít (~12 tháng)</td></tr>
    <tr><th scope="row">Màng RO</th><td>Lọc tinh ở cấp phân tử</td><td>24–36 tháng</td></tr>
    <tr><th scope="row">Lõi bù khoáng / hậu lọc</th><td>Hoàn thiện vị nước</td><td>12 tháng</td></tr>
  </tbody>
</table>
</div>
<p>Với máy lọc kiểu cụm lõi đúc nguyên khối như <a href="san-pham.html">BWT Barrier</a>, cả bộ ba lõi được
thay cùng lúc theo định mức <strong>8.000 lít</strong> (bản M, H) hoặc <strong>10.000 lít</strong> (bản L) —
tương đương khoảng 12 tháng cho hộ 4 người dùng nước đều đặn.</p>

<h2>Số tháng hay số lít?</h2>
<p>Nhà sản xuất đưa ra hai con số: <em>số tháng</em> để dễ nhớ, và <em>số lít</em> là con số thật.
Lõi hao mòn theo lượng nước đi qua, không theo lịch. Hộ độc thân có thể dùng 18 tháng chưa hết định mức;
quán cà phê nhỏ có thể cạn lõi sau 4 tháng. Hai cách xử lý:</p>
<ul>
  <li><strong>Ước lượng</strong>: gia đình 4 người dùng khoảng 20–25 lít nước uống và nấu ăn mỗi ngày → lõi
      8.000 lít đủ cho 11–13 tháng.</li>
  <li><strong>Đo thật</strong>: lắp <a href="may-loc-nuoc-bwt-barrier-m-co-bo-dem.html">bộ đếm Water Meter</a>
      trên đường nước vào máy — thiết bị đếm lít thực tế và báo phần trăm lõi còn lại, bỏ hẳn việc phải
      nhớ ngày.</li>
</ul>

<h2>5 dấu hiệu lõi đã hết hạn dù chưa tới lịch</h2>
<ol>
  <li><strong>Lưu lượng giảm rõ</strong>: rót đầy ly lâu hơn trước, lõi thô đang tắc vì cặn.</li>
  <li><strong>Nước có vị hoặc mùi lạ trở lại</strong>: mùi clo, vị tanh — lõi than đã bão hoà.</li>
  <li><strong>Cặn trắng xuất hiện lại</strong> ở ấm đun, đáy ly — lõi làm mềm hết khả năng trao đổi ion.</li>
  <li><strong>Vỏ lõi thô chuyển màu nâu đậm</strong> (với máy có cốc lọc trong): nhìn thấy được, thay ngay.</li>
  <li><strong>Nguồn nước vừa thay đổi</strong>: nhà máy nước súc rửa đường ống, mùa mưa nước đục hơn, hoặc
      vừa chuyển sang dùng giếng — lõi chịu tải đột ngột, nên kiểm tra sớm.</li>
</ol>

<h2>Nước đầu vào quyết định tuổi thọ lõi</h2>
<p>Đây là điều ít người để ý: cùng một máy, cùng một lõi, nhưng nhà dùng nước giếng chưa xử lý có thể phải
thay lõi thô nhanh gấp ba lần nhà dùng nước máy. Nếu bạn thấy mình <strong>thay lõi liên tục</strong>, vấn
đề không nằm ở lõi mà ở nguồn nước — lúc này cần xem tới <a href="loc-nuoc-dau-nguon-la-gi.html">lọc đầu
nguồn</a>. Hệ thống lọc tổng phía trước giữ lại phèn, cặn, giảm độ cứng, và máy lọc uống phía sau mới chạy
đúng định mức thiết kế. Đơn vị chuyên lọc đầu nguồn: <a %(TGLT)s>Thế Giới Lọc Tổng</a>.</p>
<p>Với máy điện giải ion kiềm, lõi lọc và bộ tiền xử lý còn có thêm nhiệm vụ bảo vệ tấm điện cực — thay
muộn không chỉ ảnh hưởng nước mà còn ảnh hưởng tuổi thọ máy. Lịch thay lõi và lõi chính hãng cho dòng
máy này, bạn tham khảo tại <a %(TGDG)s>Thế Giới Điện Giải</a>.</p>

<h2>Thay lõi ở đâu, ai thay?</h2>
<p>Với máy có cơ chế thay nhanh (như One Touch trên BWT Barrier), bạn có thể tự thay tại nhà trong vài phút
mà không cần dụng cụ. Nếu không chắc, hoặc muốn kỹ thuật viên kiểm tra luôn đường nước và áp lực, trung tâm
bảo hành hỗ trợ tận nơi. Chúng tôi cũng <strong>nhắc lịch thay lõi</strong> cho khách hàng đã đăng ký —
gọi <a href="lien-he.html">hotline CSKH</a> để đăng ký.</p>
""",
    },
]

# thay {TGLT}/{TGDG} trong body
for _a in ARTICLES:
    _a["body"] = _a["body"] % {"TGLT": TGLT, "TGDG": TGDG}
    _a["excerpt"] = " ".join(_a["excerpt"].split())
