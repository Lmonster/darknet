import os

imgs = [img for img in os.listdir('images') if not img.startswith('.')]
workding_dir = os.getcwd()
img_dir = os.path.join(workding_dir, 'images')

with open(os.path.join(workding_dir, 'train.txt'), 'w') as f:
    for img in imgs:
        f.write(os.path.join(img_dir, img) + '\n')
