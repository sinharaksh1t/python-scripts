from PIL import Image
from one_piece_bot import utils
# import utils
import os


def combine_all_pages():
  _, chapter_url = utils.get_latest_chaper_url()
  combinedFile = chapter_url
  chapters_dir = f'./one_piece_chapters/{chapter_url}'
  chapters = os.listdir(chapters_dir)
  chapters.sort(key=lambda s: sum(map(ord, s)))
  chapters_list = [f'{chapters_dir}/{chapter}' for chapter in chapters]

  images = [Image.open(img) for img in chapters_list]
  widths, heights = zip(*(i.size for i in images))
  total_height = sum(heights)
  max_width = max(widths)

  whiteColor = (256, 256, 256)
  combinedImage = Image.new('RGB', (max_width, total_height), whiteColor)
  y_offset = 0
  x_offset = 0

  for img in images:
    x_offset = (max_width - img.width) / 2
    combinedImage.paste(img, (int(x_offset), y_offset))
    y_offset += img.height + 5

  combinedImage.save(f'{chapters_dir}/{combinedFile}.jpg')


# combine_all_pages()
