# experiments — 实验记录

**命名**：`exp_001.md`、`exp_002.md`…… 编号连续，不跳号。

每条记录固定**七字段**，其中 **Observation（客观现象）与 Explanation（主观推断）必须分开写**：

    Experiment 001
    Question:         <一句话描述要回答的问题>
    Hypothesis:       <可检验的预期，包含方向>
    Setup:
      Dataset:
      Model:
      Baseline:
      Metric:
      Seed:
      Config:         <指向 config/ 下的文件>
    Result:           <数值结果，必须带指标名>
    Observation:      <客观现象，不带解释>
    Explanation:      <你的推断，可写多个候选假设>
    Next Experiment:  <下一步要验证什么>

**纪律**：没有 config 的结果，半年后无法复现，**等同于没做**。
