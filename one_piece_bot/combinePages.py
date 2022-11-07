from PIL import Image
import variables, os

def combine_all_pages():
  combinedFile = variables.CHAPTER
  chaptersDir = './one_piece_chapters'
  chapters = os.listdir(chaptersDir)
  chapters.sort(key=lambda s: sum(map(ord, s)))
  chaptersList = [f'{chaptersDir}/{chapter}' for chapter in chapters]

  # print(chapters)
  print(chaptersList)
  images = [Image.open(img) for img in chaptersList]
  widths, heights = zip(*(i.size for i in images))
  total_height = sum(heights)
  max_width = max(widths)

  whiteColor = (256, 256, 256)
  combinedImage = Image.new('RGB', (max_width, total_height), whiteColor)
  y_offset = 0
  x_offset = 0

  for img in images:
    x_offset = (max_width - img.width)/2
    combinedImage.paste(img, (int(x_offset), y_offset))
    y_offset += img.height + 5

  combinedImage.save(f'{combinedFile}.jpg')