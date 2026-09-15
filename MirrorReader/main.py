"""MirrorReader 阶段 1：读取文本并连续翻页。"""

from pathlib import Path
import sys


DEFAULT_ARTICLE = Path(__file__).parent / "sample_data" / "sample_article.txt"


def load_paragraphs(file_path: Path) -> list[str]:
    """读取 UTF-8 文本，并按空行切分出非空段落。"""
    text = file_path.read_text(encoding="utf-8")
    normalized_text = text.replace("\r\n", "\n")
    return [part.strip() for part in normalized_text.split("\n\n") if part.strip()]


def show_paragraph(paragraphs: list[str], position: int) -> None:
    """显示当前位置和对应段落。"""
    total = len(paragraphs)
    print(f"\n--- 第 {position + 1}/{total} 段 ---")
    print(paragraphs[position])


def show_help() -> None:
    """显示阶段 1 支持的命令。"""
    print("\n命令：n 下一段 | p 上一段 | s 查看进度 | help 帮助 | exit 退出")


def read_article(paragraphs: list[str]) -> None:
    """运行阅读命令循环。"""
    position = 0
    show_paragraph(paragraphs, position)
    show_help()

    while True:
        command = input("\n> ").strip().lower()

        if command == "n":
            if position < len(paragraphs) - 1:
                position += 1
                show_paragraph(paragraphs, position)
            else:
                print("已经是最后一段了。")
        elif command == "p":
            if position > 0:
                position -= 1
                show_paragraph(paragraphs, position)
            else:
                print("已经是第一段了。")
        elif command == "s":
            print(f"当前位于第 {position + 1} 段，共 {len(paragraphs)} 段。")
        elif command == "help":
            show_help()
        elif command == "exit":
            print("本次阅读结束。阶段 2 将加入进度保存功能。")
            break
        elif command == "":
            print("请输入命令；输入 help 可以查看帮助。")
        else:
            print("未知命令；输入 help 可以查看帮助。")


def main() -> None:
    """选择文章、处理常见文件错误并开始阅读。"""
    article_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_ARTICLE

    try:
        paragraphs = load_paragraphs(article_path)
    except FileNotFoundError:
        print(f"找不到文章：{article_path}")
        return
    except UnicodeDecodeError:
        print(f"无法按 UTF-8 读取文章：{article_path}")
        return

    if not paragraphs:
        print(f"文章没有可阅读的段落：{article_path}")
        return

    print(f"已读取：{article_path.name}")
    print(f"共找到 {len(paragraphs)} 个段落。")
    read_article(paragraphs)


if __name__ == "__main__":
    main()

