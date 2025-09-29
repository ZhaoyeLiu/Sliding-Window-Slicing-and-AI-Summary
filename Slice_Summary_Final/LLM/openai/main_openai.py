from Slice.sliding_window_split_text_package import sliding_window_split_text
from LLM.openai.summary_using_ai import slice_summary_iteration, slice_summary_split

def main_openai(mode, txt, window_size, overlap_size, prompt_single, prompt_two_or_more, model_input, url_input, api_key_input = None):
    if mode == "interation":
        slice = sliding_window_split_text(txt, window_size, overlap_size)
        print(slice)
        res = slice_summary_iteration(slice, prompt_single, prompt_two_or_more, api_key_input, url_input, model_input)

    elif mode == "split":
        slice = sliding_window_split_text(txt, window_size, overlap_size)
        print(slice)
        res = slice_summary_split(slice, prompt_single, prompt_two_or_more, api_key_input, url_input, model_input)

    else:
        raise ValueError(f"mode 必须是以下值之一: interation, split")

    return res


if __name__ == "__main__":

    window_size = 8000
    overlap_size = 800

    prompt_single = '''
    你是一个阅读政府通知文件的助手，你需要阅读正文，提取通知内的关键内容，包含以下内容形成一段话，不要超过150字：
    1、通知目的：要做什么事，或是要开展什么工作。
    2、发文主体和时间：谁发的文，落款的时间。
    3、重要内容
    '''
    prompt_two_or_more = '''
    你是一个阅读政府通知文件的助手，你需要阅读正文，提取通知内的关键内容，包含以下内容形成一段话，不要超过150字：
    1、通知目的：要做什么事，或是要开展什么工作。
    2、发文主体和时间：谁发的文，落款的时间。
    3、重要内容
    '''

    api_key = "not empty"
    url = "http://citybrain.hisense.com/Qwen3-32B/v1"
    model = "Qwen3-32B"

    print("Test:")
    result = main_openai("split", "testtxt/testtxt_compare1.txt", window_size, overlap_size, prompt_single, prompt_two_or_more, api_key, url, model)
    print(result)
