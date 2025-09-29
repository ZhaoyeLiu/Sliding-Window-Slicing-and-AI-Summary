from LLM.openai.qwen_call import openai_call_single,openai_call_double,openai_call_many

def slice_summary_iteration(list, prompt_1, prompt_after_1, api_key_input, url_input, model_input):

    summary_1 = openai_call_single(list[0], prompt_1, api_key_input, url_input, model_input)

    if len(list) == 1:
        return summary_1

    else:
        summary_after_1 = summary_1
        for i in range(1, len(list)):
            summary_after_1 = openai_call_double(summary_after_1, list[i], prompt_after_1, api_key_input, url_input, model_input)

    return summary_after_1


def slice_summary_split(list, prompt_single, prompt_all, api_key_input, url_input, model_input):

    summary_list = []

    for i in range(len(list)):
        summary_temp = openai_call_single(list[i], prompt_single, api_key_input, url_input, model_input)
        summary_list.append(summary_temp)

    res = openai_call_many(summary_list, prompt_all, api_key_input, url_input, model_input)
    return res



if __name__ == "__main__":
    print("1")
