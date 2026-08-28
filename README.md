<!-- CLASSIFY: L0 -->
# vci-library —— HUB-LIB 之公域 CI 影子引擎（SHADOW-CI-01 矩阵 · 知识谱系）

**意图**：公域影子：不间断解析/梳理/归纳/耦合 TOP5 公开成果（outbox/weave/导出报告），构建并维护知识谱系及其上的运算/推演/验证/米田嵌入

## 铁律
1. 本仓只载 L0/L1 公开面内容（CLASSIFY-01）；私域内容一律不走本仓。
2. 零密钥、零私仓凭证——本仓 Actions 只持 GITHUB_TOKEN（本仓 contents:write）。
3. 消费面 = 各线会话公开发布的 outbox/weave 件与 HUB-CORE 公域注册表；产出 = weave/pulse/ 摘要与本仓提交史（即哈希链）。
4. 与 warm side（chepin-bi/ci-warm 私域镜像）并列常设：warm 管私域防灾，本仓管公域语义投影。

## 机制
- `shadow-pulse`：事件驱动（push engine/** · repository_dispatch · 手动），脉冲读取 HUB-CORE/bridge/outboxes.json 注册表中对应对线 outbox，快照入 weave/pulse/ 并追加 pulse.log（自提交成链）。
- 引擎升级经 provision 车道（HUB-CORE/provision/vci/vci-library/）幂等下发。
