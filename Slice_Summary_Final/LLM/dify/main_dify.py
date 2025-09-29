from LLM.dify.summary_using_ai_dify import slice_summary_iteration_dify, slice_summary_split_dify

def main_dify(mode, txt, window_size, overlap_size, api_key_input_1, api_key_input_2, url_input):
    if mode == "interation":
        res = slice_summary_iteration_dify(txt, window_size, overlap_size, api_key_input_1, api_key_input_2, url_input)

    elif mode == "split":
        res = slice_summary_split_dify(txt, window_size, overlap_size, api_key_input_1, api_key_input_2, url_input)

    else:
        raise ValueError(f"mode 必须是以下值之一: interation, split")

    return res


if __name__ == "__main__":

    window_size = 8000
    overlap_size = 800

    api_key_1 = "app-a9NOxUz7g28SHxZCGVV5lFEk"
    api_key_2 = "app-Man5i1vOvtVNyGpFmXOZ2Jg9"
    api_key_3 = "app-Cf0ABDjcC2LB5ez6p9g7XRtO"
    url = "http://219.147.31.54:11180/v1/workflows/run"

    print("Test:")
    result = main_dify("split", "testtxt/testtxt_compare1.txt", window_size, overlap_size, api_key_1, api_key_3, url)
    print(result)








