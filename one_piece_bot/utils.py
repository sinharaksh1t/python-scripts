import platform


def get_chapter_file():
  host_platform = platform.platform()
  elysipi_chap_list_file = '/home/elysipi/Desktop/code/python-scripts/one_piece_bot/chapters_list.txt'
  mac_chap_list_file = '/Users/rakssinh/Workspace/python-scripts/ezgmail/one_piece_bot/chapters_list.txt'
  chap_file = elysipi_chap_list_file if 'linux' in str.lower(host_platform) else mac_chap_list_file

  return chap_file


def get_latest_chaper_url():
  chap_file = get_chapter_file()
  # Get the latest chapter from the chapters_list.txt file
  chapter_url_prefix = 'one-piece-chapter-'
  with open(chap_file, 'r') as f:
    current_chapter = f.readline()
  chapter_url = f'{chapter_url_prefix}{current_chapter.strip()}'
  return current_chapter, chapter_url


def update_chapter(new_chapter):
  chap_file = get_chapter_file()
  with open(chap_file, 'w') as f:
    f.write(str(new_chapter))
  print(f'Chapter number updated complete. New chapter: {new_chapter}')
