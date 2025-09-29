from LLM.openai.main_openai import main_openai
from LLM.dify.main_dify import main_dify

def main(openai_or_dify, mode, txt, window_size, overlap_size, url_input, prompt_single = None,
         prompt_two_or_more = None, api_key_input = None, model_input = None, api_key_input_1= None, api_key_input_2= None):
    if openai_or_dify == "openai":
        res = main_openai(mode, txt, window_size, overlap_size, prompt_single, prompt_two_or_more, model_input, url_input, api_key_input)

    elif openai_or_dify == "dify":
        res = main_dify(mode, txt, window_size, overlap_size, api_key_input_1, api_key_input_2, url_input)

    else:
        raise ValueError(f"mode 必须是以下值之一: openai, dify")

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
    result = main("openai", "split", "testtxt/testtxt_compare1.txt", window_size = window_size,
                  overlap_size = overlap_size, prompt_single = prompt_single, prompt_two_or_more = prompt_two_or_more,
                  api_key_input = api_key, url_input = url, model_input = model)
    print(result)
