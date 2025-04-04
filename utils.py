import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def display_image(image=None, images=None, folder_path=None):
    """
    Hiển thị ảnh hoặc nhiều ảnh từ đối tượng đã load, đường dẫn, hoặc folder.

    Parameters:
        - image: Một ảnh đơn (PIL.Image hoặc numpy.ndarray hoặc đường dẫn file).
        - images: Danh sách nhiều ảnh (PIL.Image, numpy.ndarray, hoặc đường dẫn file).
        - folder_path: Đường dẫn đến thư mục chứa ảnh.

    Raises:
        - ValueError: Nếu input không hợp lệ hoặc không tìm thấy ảnh.
    """
    
    all_images = []  # Danh sách chứa ảnh cần hiển thị

    # 1. Nếu truyền vào một ảnh đơn
    if image is not None:
        if isinstance(image, (Image.Image, np.ndarray)):  # Nếu là ảnh đã load
            all_images.append(image)
        elif isinstance(image, str) and os.path.isfile(image):  # Nếu là đường dẫn file
            all_images.append(Image.open(image))
        else:
            raise ValueError("Lỗi: 'image' phải là ảnh đã load hoặc đường dẫn file hợp lệ.")

    # 2. Nếu truyền vào danh sách nhiều ảnh
    if images is not None:
        if isinstance(images, list):
            for img in images:
                if isinstance(img, (Image.Image, np.ndarray)):  # Ảnh đã load
                    all_images.append(img)
                elif isinstance(img, str) and os.path.isfile(img):  # Đường dẫn file
                    all_images.append(Image.open(img))
                else:
                    raise ValueError("Lỗi: Một hoặc nhiều phần tử trong 'images' không hợp lệ.")
        else:
            raise ValueError("Lỗi: 'images' phải là một danh sách.")

    # 3. Nếu truyền vào thư mục chứa ảnh
    if folder_path is not None:
        if os.path.isdir(folder_path):
            image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                           if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
            if not image_files:
                raise ValueError("Lỗi: Không tìm thấy ảnh trong thư mục.")
            all_images.extend([Image.open(img) for img in image_files])
        else:
            raise ValueError("Lỗi: 'folder_path' không hợp lệ hoặc không tồn tại.")

    # Kiểm tra nếu không có ảnh nào
    if not all_images:
        raise ValueError("Lỗi: Không có ảnh nào để hiển thị.")

    # Hiển thị ảnh
    num_images = len(all_images)
    cols = 4  # Cố định 4 cột
    for i in range(0, num_images, cols):  # Duyệt qua từng nhóm 4 ảnh
        fig, axes = plt.subplots(1, cols, figsize=(15, 4))
        for j, ax in enumerate(axes):
            img_index = i + j
            if img_index < num_images:
                img = all_images[img_index]
                if isinstance(img, np.ndarray):  # Nếu ảnh là numpy array
                    ax.imshow(img)
                else:  # Nếu là PIL image
                    ax.imshow(img)
                ax.axis('off')
            else:
                ax.axis('off')  # Ẩn các subplot dư thừa
        plt.tight_layout()
        plt.show()
