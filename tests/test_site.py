import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.attrs = {}
        self.text = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.attrs.setdefault(tag, []).append(dict(attrs))

    def handle_data(self, data):
        self.text.append(data)

    @property
    def body_text(self):
        return " ".join(" ".join(self.text).split())


def parse(path):
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


class StaticSiteTests(unittest.TestCase):
    def test_required_static_files_are_present(self):
        for path in ("app-ads.txt", "googlea2b8e85e238fd56b.html", "styles.css", "site.js"):
            self.assertTrue((ROOT / path).is_file(), path)

    def test_detail_routes_use_directory_indexes(self):
        for route in ("terretatrad", "mdnote"):
            self.assertTrue((ROOT / route / "index.html").is_file(), route)

    def test_home_has_editorial_content_and_route_links(self):
        path = ROOT / "index.html"
        parser = parse(path)
        html = path.read_text(encoding="utf-8")
        self.assertIn('href="styles.css"', html)
        self.assertIn('src="site.js"', html)
        self.assertIn("<title>Erik Monsonís Pérez · Desarrollo de aplicaciones</title>", html)
        self.assertIn(
            '<meta name="description" content="Portfolio de Erik Monsonís Pérez, desarrollador de aplicaciones especializado en Android.">',
            html,
        )
        self.assertIn("Desarrollador de aplicaciones especializado en Android", parser.body_text)
        self.assertIn("Enfoque y arquitectura", parser.body_text)
        self.assertIn('href="/terretatrad/"', html)
        self.assertIn('href="/mdnote/"', html)
        self.assertIn(
            "https://www.linkedin.com/in/erikmonsonisperez/",
            [link.get("href") for link in parser.attrs["a"]],
        )
        self.assertIn("<main", html)
        self.assertNotIn("<style", html.lower())

    def test_home_app_descriptions_are_short_and_factual(self):
        text = parse(ROOT / "index.html").body_text
        self.assertIn("Traduce entre castellano y valenciano.", text)
        self.assertIn("Escribe y edita notas en Markdown.", text)

    def test_home_project_links_have_local_icons_and_only_two_apps(self):
        parser = parse(ROOT / "index.html")
        icons = [img["src"] for img in parser.attrs.get("img", [])]
        for name in ("terretatrad", "mdnote"):
            self.assertIn(f"/assets/{name}.webp", icons)
        self.assertNotIn("ML Node", parser.body_text)
        badges = [
            link for link in parser.attrs.get("a", [])
            if "store-badge" in link.get("class", "")
        ]
        self.assertGreaterEqual(len(badges), 3)
        self.assertIn("svg", parser.tags)

    def test_each_page_uses_the_studio_favicon(self):
        for route in ("", "terretatrad", "mdnote"):
            html = (ROOT / route / "index.html").read_text(encoding="utf-8")
            parser = parse(ROOT / route / "index.html")
            links = parser.attrs["link"]
            self.assertIn({"rel": "icon", "type": "image/svg+xml", "href": "/assets/monograma.svg"}, links)
            self.assertIn("/assets/monograma.svg", [img.get("src") for img in parser.attrs.get("img", [])])
            self.assertNotIn("<span>Erik Monsonís</span>", html)
        png = (ROOT / "assets/developer-icon.png").read_bytes()
        self.assertEqual(png[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(tuple(int.from_bytes(png[i:i + 4], "big") for i in (16, 20)), (512, 512))
        self.assertEqual(png[24:26], bytes([8, 6]))  # 8 bits per RGBA channel

    def test_developer_header_matches_google_play_specs(self):
        header = (ROOT / "assets/developer-header.png").read_bytes()
        self.assertEqual(header[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(tuple(int.from_bytes(header[i:i + 4], "big") for i in (16, 20)), (4096, 2304))
        self.assertEqual(header[24:26], bytes([8, 2]))  # 24-bit RGB without alpha
        self.assertLessEqual(len(header), 1_000_000)

    def test_detail_pages_have_titles_descriptions_badges_and_features(self):
        expected = {
            "terretatrad": (
                "TerretaTrad",
                "Traduce entre castellano y valenciano, guarda traducciones y compártelas.",
                "com.erikmp.terretatrad",
                "TerretaTrad · Erik Monsonís Pérez",
                "Qué es TerretaTrad",
            ),
            "mdnote": (
                "mdNote",
                "Escribe y edita notas en Markdown con vista previa.",
                "com.erikmp.mdnote",
                "mdNote · Erik Monsonís Pérez",
                "Qué es mdNote",
            ),
        }
        for route, (name, description, package_name, title, overview_heading) in expected.items():
            path = ROOT / route / "index.html"
            parser = parse(path)
            html = path.read_text(encoding="utf-8")
            self.assertIn('href="../styles.css"', html)
            self.assertIn('href="../"', html)
            self.assertIn(name, parser.body_text)
            self.assertIn(description, parser.body_text)
            self.assertIn(overview_heading, parser.body_text)
            self.assertIn("Funcionalidades principales", parser.body_text)
            self.assertIn(f"<title>{title}</title>", html)
            self.assertIn(f'<meta name="description" content="{description}">', html)
            self.assertIn("Disponible en Google Play", parser.body_text)
            self.assertIn("iOS En desarrollo", parser.body_text)
            self.assertIn("Próximamente", parser.body_text)
            self.assertNotIn("ML Node", parser.body_text)
            links = [link.get("href") for link in parser.attrs["a"]]
            self.assertIn(f"https://play.google.com/store/apps/details?id={package_name}", links)
            play_badges = [
                link for link in parser.attrs["a"]
                if "store-badge--play" in link.get("class", "")
            ]
            self.assertEqual(len(play_badges), 1)
            self.assertIn("svg", parser.tags)
            if route == "terretatrad":
                self.assertIn("https://terretatrad.com/", links)
            self.assertIn(package_name, html)
            self.assertIn("<main", html)
            self.assertNotIn("<style", html.lower())

    def test_shared_styles_are_swiss_technical_and_accessible(self):
        css = (ROOT / "styles.css").read_text(encoding="utf-8")
        self.assertIn("#eceff3", css)
        self.assertIn("#111418", css)
        self.assertIn("#d94f1e", css)
        self.assertIn(":focus-visible", css)
        self.assertIn("prefers-reduced-motion", css)
        self.assertNotIn("radial-gradient", css)
        self.assertNotIn("backdrop-filter", css)
        self.assertNotIn("box-shadow", css)

    def test_local_links_target_existing_files(self):
        for path in [ROOT / "index.html", ROOT / "terretatrad/index.html", ROOT / "mdnote/index.html"]:
            parser = parse(path)
            urls = [attrs.get(attr) for tag, attr in (("a", "href"), ("link", "href"), ("img", "src"), ("script", "src"))
                    for attrs in parser.attrs.get(tag, [])]
            for url in urls:
                if not url or url.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                local = url.split("#", 1)[0]
                target = ROOT / local.lstrip("/") if local.startswith("/") else path.parent / local
                if target.is_dir():
                    target /= "index.html"
                self.assertTrue(target.is_file(), f"Missing local URL {url}")


if __name__ == "__main__":
    unittest.main()
