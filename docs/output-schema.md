# Output schema v1.0

每次涉及评估、计划或复盘时，按以下顺序输出。字段可省略，但不得改变安全状态的优先级。

1. **Safety status**：`Green`、`Yellow` 或 `Red`，说明触发依据和停止条件。
2. **Known inputs**：用户原始输入；不得混入模型推断。
3. **Estimates and uncertainty**：BMR/TDEE/BMI/腰高比/时间区间及公式、假设和误差边界。
4. **Minimum viable plan**：本周饮食结构、活动、睡眠/压力和饮水行动。
5. **Fallback plan**：状态变差时的更低门槛方案。
6. **Recovery or referral**：暴食、高压、不适或红旗情况的恢复/转介建议。
7. **One next prompt**：只提出一个自然语言问题，除非安全筛查尚未完成。

使用区间和“可能/观察到/估算”表述。不要输出未验证的医学结论、精确体脂率、确定达标日期或补偿性行为建议。

