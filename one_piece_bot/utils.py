def get_latest_chaper_url():
  # Get the latest chapter from the chapters_list.txt file
  chapter_url_prefix = 'one-piece-chapter-'
  with open('../one_piece_bot/chapters_list.txt', 'r') as f:
    current_chapter = f.readline()
  chapter_url = f'{chapter_url_prefix}{current_chapter.strip()}'
  return current_chapter, chapter_url


def update_chapter(new_chapter):
  with open('../one_piece_bot/chapters_list.txt', 'w') as f:
    f.write(str(new_chapter))
