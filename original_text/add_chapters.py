# usage: python add_chapters.py --arg1 Exodus --arg2 40 --arg3 Old_Testament

import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--arg1')
  parser.add_argument('--arg2')
  parser.add_argument('--arg3')
  args = parser.parse_args()

  book_name = args.arg1
  max_chapters = int(args.arg2)
  testament = args.arg3

  for ch in range(1, max_chapters + 1):
    front_matter = f"""---
testament: {testament.replace("_", " ")}
testament_link: {testament}
chapter_number: {ch}
chapter_order_number: {str(ch).rjust(2, "0")}
total_chapters: {max_chapters}
book_short_name: {book_name.replace("_", " ")}
book_link_name: {book_name}
layout: chapter
---
"""
    filename = str(ch).rjust(2, "0") + ".markdown"
    with open(filename, 'w', encoding='utf-8') as f:
      f.write(front_matter)





