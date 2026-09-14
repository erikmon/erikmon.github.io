import re
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
        for path in ("app-ads.txt", "googlea2b8e85e238fd56b.html", "styles.css"):
            self.assertTrue((ROOT / path).is_file(), path)

    def test_detail_routes_use_directory_indexes(self):
        for route in ("terretatrad", "mdnote"):
            self.assertTrue((ROOT / route / "index.html").is_file(), route)

    def test_home_has_editorial_content_and_route_links(self):
        path = ROOT / "index.html"
        parser = parse(path)
        html = path.read_text(encoding="utf-8")
        self.assertIn('href="styles.css"', html)
        self.assertIn("<title>Erik Monsonís Pérez · Desarrollo aplicaciones Android</title>", html)
        self.assertIn(
            '<meta name="description" content="Portfolio de Erik Monsonís Pérez: desarrollo de aplicaciones Android.">',
            html,
        )
        self.assertIn("Desarrollo aplicaciones Android", parser.body_text)
        self.assertIn('href="/terretatrad/"', html)
        self.assertIn('href="/mdnote/"', html)
        self.assertIn("LinkedIn", parser.body_text)
        self.assertIn("<main", html)
        self.assertNotIn("<script", html.lower())
        self.assertNotIn("<style", html.lower())

    def test_home_app_descriptions_are_short_and_factual(self):
        text = parse(ROOT / "index.html").body_text
        self.assertIn("Traducción valenciana.", text)
        self.assertIn("Notas Markdown.", text)

    def test_detail_pages_have_titles_descriptions_and_play_links(self):
        expected = {
            "terretatrad": (
                "TerretaTrad",
                "Traducción valenciana.",
                "com.erikmp.terretatrad",
                "TerretaTrad · Erik Monsonís Pérez",
            ),
            "mdnote": (
                "mdNote",
                "Notas Markdown.",
                "com.erikmp.mdnote",
                "mdNote · Erik Monsonís Pérez",
            ),
        }
        for route, (name, description, package_name, title) in expected.items():
            path = ROOT / route / "index.html"
            parser = parse(path)
            html = path.read_text(encoding="utf-8")
            self.assertIn('href="../styles.css"', html)
            self.assertIn('href="../"', html)
            self.assertIn(name, parser.body_text)
            self.assertIn(description, parser.body_text)
            self.assertIn(f"<title>{title}</title>", html)
            self.assertIn(f'<meta name="description" content="{description}">', html)
            self.assertIn("Google Play", parser.body_text)
            self.assertIn(package_name, html)
            self.assertIn("<main", html)
            self.assertNotIn("<script", html.lower())
            self.assertNotIn("<style", html.lower())

    def test_shared_styles_are_light_editorial_and_accessible(self):
        css = (ROOT / "styles.css").read_text(encoding="utf-8")
        self.assertIn("#f7f4ef", css)
        self.assertIn("#24211e", css)
        self.assertIn("#a24d30", css)
        self.assertIn(":focus-visible", css)
        self.assertIn("max-width: 760px", css)
        self.assertNotIn("radial-gradient", css)
        self.assertNotIn("backdrop-filter", css)
        self.assertNotIn("box-shadow", css)

    def test_local_links_target_existing_files(self):
        for path in [ROOT / "index.html", ROOT / "terretatrad/index.html", ROOT / "mdnote/index.html"]:
            html = path.read_text(encoding="utf-8")
            for href in re.findall(r'href=["\']([^"\']+)["\']', html):
                if href.startswith(("http://", "https://", "mailto:", "#", "/")):
                    continue
                target = (path.parent / Path(href.split("#", 1)[0])).resolve()
                self.assertTrue(target.exists(), f"Missing local href {href}")


if __name__ == "__main__":
    unittest.main()
