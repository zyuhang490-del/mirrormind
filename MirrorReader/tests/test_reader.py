"""阶段 1 的基础测试。运行：python -m unittest discover -s tests"""

import tempfile
import unittest
from pathlib import Path

from main import load_paragraphs


class LoadParagraphsTests(unittest.TestCase):
    def test_splits_text_on_blank_lines(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            article = Path(directory) / "article.txt"
            article.write_text("第一段\n\n第二段\n\n第三段", encoding="utf-8")

            self.assertEqual(load_paragraphs(article), ["第一段", "第二段", "第三段"])

    def test_ignores_empty_content(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            article = Path(directory) / "empty.txt"
            article.write_text("\n\n", encoding="utf-8")

            self.assertEqual(load_paragraphs(article), [])


if __name__ == "__main__":
    unittest.main()

