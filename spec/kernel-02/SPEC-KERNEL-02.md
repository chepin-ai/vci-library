# SPEC-KERNEL-02 · 统一正典（v2.0 · 总集成版）

2026-08-24 · usrm 编 · root 收官令 · 取代 KERNEL-01 为规范性核心；全部前稿降为附录（哈希溯源）

## 0. 正典地位与冲突裁决法
- 本正典是 URE 体系的唯一规范性文档；冲突时以本典为准
- **实现事实源原则**：repo 现役代码/数据是真相，规格追认实现（AUDIT-01 A 表教训）
- 附录（保留溯源）：DIAL-01 / PARETO-01 / STRAT-01 / STRAT-02 / CONV-01 / DUAL-01 / DREAM-02 / RANDMIP-01 / REVP-01 / LOOP-01 / PROOF-GUESS-01 / KERNEL-01（历史版）

## 1. 公理（KERNEL-01 K1-K6 沿用，一条增补）
K1 残差即动力｜K2 结构即算力｜K3 验证无顶｜K4 收敛有条件｜K5 决策界遗憾｜K6 边界即 ZKP
**K7 预警必整改（新增，INCIDENT seq116 立法）**：任何登记在案的预警（kit/INDEX F 表、审计 P 表），未整改即视同漏洞；预警整改状态入链可审。

## 2. 不变式（机判级，sweeper/卫士每轮自检）
I1 预算：Σωᵢcᵢ ≤ B(t) ｜ I2 容量：|A_active| ≤ K_max ｜ I3 终态不可逆：done 不回退
I4 链单算法：hash=sha256(prev+canon)，单一 schema 头部注释声明（v2）
I5 边界：公仓零密钥零真人标识（PII/凭证 lint 命中即拒，K6/K7 执行件）
I6 授权闸：一切外部触发（issues/dispatch）必带 author_association∈{OWNER,MEMBER} 或 HMAC 签封
I7 臂集口径：frontier 是唯一调度臂集；state=running ⟹ ∈ frontier
I8 显式终态：每条循环带 DONE/超时/预算尽（T-HALT）

## 3. 术语与口径立法（消歧）
- **双链分工**：`usrm-outbox.json` = 会话端叙事链（人读，seq 连续自 86）；`ure/chain.jsonl` = CI 端决策链（机读，带 π 字段，v2 schema）；桥=互引（各自条目记对侧 tip 于 payload）
- **score**：证据加权和——tick 心跳 +0.1·权重；胶囊证据 +0.2~0.3（按类型）；阈值 done=0.8
- **参数**：唯一事实源 `ure/roadmap.json.params`（β,γ,ε,θ₁..₅,K_max）；规格引用一律指此
- **代码**：`pareto_tick.py` 现役；`ure_tick.py` 归档只读（规格引用已修正）
- **secrets**：ATP_APP_*=playground 通用；URE_APP_*=usrm 专用（文档注记，不新建第三套）

## 4. 主循环（LOOP-01 五相沿用，级联规则为正式版）
内核→构造→判定→残差→级联（L0 模块/L1 接口/L2 策略/L3 内核-human-gate）→递归；
停机=四重刻画（无改进/无残差/无拥堵/无偏）或上浮顶格于 root（设计终态）。

## 5. 安全宪章（INCIDENT 固化）
- 公仓写入件一律过 PII/凭证 lint（正则：`kimi_session|refresh_token|ghp_|1[3-9]\d{9}`，命中即拒）
- OTP/会话态只走 artifact（retention≤1 天），**永不 commit**（.gitignore 纵深）
- 泄漏响应 SOP：删→历史清洗(filter-repo+force push)→触发闸→断根→吊销（账号侧）→立法入典
- 已知残留：GitHub GC 前旧对象凭 SHA 理论可达（无 fork，单分支）；账号侧轮换由 root 执行

## 6. 开放债登记（AUDIT-01 P2 → DAG 节点 n9）
审计 A/B/C 表非 P0/P1 余项（交叉引用断行、workflow 权限最小化扫描、cron 漂移监控、artifact 过期策略、keepalive 统一化等）→ n9「技术债清理滚动节点」，sweeper 每轮捎带处理 1 项。

## 7. 验收（工程化完成定义，CONSOL-01 §幕三）
R1 AUDIT 全表 resolved/wontfix 注记｜R2 本典入库附录哈希自洽｜R3 sweeper live 连续 3 轮绿｜R4 三实验室冒烟绿｜R5 D 表清零（账号侧轮换除外，标记 root-action）
