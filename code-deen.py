import os
import base64
import zlib

def encode_images_to_base64(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            
            with open(image_path, 'rb') as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                compressed_string = zlib.compress(encoded_string.encode('utf-8'))
                output_file = os.path.join(output_folder, f"{filename}.txt")
                with open(output_file, 'wb') as f:
                    f.write(compressed_string)
                print(f"Encoded and compressed content of {filename} saved to {output_file}")
    print(f"Encoded and compressed images saved to {output_folder}")

def decode_base64_to_images(encoded_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(encoded_folder):
        if filename.lower().endswith('.txt'):
            encoded_file_path = os.path.join(encoded_folder, filename)
            with open(encoded_file_path, 'rb') as f:
                compressed_string = f.read()
                encoded_string = zlib.decompress(compressed_string).decode('utf-8')
                image_data = base64.b64decode(encoded_string)
                image_filename = filename.rsplit('.', 1)[0]  # 去掉.txt后缀
                output_path = os.path.join(output_folder, image_filename)
                with open(output_path, 'wb') as image_file:
                    image_file.write(image_data)
    print(f"Decoded images saved to {output_folder}")

if __name__ == "__main__":
    image_folder = "D:\\Adrerie\\Desktop\\sample\\test\\encode"  # 替换为你的图片文件夹路径
    encoded_folder = "D:\\Adrerie\\Desktop\\sample\\test\\encoded"  # 替换为你的Base64编码文件夹路径
    output_folder = "D:\\Adrerie\\Desktop\\sample\\test\\decode"  # 替换为你的输出文件夹路径

    # 编码图片
    encode_images_to_base64(image_folder, encoded_folder)
    
    # 解码图片
    decode_base64_to_images(encoded_folder, output_folder)