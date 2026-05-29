# 文本文件写操作
from pathlib import Path

file_path = Path("poem01.txt")
contents = "秋浦歌十七首（其十四）\n"
contents += "李白\n"
contents += "炉火照天地，红星乱紫烟。\n"
contents += "赧郎明月夜，歌曲动寒川。"
file_path.write_text(contents, encoding="utf-8")
