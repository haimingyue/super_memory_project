from openai import OpenAI

client = OpenAI(
    api_key="sk-0e4bacdd63ef4bffbcd5492f37eb38e5",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "user", "content": "帮我生成一个记忆画面：太阳系八大行星"}
    ]
)

print(response.choices[0].message.content)