# Project Context

## Project Name
**Super Memory** - 记忆画面生成系统

## Project Goal
帮助用户将学习知识点转换为生动形象的视觉记忆画面，通过 AI 生成联想故事来增强记忆效果。

## Core Modules
- **memory_backend** - Python 后端，负责调用 AI API 生成记忆画面
- **memory_front** - Nuxt 3 前端，提供用户界面

## Current Development Focus
- 项目初始化阶段
- 后端：完成基础 AI 集成
- 前端：Nuxt 3 项目搭建完成

## Key Architecture Decisions
- 使用阿里云 DashScope API（通义千问）作为 AI 引擎
- 前端使用 Nuxt 3 + Vue 3 + TypeScript
- 前后端分离架构

## Important Prompts

### 记忆画面生成提示词 (prompt_memory.txt)
```
你是一位专业的记忆术专家。
用户会提供：问题、答案
任务：设计夸张的记忆画面，使用强烈视觉元素、动作和情绪
输出格式：记忆画面、联想故事、关键词
```

## Important Directories
```
memory_project/
├── memory_backend/      # Python 后端
│   ├── memory_generator.py   # 记忆生成器
│   ├── prompt_memory.txt     # 提示词模板
│   └── test.py               # 测试文件
├── memory_front/        # Nuxt 3 前端
│   ├── app.vue
│   ├── nuxt.config.ts
│   └── package.json
├── docs/                # 项目文档
├── daily-log/           # 每日开发日志
└── tasks/               # 任务管理
```

## Backend Stack
- Python 3.14
- OpenAI SDK (兼容模式)
- API: 阿里云 DashScope (qwen-plus 模型)

## Frontend Stack
- Nuxt 3
- Vue 3
- TypeScript
- Node.js 24

## API Architecture
```
前端 (Nuxt 3) <--HTTP--> 后端 (Python/FastAPI) <--API--> 阿里云 DashScope
```

## Environment Variables
- `DASHSCOPE_API_KEY` - 阿里云 API 密钥

## Current Status
- 后端：基础功能完成，等待 API 接口封装
- 前端：项目初始化完成，等待页面开发
