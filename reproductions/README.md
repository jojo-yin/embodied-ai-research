# reproductions — 论文复现工程

一次完整复现 = 走完**八环节**，缺一不算：

    论文 → GitHub → 环境配置 → Dataset → Baseline → Training → Evaluation → 结果

**硬性要求**
- 必须把复现结果与论文报告指标做**数值对比**，差异写进 `reproduction.md`。
- **只跑到 Training 不算复现。**
- 环境配置设 **4 小时上限**，超时换方案。

**约定**：一个复现一个子目录 `<论文简称>/`，内部结构同 `papers/paper_XXX/`。
