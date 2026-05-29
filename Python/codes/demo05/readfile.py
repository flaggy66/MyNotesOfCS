# 文本文件读操作
from pathlib import Path

file_path = Path("poem.txt")
contents = file_path.read_text(encoding="utf-8")
# 读取全部内容
print(contents)
# 逐行获取内容
i = 1
for line in contents.splitlines():
    print(f"第{i}行内容：", line)
    i += 1
