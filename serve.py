# -*- coding: utf-8 -*-
"""
Server xem thử tại máy, mô phỏng đúng cách Vercel phục vụ site (cleanUrls).

    python serve.py            # http://127.0.0.1:8000
    python serve.py 3000       # đổi cổng

Khác với `python -m http.server`: server này hiểu đường dẫn không có đuôi
`.html` (ví dụ /san-pham -> san-pham.html) giống cấu hình cleanUrls của Vercel,
và trả về 404.html cho đường dẫn không tồn tại.
"""
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

ROOT = os.path.dirname(os.path.abspath(__file__))

# Console Windows mac dinh la cp1252 -> ep UTF-8 de in duoc tieng Viet
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


class CleanUrlHandler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        full = super().translate_path(path)
        if os.path.isdir(full):
            index = os.path.join(full, "index.html")
            if os.path.isfile(index):
                return index
        if not os.path.exists(full) and not os.path.splitext(full)[1]:
            # /san-pham -> san-pham.html
            if os.path.isfile(full + ".html"):
                return full + ".html"
        return full

    def send_head(self):
        full = self.translate_path(self.path)
        if not os.path.exists(full):
            page404 = os.path.join(ROOT, "404.html")
            if os.path.isfile(page404):
                body = open(page404, "rb").read()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                return __import__("io").BytesIO(body)
        return super().send_head()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    srv = HTTPServer(("127.0.0.1", port), CleanUrlHandler)
    print("Đang chạy tại http://127.0.0.1:%d  (Ctrl+C để dừng)" % port)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng.")


if __name__ == "__main__":
    main()
