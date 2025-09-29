from LLM.dify.dify_call import dify_call_single, dify_call_double, dify_call_many
from Slice.sliding_window_split_text_txt_package import sliding_window_split_text_txt

def slice_summary_iteration_dify(txt, window_size, overlap_size, api_key_input_1, api_key_input_2, url_input):
    list = sliding_window_split_text_txt(txt, window_size, overlap_size)

    if len(list) == 1:
        the_summary = dify_call_single(list[0], api_key_input_1, url_input)

    else:
        the_summary = dify_call_single(list[0], api_key_input_1, url_input)
        print(the_summary)
        for i in range(1, len(list)):
            the_summary = dify_call_double(the_summary, list[i], api_key_input_2, url_input)
            print(the_summary)

    return the_summary


def slice_summary_split_dify(txt, window_size, overlap_size, api_key_input_1, api_key_input_3, url_input):
    list = sliding_window_split_text_txt(txt, window_size, overlap_size)
    temp_list = []
    if len(list) == 1:
        the_summary = dify_call_single(list[0], api_key_input_1, url_input)
        return the_summary

    else:
        for i in range(len(list)):
            temp_summary = dify_call_single(list[i], api_key_input_1, url_input)
            print(temp_summary)
            temp_list.append(temp_summary)

    combine_summary = "\n###\n".join(temp_list)
    final_summary = dify_call_many(combine_summary, api_key_input_3, url_input)
    return final_summary

if __name__ == "__main__":
    print("1")









