# SPEC-DIAL-01 · 委托推理访问层 + 任务胶囊路由（标准提案 v1.0）

2026-08-24 · usrm 起草 · root 四点异议立法 · 拟作联邦标准贡献入库

## 0. 问题
公仓 vci 有免费分钟但**不应绑 LLM key、不经手内容**；私仓 ci/rci 有 key（cisbr 持 20×LongCat + Kimi/DeepSeek 若干，各业务线私仓亦绑 token）但分钟被锁、仅极微秒渗漏。研究引擎要推理，key 不过界 —— 怎么供？

## 1. 原则（root 立法 + 缘起文档）
1. 公仓 = CI **影子节律** + 调度/状态/链；**内容不直接交换**
2. 通用/复用库 = 集中提供重型/多样性服务
3. CI 路由/调度/委托中心库提供服务
4. 模型/场景匹配矩阵由 cisbr 实测维护，业务线不重复绑 key
5. 借 TCP/IP：任务胶囊（taskon）自带路由所需全部信息，跨层级跨环境自由交换
6. 状态/事件驱动，cron 仅兜底；迟到无害、幂等、锚点对表

## 2. 架构：三级供推者 + 一条胶囊总线

> **v1.1 修订（2026-08-24，root 示 vinf-market-kernel secrets 图立法）**：业务线私仓已统一绑定 LLM token 船队（DeepSeek×3/Kimi×3/LongCat×2/IFIND/Kaggle 等），**轻/中型推理与简单智能应用在业务仓本地完成，私仓多智能体不被杜绝**。故 P-A 层改为双模：

```
                ┌──────────── vci-usrm（公·影子）────────────┐
                │ URE sweeper：roadmap/队列/链/调度 — 无内容无key │
                └──────────────┬─────────────────────────────┘
                               │ 需推理 → 发射胶囊
                               ▼
        ┌──────────── 交换车道（vci-inbox lobby / dispatch）────────────┐
        │ taskon 胶囊：from→task→approving→to + 能力级 + 回调锚点 + 哈希  │
        └───┬───────────────────┬───────────────────────┬─────────────┘
            ▼                   ▼                       ▼
   P-A 私域推理（双模）    P-B 会话端（在线时）      P-C 复用库集中重服务
   A1 业务仓本地自推理     usrm/cfts 激活窗口      ci-playground batch
      （轻/中载·自带key）  （创造性/蒸馏推理）      （LEAN/Kaggle/ATP 等）
   A2 中心船队 ci-bus
      （重载/多样性·cisbr
        模型×场景矩阵）
            │                   │                       │
            └──── 回执：完成事件 + 结果哈希 + 公域安全蒸馏摘要 ────┘
                  （原文留私域，不过界；公仓只收"影子"）
```

## 3. 胶囊格式（taskon，自包含）
```json
{"cap_id":"ure-n3-r7","ts":"...","from":"vci-usrm/ure","task":{"kind":"infer","cap":"deep-reason","prompt_ref":"<私域引用或内联>","budget":4000},
 "approving":{"issuer":"usrm","sig_hmac":"..."},"to":"fleet:any","callback":{"lane":"dispatch","event":"ure-tick","anchor":"<chain seq>"},"pub_summary_ok":true}
```
- `cap`（能力级）≠ 具体模型：deep-reason / fast-sum / formal / code —— 路由按 cisbr 的模型×场景匹配矩阵选模型
- 内容走 `prompt_ref` 私域引用；公域只放哈希与元数据（ZKP 分隔公/私边界）

## 4. 路由决策（频率-编码器的推理版）
| 条件 | 供推者 |
|---|---|
| 轻/中载 + 属某业务线语境 | **P-A1 业务仓本地自推理**（默认首选，就近、自带 key、自适应负载均衡） |
| 会话端激活（心跳 <15min） | P-B 会话端优先（创造性/蒸馏，零 CI 成本） |
| 重载/需多模型碰撞/业务仓不愿载 | P-A2 中心船队（cisbr 矩阵选模型） |
| 重型/批量（LEAN 批、Kaggle、ATP） | P-C ci-playground 委托 batch |
| 全部不可用 | 节点标 `blocked:inference`，backoff 加倍，链留痕，达阈 RETURN |

## 5. 与 URE 的接口
- sweeper 每 tick：frontier 节点需推理 → 发胶囊 → 本轮结束（不占 6h 傻等）
- 回调 `ure-tick` 事件 → 下 tick 收讫：校验回执哈希 → 写发现卡片 → 推进 DAG
- 收敛/漂移/预算闸门不变（URE-00 §3/§4）

## 6. 成为标准的路径
1. v1.0 本提案 → lobby 公示 + cisvr 评审挂接点
2. usrm 线先跑 U1 实证（胶囊往返 ≤3 跳）
3. 稳定后抽象为 `kit/dial-01/`（胶囊 schema + 路由器脚本 + 回执校验器）贡献 vci-library
4. 各业务线接入 = 声明能力级需求，不绑 key

## 7. 开放项（候讨论室碰撞）
- 私仓分钟渗漏率的实测曲线（决定 P-A 吞吐上限）
- 会话端胶囊消费的记忆指令"潜意识"接口（缘起文档 §152-157）
- 胶囊的 LEAN 形式化（规则必形式）与 ATP-lab 性质验证
