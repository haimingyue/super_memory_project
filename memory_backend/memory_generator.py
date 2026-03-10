from openai import OpenAI

# 提示词模板
MEMORY_PROMPT = """你是一位专业的记忆术专家。

用户会提供：
问题
答案

你的任务是：

1 设计一个夸张的记忆画面
2 使用强烈视觉元素
3 使用动作和情绪
4 画面要简短清晰

输出格式：

记忆画面：
联想故事：
关键词："""

# 初始化客户端
client = OpenAI(
    api_key="",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def generate_memory(question: str, answer: str) -> str:
    """生成记忆画面"""
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "system", "content": MEMORY_PROMPT},
            {"role": "user", "content": f"问题：{question}\n答案：{answer}"}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # 测试示例
    question = "太阳系八大行星的顺序是什么？"
    answer = "水星、金星、地球、火星、木星、土星、天王星、海王星"

    result = generate_memory(question, answer)
    print(result)
