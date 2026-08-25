# SPEC-GOAL-01 · Kimi /goal 范式勘察与义务机嵌入（v1.0）

2026-08-25 · usrm 编 · root 令：探索/善用 /goal——目标全生命周期管理，嵌入范式/系统

## §1 /goal 是什么（官方件实测情报）
- **Kimi Code CLI /goal**（MoonshotAI/kimi-code，GOAL.md 公开）：目标=「最终要达成什么状态」而非「下一步做什么」；生命周期四态 `active/paused/blocked/complete`；命令面 `/goal status|pause|resume|cancel|replace|next`（next=目标队列）；prompt 模式退出码 0=complete/3=blocked/6=paused
- **Kimi Work 桌面目标模式**：24h 连续循环、Agent 集群（至 300）、定时任务（cron 化目标）
- **好目标五要素**（官方 GOAL.md）：end state（什么必须为真）/ proof（可观察证据）/ boundaries（范围与禁区）/ loop（如何迭代）/ stop rule（何时停报）

## §2 关键设计决策与义务机的逐项同构（独立趋同=互相验证）
| /goal 设计 | 义务机对应 | 同构判定 |
|---|---|---|
| 四态生命周期 | 七态格（raised…legislated）的粗化投影 | ✅ 四态⊂七态（complete≈legislated，blocked≈挂起+L2，paused≈L0 挂起，active≈open） |
| **模型只能标 complete，不能 pause/resume**（防自我偷懒） | **N10 迁移必有据 + wontfix 须 L3 签封**——机器不得自我豁免 | ✅ 独立趋同的最强证据：两个团队各自推出"机器无自我宽免权" |
| 续跑检查链（goal on?active?零工具调用抑制?） | T-HALT 显式终态 + sweeper 心跳 | ✅ |
| 目标队列 /goal next（当前目标运行期间队列不可见） | FIFO 义务队列（最老优先，队列其余不影响当前清算） | ✅ |
| 预算 opt-in + 缓存 token 不计费 | I1 预算不变式（硬上限为法定，非默认） | ✅ |
| 好目标五要素 | 义务=⟨终态, 证据谓词, 边界(GATE/禁区), 迁移循环, 超时/wontfix⟩ | ✅ 五要素恰是义务 schema 的五个字段 |
**结论**：Kimi 官方的 /goal 是义务机在单人编程场景的工业实现；我们的义务机是 /goal 在联邦多智能体+证明场景的泛化。**趋同本身=两族独立证据支持该架构的正确性**（借范三级：不是抄，是互相作证）。

## §3 嵌入方案（/goal 经验→义务机升级）
1. **完成契约格式化**：义务 schema 吸收五要素——现有 o={id,src,state,evidence,opened} 增 {end_state,proof_pred,boundaries,stop_rule}（proof_pred 直接就是 N10 的 V 谓词句柄；boundaries 接 GATE 文件族；stop_rule 即 wontfix 条款）
2. **反自我偷懒立法强化**：机器只能以证据把义务推向 legislated；**pause/wontfix 永远需要人域签封**——/goal 的源码级决策（`update_goal can only mark complete`）成为我们 L3 条款的工业先例引用
3. **阻塞语义采用**：blocked=机器写"阻塞原因+解阻所需输入"短消息（我们现在只有挂起心跳；升级为：每次阶梯升级附阻塞结构体 {reason,unblock_needs}——o-root-rotate 即首例：unblock_needs="root App 侧注销会话"）
4. **队列不可见性**：当前清算中的义务独占 sweeper 注意力（已有：每轮≤1 清算），队列其余只在视图层可见——确认现役行为与此一致 ✅
5. **目标队列机**：/goal next 队列=我们的 deps 偏序排队（queued→frontier 的准入即队列推进）✅ 现役

## §4 反向输出（我们给 /goal 的）
义务机有而 /goal 无：证据链锚（N11）、正反互补证明（ATP）、跨仓联邦视图、义务因果自推进（∇A 驱动）、双队列人机分流。若 Kimi Code 开源社区接受，GOAL 联邦化是我们的潜在贡献点（贡献入库纪律：先内部跑稳一周期）。

## §5 饱和攻击开线登记
GO 令的全量全维度搜索突破：CHGS-01（CC 打底+KG+TN 缝合）首波；/goal 嵌入（本卷）为范式对齐波；后续波次按 DAG 排队。
