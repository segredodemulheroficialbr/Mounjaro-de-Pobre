from PIL import Image
import sys

# Source image path (update if desired)
src = r"emagrecasemdieta.site/images/logo1.png"
# Output paths
out_root = r"favicon.ico"
out_folder = r"favicons/favicon.ico"

sizes = [(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)]

try:
    img = Image.open(src)
    # Convert to RGBA for transparency
    img = img.convert('RGBA')
    # Pillow can save .ico with multiple sizes by passing the sizes tuple
    img.save(out_root, format='ICO', sizes=sizes)
    img.save(out_folder, format='ICO', sizes=sizes)
    print('favicon.ico created at', out_root, 'and', out_folder)
except Exception as e:
    print('ERROR:', e)
    sys.exit(1)
