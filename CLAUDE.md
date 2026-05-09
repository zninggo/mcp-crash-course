# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

MCP Crash Course 教学仓库，通过分支结构学习 Model Context Protocol (MCP)。每个 `project/*` 分支覆盖一个 MCP 主题，提交按时间顺序排列，逐步学习。

## 当前分支

`project/langchain-mcp-adapters` — 集成 MCP 与 LangChain 适配器。

## 常用命令

```bash
# 安装依赖
uv sync

# 运行主程序
uv run main.py
```

包管理器：`uv`（非 pip）。Python >=3.12。

## 关键依赖

- `langchain-mcp-adapters` — LangChain 与 MCP 的桥接层

## 代码规范

- 函数优先，避免不必要的类
- 类型标注所有函数签名
- 使用 Pydantic v2 做输入验证
- `def` 用于纯函数，`async def` 用于异步操作
- 文件和目录使用小写加下划线命名
