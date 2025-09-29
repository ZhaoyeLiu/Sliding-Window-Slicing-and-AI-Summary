import re

def sliding_window_split_text(text, window_size, overlap_size):

    if(len(text) < window_size):
        return [text]
    
    if(window_size < overlap_size):
        print("Error: 窗口大小小于重叠大小")
        return []
    
    # 按段落分割文本
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    
    result = []
    current_window = ""
    
    #sentence_endings = r'[。！？!?,.，；;]'
    all_punctuations = r'[。！？!?,.，；;]'
    
    def find_overlap_start(text, min_overlap):
        """找到从文本末尾开始，第一个大于等于min_overlap的标点符号位置，并返回标点符号后的位置"""
        parts = re.split(f'({all_punctuations})', text)
        current_length = 0
        for i in range(len(parts)-1, -1, -2):
            if i > 0:  # 确保有标点
                part = parts[i-1] + parts[i]  # 文本+标点
                current_length += len(part)
                if current_length >= min_overlap:
                    # 返回标点符号后的位置
                    return len(text) - current_length + len(parts[i-1]) + 1
        return 0
    
    def split_at_punctuation(text, max_size):
        """在标点符号处分割文本，确保不超过最大长度"""
        parts = re.split(f'({all_punctuations})', text)
        temp_window = ""
        for i in range(0, len(parts)-1, 2):
            if i+1 < len(parts):  # 确保有标点
                part = parts[i] + parts[i+1]  # 文本+标点
                if len(temp_window) + len(part) <= max_size:
                    temp_window += part
                else:
                    break
        return temp_window if temp_window else text[:max_size]
    
    for paragraph in paragraphs:
        # 如果当前窗口加上新段落超过窗口大小
        if len(current_window) + len(paragraph) + 1 > window_size:
            # 保存当前窗口
            if current_window:
                result.append(current_window)
                # 找到重叠起始位置
                overlap_start = find_overlap_start(current_window, overlap_size)
                current_window = current_window[overlap_start:]
            
            # 处理新段落，确保不超过window_size
            remaining_text = paragraph
            while remaining_text:
                if len(current_window) + len(remaining_text) + 1 <= window_size:
                    current_window += "\n" + remaining_text if current_window else remaining_text
                    break
                else:
                    # 在标点符号处分割
                    split_text = split_at_punctuation(remaining_text, window_size - len(current_window) - 1)
                    if current_window:
                        current_window += "\n" + split_text
                    else:
                        current_window = split_text
                    result.append(current_window)
                    # 找到重叠起始位置
                    overlap_start = find_overlap_start(current_window, overlap_size)
                    current_window = current_window[overlap_start:]
                    remaining_text = remaining_text[len(split_text):]
        else:
            # 添加段落到当前窗口
            if current_window:
                current_window += "\n" + paragraph
            else:
                current_window = paragraph
            
            # 检查当前窗口是否超过window_size
            if len(current_window) > window_size:
                split_text = split_at_punctuation(current_window, window_size)
                result.append(split_text)
                # 找到重叠起始位置
                overlap_start = find_overlap_start(split_text, overlap_size)
                current_window = current_window[overlap_start:]
    
    # 添加最后一个窗口
    if current_window:
        result.append(current_window)
    
    return result

if __name__ == "__main__":
    test_text = """这是第一段文本。这是第一段的第二句,1111,11111111111111,111,11111111111,11111111,11111111,111111111,11111111111111！
这是第二段文本，包含一些内容。这是第二段的第二句.iaudo,adjoisad,jxojoadsoahdioajohsdoi,aoer,uxowopsmciwqqq？
这是第三段文本，用于测试滑动窗口切片功能。这是第三段的第二句。
这是第四段文本，继续测试。这是第四段的第二句！
这是最后一段文本。这是最后一段的第二句？"""

    window_size = 50
    overlap_size = 20

    slices = sliding_window_split_text(test_text, window_size, overlap_size)
    print(slices)
    print("\n")

    print("原始文本长度:", len(test_text))
    print("切片数量:", len(slices))
    print("\n切片结果:")
    for i, slice in enumerate(slices, 1):
        print(f"\n切片 {i}:")
        print(slice)
        print(f"长度: {len(slice)}") 