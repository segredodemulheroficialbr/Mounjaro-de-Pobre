from PIL import Image, ImageDraw, ImageFont
import os

out_dir = os.path.join(os.path.dirname(__file__), '..', 'assets', 'icons')
os.makedirs(out_dir, exist_ok=True)

# base color and simple emblem
bg = (40, 167, 69)  # green
fg = (255,255,255)

sizes = [16, 32, 48, 180]
for s in sizes:
    img = Image.new('RGBA', (s, s), bg)
    draw = ImageDraw.Draw(img)
    # draw a simple rounded square inner
    pad = max(1, s//6)
    draw.rounded_rectangle([pad, pad, s-pad-1, s-pad-1], radius= max(1, s//8), fill=fg)
    # draw a small circle to make it look different
    r = max(1, s//8)
    cx = s - pad - r - 1
    cy = pad + r + 1
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=bg)
    path = os.path.join(out_dir, 'apple-touch-icon.png' if s==180 else f'favicon-{s}x{s}.png')
    img.save(path)
    print('Wrote', path)

# create ICO containing 16,32,48
ico_sizes = [(16,16),(32,32),(48,48)]
icons = []
for (w,h) in ico_sizes:
    src = os.path.join(out_dir, f'favicon-{w}x{h}.png')
    icons.append(Image.open(src))
ico_path = os.path.join(out_dir, 'favicon.ico')
# save first image and provide sizes for multi-icon
icons[0].save(ico_path, sizes=[(16,16),(32,32),(48,48)])
print('Wrote', ico_path)
