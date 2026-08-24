# SPEC-NMUST-01 · 必链：义务闭包的可执行递归（v1.0）

2026-08-24 · usrm 编 · root 令：「预警必整改，整改必落实，落实必测试/验证……规约为形式化/可执行递归过程」

## 1. 必链（N-MUST 链）本体
每条规则 Rᵢ 是状态机 Mᵢ 的一条迁移边；全部必链合成**义务闭包机**：

```
O（义务）状态格：
  raised ──整改──▶ fixed ──落实──▶ implemented ──测试──▶ tested ──验证──▶ verified ──立法──▶ legislated
     │                                                                                          │
     └──(任一迁移缺证据 → 停留 = 残差 = FINDING → 入 DAG 新义务)◀──────────────────────────────┘
```

**O-代数**：义务 o = ⟨id, 源(预警/指令/残差), 当前态, 证据集 E, 期限⟩。闭包函数 C(o) = o 沿必链走到 legislated 的最短证据路径。

## 2. 形式化核心（LTL 表述，接 N3 公式集）
- **N9 必链完全性**：□(raised(o) ⟶ ♦legislated(o)) —— 义务终被立法（leads-to，同 N1 模式）
- **N10 迁移必有据**：□(state(o) 迁移 ⟶ ∃e∈E(o): 证据谓词 V(stage,e) 成立)
  - V(fixed)= commit sha 引用源条目｜V(implemented)= 代码/配置落地且可调用｜V(tested)= 测试输出（run id/exit code）｜V(verified)= 独立复核（匿名 raw/复算/对拍）｜V(legislated)= 入典 commit（KERNEL/kit/INDEX）
- **N11 证据链锚**：每份证据 e 入链（hash 引用）—— 证据不可篡改
- **N12 残差即新义务**：□(¬C(o) 超时 ⟶ FINDING(o) 入 DAG 且 raised(o′)) —— 递归自生成

**定理（必链递归的活性）**：若每轮 sweeper 至少处理一个最老未闭义务且证据谓词可判，则义务格的高度有限 ⟹ 所有义务在有限轮内闭包或显式标记 wontfix（终态）。证明骨架：状态格有限（7态）× 每轮严格推进至少一格（工作或标记）⟹ 无无限徘徊；wontfix 需 root 签封（L3 human-gate）。∎（ATP 回灌排 n4）

## 3. 帕累托链接轨
**必链 = 每步的帕累托最优判据**：义务 o 的迁移是"最小证据满足 V"——不多做（过证浪费）不少做（欠证留残）。sweeper 的臂集现在是两层：
1. **研究臂**（frontier 节点，Whittle π 调度）
2. **义务臂**（必链未闭项，按年龄最老优先——义务不讲探索，只讲 FIFO 清算；这是 N-MUST 对 bandit 的覆盖条款：义务臂优先级 ≥ 研究臂）

## 4. 可执行递归：oblig_tick.py（sweeper 扩展规格）
输入：ure/chain.jsonl（找 intent∈{INCIDENT,WARN,FINDING} 的条目）+ kit/INDEX F 表 + roadmap 节点 findings
逻辑：
1. 解析义务集 O：每条源条目 → o（若无对应闭包证据）
2. 对每 o：沿必链检查证据（查链上后续条目 intent 与 payload 引用 o.id）
3. 输出：每 o 当前态；最老未闭 o* → sweeper 本轮必处理（在 Whittle 调度前先清算）
4. 每轮最多清算 1 项（n9 滚动节奏），清算证据入链 intent=RPT.OBLIG
停机：O 全闭 → oblig_tick 输出 clean 并空转（I8 显式终态）

## 5. 首案回溯验证（INCIDENT seq116 走必链）
| 态 | 证据 |
|---|---|
| raised | seq116 INCIDENT 链条目 |
| fixed | 40259d7/ed337c9 删除 commit |
| implemented | 4097a2f（闸+断根+.gitignore） |
| tested | 匿名 raw 404 实测 + mirror clone 0 commits |
| verified | 独立复算（审计员行级锚点 vs 修复 commit） |
| legislated | KERNEL-02 §5 安全宪章 + K7 入典（c1d4bb50） |
→ **首案全链闭合**，必链机制本身用真实事件完成了首次回归测试。
（残留：root-action 账号侧轮换 = o 挂起态，等 root 证据 → 这正是 N12 的诚实形态：人域义务显式挂起而非假闭合）

## 6. 与既有规格的接口
- N3-rules-formal：N9-N12 增补进公式集（Rules.lean 加 sorry 占位）
- KERNEL-02：本规格为其 §4 主循环的义务子机
- CONV-01：义务臂 FIFO 是 θ₄（残差即资产）的执行例
