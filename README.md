# LLM Algorithm Lab

面向大模型算法岗位的个人学习与可复现实验仓库：从小型 GPT，到指令微调，再到可验证奖励的强化学习。

> 当前状态：学习与实验框架已建立；三个算法项目尚未实现、尚未训练。仓库不包含真实模型效果或求职成果声明。完成实验后用日志和报告更新状态。

## 给面试官

本仓库将展示模型实现、数据划分、基线比较、消融实验、错误分析与复现方法。当前仅可审阅学习计划、实验规范和评测结果校验工具，不能据此认定作者已掌握以下算法。

| 项目 | 状态 | 计划检验的能力 | 入口 |
|---|---|---|---|
| Tiny GPT | 待实现 | 因果注意力、训练循环、泛化分析 | [项目说明](projects/01-tiny-gpt/README.md) |
| SFT / LoRA | 待实现 | 数据质量、参数高效微调、独立评测 | [项目说明](projects/02-sft-lora/README.md) |
| Verifiable RL | 待实现 | 奖励设计、GRPO、奖励投机分析 | [项目说明](projects/03-verifiable-rl/README.md) |

## 从这里开始

1. 阅读 [学习路线与地址](docs/learning-path.md)，先完成 PyTorch 基础。
2. 按顺序实现项目；第一阶段可以在 CPU 上验证流程，真实训练规模按设备决定。
3. 每次实验复制 [报告模板](docs/experiment-template.md)，写入对应项目的 `reports/` 目录。
4. 按 [复现与评测规范](docs/reproducibility.md) 保存配置、数据来源、日志和失败案例。
5. 满足项目验收标准后，更新此表并链接具体实验报告。不要填写未经测量的提升数字。

## 本地检查（只用 Python 标准库）

```powershell
python -m unittest discover -s tests -v
python tools/check_predictions.py examples/predictions.demo.jsonl
```

第二条命令仅演示数值精确匹配评测，示例数据不是模型预测，不能作为算法成绩。

后续训练代码和依赖应随项目实现提交；当前不提供不存在的训练命令或未验证的 GPU 环境。

## 发布与隐私

GitHub 发布步骤见 [发布说明](docs/github-publishing.md)。仅提交有权公开的数据、代码与日志，不提交密钥、个人资料、模型权重或大规模数据。外部课程和参考实现属于其各自作者；学习过程中记录借鉴来源和自己完成的部分。
