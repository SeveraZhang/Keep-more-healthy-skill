# weight-loss-coach

一个运行在 Codex Desktop 中的生活化减脂健康教练 Skill。它帮助用户估算代谢、进行运动风险分层、使用自然语言记录生活状态、制定低负担计划，并在压力、睡眠不足或暴饮暴食后回到可持续节奏。

> **安全边界**：本 Skill 提供估算、行为支持与趋势复盘，不提供医疗诊断、治疗或处方。出现胸痛、晕厥、明显心悸、呼吸困难、持续疼痛、反复暴食或补偿行为时，应停止自行加码减脂计划，并优先咨询医生、注册营养师或心理健康专业人士。

## 适合什么场景

- 初次减脂评估：BMR、TDEE、BMI、腰高比和时间区间
- 体检后运动前的绿/黄/红风险提示
- 不能称重时的餐盘、手掌和烹调方式估算
- 通过一句话、照片或截图记录压力、睡眠、饮食和活动
- 暴食后的去羞耻化恢复计划
- 每周趋势复盘，而不是每日强制打卡

## 安装到 Codex

### 方式 A：直接复制

将本目录复制到个人 Skills 目录，然后重启 Codex 或新开任务：

```bash
mkdir -p "$HOME/.codex/skills"
cp -R weight-loss-coach "$HOME/.codex/skills/"
```

调用：

```text
使用 $weight-loss-coach 帮我完成一次低负担的减脂健康评估。
```

### 方式 B：从 GitHub 克隆

```bash
git clone https://github.com/<your-account>/weight-loss-coach.git
cp -R weight-loss-coach "$HOME/.codex/skills/"
```

## 目录结构

```text
weight-loss-coach/
├── SKILL.md                         # 主工作流和安全优先级
├── agents/openai.yaml               # Codex UI 元数据
├── references/defaults.yaml         # 可调参数
├── references/safety-and-triage.md  # 运动风险分层
├── references/lifestyle-food-estimation.md
├── references/binge-recovery.md
├── references/photo-guidance.md
├── assets/intake-template.md
├── assets/weekly-review-template.md
├── scripts/calculate_metrics.py     # 可复核计算脚本
├── tests/test_cases.md              # 发布前测试集
├── docs/output-schema.md             # 输出结构规范
├── CHANGELOG.md
└── LICENSE
```

## 参数和迭代

优先修改 `references/defaults.yaml`：热量缺口、活动系数、复盘周期、提醒默认值、压力降阶和暴食恢复模式都集中在这里。安全规则修改 `references/safety-and-triage.md`；整体交互顺序才修改 `SKILL.md`。

每次发布前：

1. 更新 `references/defaults.yaml` 的 `version` 和 `CHANGELOG.md`。
2. 运行计算脚本测试。
3. 按 `tests/test_cases.md` 手工验证安全、压力、暴食和自然语言场景。
4. 运行 Codex Skill 结构校验：

```bash
python3 "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" ./weight-loss-coach
```

如本机没有 PyYAML，可先安装：

```bash
python3 -m pip install PyYAML
```

## 许可证

MIT。健康建议和免责声明详见 `LICENSE` 与 `SKILL.md`。

