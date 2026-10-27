# 学习路线与学习地址

以下为课程原站、官方文档或作者维护的参考实现。2026-10-27 整理；文档会更新，实现时记录实际依赖版本。时间仅供安排，不是掌握程度承诺。

## 0. PyTorch 基础（建议 1–2 周，按基础调整）

- [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)：张量、数据集、自动求导、训练循环、保存加载。
- [Karpathy Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)：神经网络与语言模型原理。

验收：不照抄教程完成一个小型分类训练流程；解释梯度、训练/验证划分和过拟合；保存并重新加载模型。

## 1. Tiny GPT（建议 3–5 周）

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)：重点理解注意力公式、位置编码与 mask。
- [作者维护的 nanoGPT](https://github.com/karpathy/nanoGPT)：学习代码组织与训练流程，标注借鉴，不将 fork 视为独立实现。
- [项目任务](../projects/01-tiny-gpt/README.md)。

顺序：字符级 tokenizer → 数据切分 → 单头因果注意力 → 多头注意力 → Transformer → 训练 → 采样 → 消融。

## 2. 指令微调（建议 3–5 周）

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/zh-CN/chapter1/1)：tokenizer、数据集、Transformer 和微调。
- [Hugging Face smol-course](https://huggingface.co/learn/smol-course/en/unit0/1)：后训练实践；先完成深度学习基础。
- [PEFT 官方文档](https://huggingface.co/docs/peft/index)：LoRA 配置和适配器加载。
- [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer)：按安装版本阅读对应文档。
- [LoRA 论文](https://arxiv.org/abs/2106.09685)。

先做小规模 smoke test，再决定模型、序列长度、训练量。未确认显卡和可用显存前，不承诺本地能运行某个模型。

## 3. 可验证奖励强化学习（建议 4–6 周或更久）

- [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction)：策略、奖励、优势函数基础。
- [DeepSeekMath 论文](https://arxiv.org/abs/2402.03300)：阅读 GRPO 部分。
- [TRL GRPOTrainer](https://huggingface.co/docs/trl/grpo_trainer)：训练接口与配置。
- [项目任务](../projects/03-verifiable-rl/README.md)。

先用合成整数算术任务练习。无需立即做复杂 Code Agent；完成奖励验证、SFT/RL 对照和错误分析后再扩展。

## 每周工作方式

每周完成一个能解释的小改动，写一份实验记录。代码可以借助 AI，但应能自行解释、修改和验证；在报告中写明工具辅助范围。学习笔记、真实失败与复现实验比空泛的技术列表更有用。
