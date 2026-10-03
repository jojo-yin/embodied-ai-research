# embodied-ai-research

个人具身智能科研知识库。同时承担两个身份：**知识资产库**与**科研履历**。

## 这个仓库在做什么

系统学习具身智能 / VLA，并把每一步的**过程**留下证据：读过的论文有逐条作答的笔记，跑过的实验有可复现的 config 与数值结果，复现过的论文有与原文指标的对账表。

## 目录导航

| 目录 | 放什么 |
|---|---|
| `mathematics/` | 线性代数、概率统计、微积分、最优化笔记 |
| `robotics/` | 坐标系与位姿、正 / 逆运动学、抓取几何 |
| `ros2/` | ROS 2 工程（节点 / 话题 / 服务 / 动作、TF、录包回放） |
| `computer_vision/` | 图像分类、目标检测、语义分割、自监督表征 |
| `deep_learning/` | MLP → CNN → 注意力机制与 Transformer |
| `reinforcement_learning/` | 强化学习 |
| `imitation_learning/` | 模仿学习 |
| `VLA/` | Vision-Language-Action 主线 |
| `papers/` | 论文精读，`paper_XXX/` 编号连续 |
| `reproductions/` | 论文复现工程 |
| `experiments/` | 实验记录，固定七字段 |
| `projects/` | 项目与成果整合 |

每个目录下都有自己的 `README.md`，写明该目录的命名约定与模板。

## 使用方式

### 读一篇论文

在 `papers/` 下新建 `paper_XXX/`（编号连续不跳号），按顺序产出三份文件：

1. `paper_notes.md` —— 逐条书面回答**精读十二问**，不允许只写摘要
2. `reproduction.md` —— 复现过程、命令、踩坑记录
3. `conclusion.md` —— 结论与**可迁移的东西**

**`conclusion.md` 没写，这篇论文视为未完成。**

### 记一次实验

在 `experiments/` 下新建 `exp_XXX.md`，固定七字段：

`Question / Hypothesis / Setup / Result / Observation / Explanation / Next Experiment`

**Observation（客观现象）与 Explanation（主观推断）必须分开写。**

### 复现一篇论文

走完八环节，缺一不算：

论文 → GitHub → 环境配置 → Dataset → Baseline → Training → Evaluation → 结果

必须与论文报告的指标做**数值对比**。**只跑到 Training 不算复现。** 环境配置 4 小时上限，超时换方案。

## 仓库纪律

- 目录名一律用**英文**，避免中文路径导致的编码问题。
- 实验产生的 **config 文件必须入库**。没有 config 的结果等同于没做。
- **权重、数据集、日志不入库**（见 `.gitignore`）。
- 每条实验记录的 `Setup.Config` 必须指向一个仓库里**真实存在**的文件。
