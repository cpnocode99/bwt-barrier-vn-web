/* ============================================================
   BWT BARRIER Việt Nam — script chung (thuần JS, không phụ thuộc)
   ============================================================ */
(function () {
  "use strict";

  /* ---------- helpers ---------- */
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /** Bỏ dấu tiếng Việt để tìm kiếm không phân biệt dấu. */
  function fold(s) {
    return String(s || "")
      .normalize("NFD").replace(/[̀-ͯ]/g, "")
      .replace(/đ/g, "d").replace(/Đ/g, "D")
      .toLowerCase().trim();
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  /* ---------- 1. Menu mobile ---------- */
  (function nav() {
    var burger = $(".burger");
    var menu = $("#site-nav");
    if (!burger || !menu) return;

    var backdrop = document.createElement("div");
    backdrop.className = "nav-backdrop";
    document.body.appendChild(backdrop);

    var closeBtn = $(".nav__close", menu);

    function set(open) {
      burger.setAttribute("aria-expanded", open ? "true" : "false");
      menu.setAttribute("data-open", open ? "true" : "false");
      backdrop.setAttribute("data-open", open ? "true" : "false");
      if (open) {
        document.body.classList.add("nav-open");
      } else {
        document.body.classList.remove("nav-open");
      }
    }
    burger.addEventListener("click", function () {
      set(burger.getAttribute("aria-expanded") !== "true");
    });
    if (closeBtn) {
      closeBtn.addEventListener("click", function () { set(false); });
    }
    backdrop.addEventListener("click", function () { set(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") set(false);
    });
    var links = menu.querySelectorAll("a");
    for (var i = 0; i < links.length; i++) {
      links[i].addEventListener("click", function () { set(false); });
    }
    window.addEventListener("resize", function () {
      if (window.innerWidth > 980) set(false);
    });
  })();

  /* ---------- 2. Tìm kiếm ---------- */
  function score(item, q) {
    var hay = fold(item.title + " " + item.desc + " " + item.type + " " + (item.keys || ""));
    var title = fold(item.title);
    var words = q.split(/\s+/).filter(Boolean);
    var s = 0;
    for (var i = 0; i < words.length; i++) {
      if (hay.indexOf(words[i]) === -1) return 0;
      s += 1;
      if (title.indexOf(words[i]) !== -1) s += 2;
    }
    if (title.indexOf(q) === 0) s += 5;
    else if (title.indexOf(q) !== -1) s += 3;
    return s;
  }

  function search(query, limit) {
    var data = window.BWT_INDEX || [];
    var q = fold(query);
    if (!q) return [];
    return data
      .map(function (it) { return { it: it, s: score(it, q) }; })
      .filter(function (r) { return r.s > 0; })
      .sort(function (a, b) { return b.s - a.s; })
      .slice(0, limit || 6)
      .map(function (r) { return r.it; });
  }
  window.bwtSearch = search;

  function highlight(text, query) {
    var fq = fold(query);
    var ft = fold(text);
    var i = ft.indexOf(fq);
    if (i === -1 || !fq) return esc(text);
    return esc(text.slice(0, i)) + "<mark>" + esc(text.slice(i, i + fq.length)) + "</mark>" + esc(text.slice(i + fq.length));
  }
  window.bwtHighlight = highlight;

  (function searchBox() {
    var form = $(".search__form");
    if (!form) return;
    var input = $(".search__input", form);
    var box = $("#search-results");
    if (!input || !box) return;

    var base = document.documentElement.getAttribute("data-base") || "";

    function render(list, q) {
      if (!q) { box.hidden = true; box.innerHTML = ""; return; }
      if (!list.length) {
        box.innerHTML = '<p class="sres-empty">Không tìm thấy kết quả cho “' + esc(q) + '”.<br>Thử: <b>iMaster M</b>, <b>tiền xử lý</b>, <b>nước cứng</b>…</p>';
        box.hidden = false;
        return;
      }
      var html = '<p class="sres-head">' + list.length + " kết quả</p>";
      list.forEach(function (it) {
        html +=
          '<a class="sres-item" href="' + base + it.url + '">' +
          '<img src="' + base + it.img + '" alt="" loading="lazy" width="44" height="44">' +
          "<span>" +
          '<span class="sres-item__t">' + highlight(it.title, q) + "</span><br>" +
          '<span class="sres-item__m">' + esc(it.type) + (it.price ? " · " + esc(it.price) : "") + "</span>" +
          "</span></a>";
      });
      box.innerHTML = html;
      box.hidden = false;
    }

    input.addEventListener("input", function () {
      var q = input.value.trim();
      render(search(q, 6), q);
    });
    input.addEventListener("focus", function () {
      var q = input.value.trim();
      if (q) render(search(q, 6), q);
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var q = input.value.trim();
      if (!q) return;
      window.location.href = base + "/tim-kiem?q=" + encodeURIComponent(q);
    });
    document.addEventListener("click", function (e) {
      if (!form.contains(e.target) && !box.contains(e.target)) box.hidden = true;
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") box.hidden = true;
    });
  })();

  /* ---------- 3. Lọc danh mục sản phẩm ---------- */
  (function filters() {
    var tabs = $$(".tab[data-filter]");
    if (!tabs.length) return;
    var cards = $$("[data-cat]");

    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var f = tab.getAttribute("data-filter");
        tabs.forEach(function (t) { t.setAttribute("aria-selected", String(t === tab)); });
        cards.forEach(function (c) {
          c.hidden = !(f === "all" || c.getAttribute("data-cat") === f);
        });
      });
    });
  })();

  /* ---------- 4. Thư viện ảnh sản phẩm ---------- */
  (function gallery() {
    var main = $("#pd-main-img");
    if (!main) return;
    var thumbs = $$(".pd__thumb");
    thumbs.forEach(function (t) {
      t.addEventListener("click", function () {
        var src = t.getAttribute("data-src");
        if (!src) return;
        main.src = src;
        main.alt = t.getAttribute("data-alt") || main.alt;
        thumbs.forEach(function (x) { x.setAttribute("aria-selected", String(x === t)); });
      });
    });
  })();

  /* ---------- 5. Nút lên đầu trang ---------- */
  (function toTop() {
    var btn = $(".dock__btn--top");
    if (!btn) return;
    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    var tick = function () {
      btn.setAttribute("data-show", window.scrollY > 500 ? "true" : "false");
    };
    window.addEventListener("scroll", tick, { passive: true });
    tick();
  })();

  /* ---------- 6. Trang kết quả tìm kiếm ---------- */
  (function resultsPage() {
    var wrap = $("#search-page-results");
    if (!wrap) return;
    var q = new URLSearchParams(window.location.search).get("q") || "";
    var input = $("#search-page-input");
    if (input) input.value = q;

    var titleEl = $("#search-page-title");
    var list = search(q, 20);

    if (titleEl) {
      titleEl.textContent = q
        ? list.length + " kết quả cho “" + q + "”"
        : "Nhập từ khoá để tìm sản phẩm BWT Barrier";
    }

    if (!q) { wrap.innerHTML = ""; return; }
    if (!list.length) {
      wrap.innerHTML =
        '<p class="sres-empty">Không tìm thấy nội dung phù hợp. Bạn thử các từ khoá: ' +
        '<b>iMaster M</b>, <b>iMaster L</b>, <b>iMaster H</b>, <b>tiền xử lý</b>, <b>nước cứng</b>.</p>';
      return;
    }
    wrap.innerHTML = list.map(function (it) {
      return '' +
        '<article class="pcard">' +
        '<div class="pcard__media"><img src="' + it.img + '" alt="' + esc(it.title) + '" loading="lazy"></div>' +
        '<div class="pcard__body">' +
        '<span class="pcard__tag" style="position:static;display:inline-block;margin-bottom:10px">' + esc(it.type) + "</span>" +
        '<h2 class="pcard__title"><a href="' + it.url + '">' + highlight(it.title, q) + "</a></h2>" +
        "<p style=\"color:var(--muted);font-size:.9rem;margin:0 0 14px\">" + esc(it.desc) + "</p>" +
        '<div class="pcard__foot">' +
        (it.price ? '<span class="price">' + esc(it.price) + "</span>" : "<span></span>") +
        '<a class="btn btn--primary btn--sm" href="' + it.url + '">Xem chi tiết</a>' +
        "</div></div></article>";
    }).join("");
  })();

  /* ---------- 7. Năm hiện tại ở footer ---------- */
  $$("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
