from openai import Client

def openai_call_single(message, prompt, api_key_input, url_input, model_input):
    client = Client(
        api_key=api_key_input,
        base_url=url_input
    )

    res = client.chat.completions.create(
        model=model_input,
        messages=[
            {
                "content": prompt,
                "role": "system",
            },
            {
                "content": f"帮我总结以下这段话： {message}",
                "role": "user",
            }
        ],
        temperature=0.1,
        max_tokens=10240
    )
    res = res.choices[0].message.content
    print(res)
    return res


def openai_call_double(message_summary, message_slice, prompt, api_key_input, url_input, model_input):
    client = Client(
        api_key=api_key_input,
        base_url=url_input
    )

    res = client.chat.completions.create(
        model=model_input,
        messages=[
            {
                "content": prompt,
                "role": "system",
            },
            {
                "content": f"以下是上一个切片的总结：{message_summary}，以下是下一个切片的内容：{message_slice}。请将上一个切片的总结和下一个切片的内容总结为一段话",
                "role": "user",
            }
        ],
        temperature=0.1,
        max_tokens=10240
    )
    res = res.choices[0].message.content
    print(res)
    return res


def openai_call_many(list, prompt, api_key_input, url_input, model_input):
    client = Client(
        api_key=api_key_input,
        base_url=url_input
    )

    res = client.chat.completions.create(
        model=model_input,
        messages=[
            {
                "content": prompt,
                "role": "system",
            },
            {
                "content": f"以下是对一篇文章里所有文章切片的总结，每个总结之间用“###”来分隔：{'###'.join(list)}，请将所有这些总结总结为一个总结",
                "role": "user",
            }
        ],
        temperature=0.1,
        max_tokens=10240
    )
    res = res.choices[0].message.content
    print(res)
    return res


if __name__ == "__main__":
    print("Test:")
    message = "新华社北京5月15日电??5月14日，国家主席习近平致电让－吕西安·萨维·德托夫，祝贺他就任多哥共和国总统。同日，习近平主席还致电福雷·埃索齐姆纳·纳辛贝，祝贺他就任多哥共和国部长会议主席。习近平指出，中多友好关系由两国历代领导人共同缔造和精心培育。半个多世纪以来，双方始终坚持真诚友好、平等互信、合作共赢，在涉及彼此核心利益和重大关切问题上坚定相互支持，成为大小国家平等相待和全球南方团结合作的典范。2024年中非合作论坛北京峰会期间，中多关系提升为全面战略伙伴关系，开启了两国关系新篇章。我高度重视中多关系发展，愿同多哥领导人一道努力，以落实中非合作论坛北京峰会成果为契机，赓续传统友好，拓展各领域合作，不断丰富两国全面战略伙伴关系内涵，更好造福两国人民。同日，国务院总理李强也致电祝贺福雷就任多哥共和国部长会议主席。"
    prompt = "总结要庄重、朴实、严肃"
    api_key = "not empty"
    url = "http://citybrain.hisense.com/Qwen3-32B/v1"
    model = "Qwen3-32B"
    res = openai_call_single(message, prompt, api_key, url, model)
    print(res)