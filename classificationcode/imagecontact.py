import cv2
import os

# 定义要拼接的两张图像的路径和文件名
img1_path = r'C:\Users\LENOVO\Desktop\results(1).png'
img2_path = r'C:\Users\LENOVO\Desktop\results(2).png'

# 读入两张图像
img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

# 将两张图像水平拼接在一起
h_concat = cv2.hconcat([img1, img2])

# 定义拼接后图像的文件名和保存路径
save_path = os.path.dirname(img1_path)  # 获取原始图像所在的文件夹路径
save_name = 'h_concat.jpg'  # 定义拼接后图像的文件名
save_file = os.path.join(save_path, save_name)  # 定义拼接后图像的保存路径

# 保存拼接后的图像
cv2.imwrite(save_file, h_concat)