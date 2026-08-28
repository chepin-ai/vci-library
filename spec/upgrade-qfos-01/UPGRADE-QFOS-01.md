# UPGRADE-QFOS-01 · cisvr QF-OS 雏形 → URE/义务机升级映射（v1.0）

2026-08-25 · usrm 编 · 源：QFOS-archaeology（八件套全实证，HUB-CORE 一手设计件）

## 0. 总判
cisvr 的 QF-OS 雏形与我们独立建造的 URE/义务机是**同一抽象机的两套实现**（UNIFY-01 定理的第二次印证）；八件套中三件我们已有同构件（互相作证），五件带来真升级。

## 1. 互相作证（三件，趋同确认）
| cisvr 件 | 我们对应 | 趋同点 |
|---|---|---|
| 传送门协议（作业卡跨境执行） | W2 .enc 态迁移 + DIAL 胶囊 | 制备/密文/坍缩三步同构 |
| ZKP 三式（持权而不知值） | zkp-pat-check + 三层分离 | root P7 原话=我们的 K6 边界条款原型 |
| 指针旅行 | W4 胶囊回执（内容不过墙，摘要+hash 过） | "需要旅行的从来不是内容"=我们的蒸馏纪律 |

## 2. 真升级（五件，按接入优先级）

### U1 软纠缠对锚 → 双链互签（立即接，NMUST-03 §2 双核的现成实现）
cisvr：vci-root witness 每 6h 副签公链 checkpoint；任一侧篡改→双侧失配→报警。
**接入**：我们的双链（叙事链 usrm-outbox ⇄ 决策链 ure/chain.jsonl）增加**交叉副签**：sweeper 每 tick 把对侧 tip 写入本侧条目（KERNEL-02 §3 互引条款升级为副签协议）；四黄 R3 重放扩展为**双链交叉验证**（一侧被改，对侧副签即失配）。成本：oblig_tick/pareto_tick 各加 3 行；收益：双核互证从设计变为运转件。

### U2 信标起搏 → 义务因果驱动的联邦时钟（接，强化 §3 驱动）
cisvr：Quafu QRNG 信标链式时钟 + 高度点火 + qrand jitter 防预测；总则"闹钟只是兜底，事件/因果链才是驱动源"。
**接入**：我们的义务因果驱动（∇A）+ 事件驱动（dispatch）已立法；升级点：(a) cron 降格为兜底（现状：cron 是主时钟）——义务年龄阈值点火为主、cron 保底；(b) 联邦同步用信标高度而非墙钟（防 2026 漂移已踩过的坑）；(c) qrand jitter 防调度可预测（安全增益）。成本：oblig_tick 加点火条件评估；Quafu 信标有现役 poller 可挂。

### U3 break-glass override → GATE 升级（接，治理增强）
cisvr：白名单场景+双验（出席证明×角色证明）+动作集封顶+必上链+24h必审；"受治理时是资源，不受治理时是漏洞"。
**接入**：我们的 GATE 只有 binary halt。升级为**封顶 override 信道**：白名单（灾难恢复/链全断）+ 双验（HMAC+root 签封）+ 动作集封顶（只许 HALT/RESUME/直投 lobby）+ 每次上链（RPT.OVERRIDE）+ 24h 必审（自动生成审记义务）。成本：GATE 判读器扩展 + 一个 workflow。

### U4 折叠/展开 → HoloSense 审计压缩（接，Φ 场的全息化）
cisvr：等效路径束折叠 247→65（52.1%），"审计看代表，取证可展开"；directives-holo 三哈希摘要整个指令面。
**接入**：HoloSense Φ 场快照 + 折叠映射：联邦视图默认只发代表摘要（折叠态），取证时按展开映射还原——审计带宽降一半，完整性由展开映射的确定性保证。这也是"全息"的精确定义候选：**折叠映射 + 展开可逆 = 全息编解码**（回答 QFOS-Q1 #12）。
成本：oblig_monitor 视图加 fold/expand 双函数 + 映射入链。

### U5 多跳传态接力 → 跨业务线密文路由（排期接）
cisvr：ephemeral X25519 每跳换钥、内存解密、用后即焚；relaybox 转密封零落盘。
**接入**：我们的 .enc 是单跳（公仓⇄runner）。业务线链接入时（vinf/ucif2/qgl 影子参与推理链）需要多跳。排期 n4 后；先立法：任何多跳中继必须每跳换钥+内存限定+焚毁声明。

## 3. 对问题清单 QFOS-Q1 的自答（考古已答部分）
已答：#1（治理机=governor+kernel+witness 三证明者，对应我们 L3+机器+外部层）、#6（脉动=信标点火，cron 兜底——U2 采纳）、#8（审计=回执链+折叠，不落盘但可证——U4 采纳）、#10（override 双验+封顶——U3 采纳）、#12（全息=折叠/展开——U4 给定义）、#14（接力=每跳换钥——U5 立法）、#16（ZKP=持权不知值三式——互证）。
待 cisvr 答：#2/4/5（传态驱动细节）、#13（信息论保证陈述）、#18/19/20（接点与入库意愿）。

## 4. 升级实施登记（义务候选）
| 义务 | domain | 优先级 |
|---|---|---|
| o-xsign 双链交叉副签 | machine | P0（本批） |
| o-beacon-ignition 信标点火爆改 | machine | P1 |
| o-breakglass GATE 升级 | machine | P1 |
| o-foldexpand 视图折叠 | machine | P2 |
| o-multihop 接力立法 | machine | P2 |
| o-cisvr-answers 清单回签 | human(cisvr) | P1 |
