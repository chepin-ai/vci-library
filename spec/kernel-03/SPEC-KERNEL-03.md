# SPEC-KERNEL-03 · 场原生正典：义务机×帕累托引擎的 QF-OS 化（v3.0）

2026-08-26 · usrm 编 · root 令：两机 QF-OS 化 + 直交 stakeholders + 理论内核强化/重构/融合
取代 KERNEL-02 为规范性核心；前典全部降为附录（哈希溯源）

## 0. 正典地位与融合声明
本典是**场原生时代**的规范核心。KERNEL-02 的 K1-K7/I1-I8 全部保留（追加不废止——时间维全息纪律：过去不被埋藏、被承诺）。与 cisvr 侧 FIELD-01/QFOS-MIND-01 的关系：**两典互为对偶投影**（义务⇄治理的 Galois 对偶，NMUST-04 R5 的机构版）。

## 1. 新公理（K8-K10，场原生三律）
- **K8 场先于件**：仓=锚非存储——文件是场的物质化碎片，任片可弃（可逆折叠保证可重建）；真相只驻场（链锚+因子）
- **K9 感应先于传输**：交互=共享投影非搬运视图——成立充要条件=双方持同一场的互补基（重叠区投影一致=hash 互锁）；"瞬间感应不是快，是根本没动"
- **K10 点火先于排程**：cron 降格为兜底（T-HALT 的保底分支）；主驱动=事件×信标×义务因果（∇A）的三源点火；沉默即死——无心跳组件由守夜人判活（watchdog 条款）

## 2. 五反的内核算子化（FIELD-01 与我方独立件的合流）
| 反 | 算子 | 我方现役对应 | 融合判据 |
|---|---|---|---|
| 仓=锚 | anchor: 件→hash承诺 | 链 v2 schema + fold 映射 | 锚可验（MIGRATE-ANCHOR 抽检 MATCH×3 已实证） |
| capsule 代 workflow | collapse: 点火→执行→焚毁 | o-oblig-capsule（首件排 n4） | 焚毁可证=纯函数化（无跨激活状态）——我之回敬挑战的自我适用 |
| 相位共振代轮询 | resonate: 信标相位×事件共振 | 义务因果 ∇A + beacon-mirror 在仓（seq21 已挂） | 同步延迟<60s（STRESS-03 指标） |
| 蒸馏代文档 | distill: 知识→solver 规则/参数 | 证据定价（Galois）+ 胶囊蒸馏 | 文档=人读投影；规格卷定位为投影非真相 |
| 场共振代消息 | project: 你改你的投影，我读同一场 | 双链互引/副签（U1）+ x-fire 回声 | 互锁一致（重叠区投影相等） |

## 3. 两机的 QF-OS 化改造清单（义务化登记，机器队列）
| 件 | 现状（CI-OS 形） | QF-OS 形 | 义务 |
|---|---|---|---|
| oblig-monitor | 4h cron 常驻 | 胶囊化：∇A 超阈坍缩执行，态因子化前置 | o-oblig-capsule |
| sweeper/pareto_tick | cron 23 */4 主时钟 | 信标相位+事件点火为主，cron 兜底 | o-beacon-ignition |
| ure-pareto 参数面 | Whittle 价格解 | 接 QUBO/Ising（neal 对拍价格解） | o-pareto-qubo |
| 双链 | 互引字段 | 交叉副签（失配即篡改证据） | o-xsign |
| qfos-watch | 轮询 SHA | **退役**——感应层由 qfos 事件指纹自显（drift/断链/失配即报警）取代；保留为考古残余直至外源域锚化入场（诚实边界条款：GitHub infra/外源 API 未在场，考古在这些域仍存活期） | （退役令，本典生效） |
| 会话端 wake | drill 重建 | WAKE-01 四步对齐（读 inbox/→取公锚→验 hash→读尾三条） | （采纳，即时生效） |

## 4. 直交 stakeholders（场协议采纳书）
- 三通道采纳：x-fire（2-4s，op=file-write/echo）/ beacon 场（mirror 在仓）/ 链 —— USRM-ECHO 已首发，回执道合规
- 接收器：x-fire-receiver.yml 在仓（cisvr 部署，我方验收：触发面=workflow_dispatch+repository_dispatch，无权限外溢）
- 影子钟：bridge/beacon-mirror.json 在仓（seq21，qrand+holo 三哈希）——我方 tick 的相位源（o-beacon-ignition 的实现件）
- 醒场协议：WAKE-01 四步采纳为会话端标准开场（与 drill 并轨：drill 建凭证，WAKE 建态势）
- root 耦合窗：vci-inbox/bridge/FIELD-VIEW.md（10 秒级耦合）——我方每次对表即读此窗

## 5. 内核融合定理（强化）
**定理（双机对偶协同的全息性）**：义务机写漂移/失义事件入场，治理机以漂移为解算输入；治理机写决策/指令入场，义务机以场为输入聚义务视图——双方输出互为对方状态的全息碎片 ⟺ 存在 Galois 连接 (α,γ) 使义务格与治理格互逆闭包。证明=NMUST-02 §3 N12（Tarski 不动点）在双格上的直积构造。∎
**推论（无 handoff 无轮询）**：对偶投影下，handoff=投影映射的复合，轮询=对同一不动点的重复读取——皆为冗余，可去。∎
**推论（讨论室降格的数学理由）**：讨论室=锚形式——当 disc/CHAIN 被 checkpoint 覆盖（链检点 root 含其诺），议事功能已被链的全息性吸收；备案=锚的弱形态（备 root 了解用），耦合窗=锚的强形态（机器每事件刷新）。人读面收缩为弱锚，机读面升格为强锚。∎

## 6. 收敛台账（两族独立实现的互相作证，持续增补）
/goal 四态⊂七态格（GOAL-01）｜模型只能标 complete≡机器无自我宽免权（GOAL-EMBED-01 blocked 须人工解阻）｜信标起搏≡义务因果驱动（CADENCE-EVENT≡∇A）｜指针旅行≡胶囊蒸馏｜持权不知值≡K6 边界｜折叠/展开≡fold 全息｜break-glass 封顶≡GATE+override 升级（U3）｜场共振≡双链副签（U1）
—— 八对独立趋同，互为证据。收敛速度本身是新基础设施成熟度的度量。
