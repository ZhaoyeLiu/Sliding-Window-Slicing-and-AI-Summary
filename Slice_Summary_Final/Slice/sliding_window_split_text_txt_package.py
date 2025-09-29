import re
from Slice.sliding_window_split_text_package import sliding_window_split_text

def read_txt_file(file_path):
    #UTF-8
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        raise Exception("文件不是UTF-8编码格式，请将文件转换为UTF-8编码后重试")
    except Exception as e:
        raise Exception(f"读取文件时发生错误: {str(e)}")

def sliding_window_split_text_txt(text_or_file, window_size, overlap_size):
    if isinstance(text_or_file, str) and text_or_file.endswith('.txt'):
        text = read_txt_file(text_or_file)
    else:
        text = text_or_file
    
    return sliding_window_split_text(text, window_size, overlap_size)


if __name__ == "__main__":
    # 测试参数
    window_size = 100
    overlap_size = 30
    
    # 测试文本
    test_text = """这是第一段文本。这是第一段的第二句,1111,11111111111111,111,11111111111,11111111,11111111,111111111,11111111111111！
这是第二段文本，包含一些内容。这是第二段的第二句.iaudo,adjoisad,jxojoadsoahdioajohsdoi,aoer,uxowopsmciwqqq？
这是第三段文本，用于测试滑动窗口切片功能。这是第三段的第二句。
这是第四段文本，继续测试。这是第四段的第二句！
这是最后一段文本。这是最后一段的第二句？"""
    
    # 测试1：直接使用文本
    print("测试1：直接使用文本")
    slices = sliding_window_split_text_txt(test_text, window_size, overlap_size)
    print(f"切片数量: {len(slices)}")
    for i, slice in enumerate(slices, 1):
        print(f"\n切片 {i}:")
        print(slice)
        print(f"长度: {len(slice)}")
    
    # 测试2：使用文件路径
    print("\n测试2：使用文件路径")
    try:
        slices = sliding_window_split_text_txt("testtxt/testtxt1.txt", window_size, overlap_size)
        print(f"切片数量: {len(slices)}")
        for i, slice in enumerate(slices, 1):
            print(f"\n切片 {i}:")
            print(slice)
            print(f"长度: {len(slice)}")
    except Exception as e:
        print(f"文件读取错误: {str(e)}") 