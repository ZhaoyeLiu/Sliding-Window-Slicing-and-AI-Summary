import requests
import json

def dify_call_single(txt, api_key_input, url_input):
    API_KEY = api_key_input
    API_URL = url_input

    payload = {
        "inputs": {'slice': txt},
        "response_mode": "blocking",
        "user": "L-test"
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        summary = result.get('data', {}).get('outputs', {}).get('summary')
        #print(summary)
    else:
        print("Dify API 请求失败:", response.text)
        return

    return summary


def dify_call_double(txt1, txt2, api_key_input, url_input):
    API_KEY = api_key_input
    API_URL = url_input

    payload = {
        "inputs": {'summary': txt1, 'slice': txt2},
        "response_mode": "blocking",
        "user": "L-test"
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        summary = result.get('data', {}).get('outputs', {}).get('summary_from_2')
        #print(summary)
    else:
        print("Dify API 请求失败:", response.text)
        return

    return summary


def dify_call_many(txt, api_key_input, url_input):
    # 输入内容用 ### 区分不同段落
    API_KEY = api_key_input
    API_URL = url_input

    payload = {
        "inputs": {'many_summaries': txt},
        "response_mode": "blocking",
        "user": "L-test"
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()
        summary = result.get('data', {}).get('outputs', {}).get('final_summary')
        #print(summary)
    else:
        print("Dify API 请求失败:", response.text)
        return

    return summary


if __name__ == "__main__":

    txt1 = '''
    今年以来，尽管面临比较大的外部冲击，国内金融体系仍然保持稳健。货币信贷呈现“数量增加、价格下降、结构优化”的运行特征；股市运行总体平稳，交易较为活跃。
    ###
    在5月7日举行的国新办新闻发布会上，中国人民银行行长潘功胜、金融监管总局局长李云泽、中国证监会主席吴清围绕“一揽子金融政策支持稳市场稳预期”有关情况进行了详解。
    ###
    十项政策加大宏观调控强度
    今年以来，人民银行实施好适度宽松的货币政策，强化逆周期调节，综合运用多种货币政策工具，服务实体经济高质量发展，为推动经济持续回升向好营造良好的货币金融环境。
    数据显示，一季度末，社会融资规模同比增长8.4%、贷款同比增长7.4%，广义货币供应量（M2）保持7%左右平稳增长，明显高于名义经济增速。社会融资成本保持低位，普惠小微、制造业中长期、科技型中小企业等贷款增速均快于全部贷款增速，信贷结构进一步优化。
    '''
    txt2 = '''
    潘功胜表示，为进一步实施好适度宽松的货币政策，人民银行将加大宏观调控强度，推出三大类共十项一揽子货币政策措施。
    这十项政策包括：降低存款准备金率0.5个百分点，预计将向市场提供长期流动性约1万亿元。完善存款准备金制度，阶段性将汽车金融公司、金融租赁公司的存款准备金率从目前的5%调降为0%。下调政策利率0.1个百分点，即公开市场7天期逆回购操作利率从目前的1.5%调降至1.4%，预计将带动贷款市场报价利率（LPR）同步下行约0.1个百分点。下调结构性货币政策工具利率0.25个百分点，包括各类专项结构性工具利率、支农支小再贷款利率，都从目前的1.75%降至1.5%；抵押补充贷款（PSL）利率从目前的2.25%降至2%。降低个人住房公积金贷款利率0.25个百分点，五年期以上首套房利率由2.85%降至2.6%，其他期限利率同步调整。增加3000亿元科技创新和技术改造再贷款额度，由目前的5000亿元增加至8000亿元。设立5000亿元“服务消费与养老再贷款”，引导商业银行加大对服务消费与养老的信贷支持。增加支农支小再贷款额度3000亿元，与调降再贷款利率的政策形成协同效应。优化两项支持资本市场的货币政策工具，将5000亿元证券基金保险公司互换便利和3000亿元股票回购增持再贷款的额度合并使用，总额度8000亿元。创设科技创新债券风险分担工具。
    '''

    api_key_1 = "app-a9NOxUz7g28SHxZCGVV5lFEk"
    api_key_2 = "app-Man5i1vOvtVNyGpFmXOZ2Jg9"
    api_key_3 = "app-Cf0ABDjcC2LB5ez6p9g7XRtO"
    url = "http://219.147.31.54:11180/v1/workflows/run"

    print("Test:")
    res = dify_call_many(txt1, api_key_3, url)
    print(res)