# WEDGE · 张量网络工具链（tensor-net-01）· 桩 v0.1
2026-08-24 usrm 打桩 · 多纠缠四语跨域计算的计算内核

## 定位
张量网络 = 全息感知→全局计算→动态多维评估 的计算底座（缘起文档 §22）。
与四语链关系：TN 提供"语义场"的数值表示，四语链提供互证框架；两者在 L1/L2 层耦合。

## 接口契约
tn_contract(network_spec, budget) -> {result, contraction_path, cost}
tn_embed(knowledge_slice) -> tensor_field   # 知识谱系切片→张量场
tn_residual(field_a, field_b) -> scalar     # 场间残差→FINDING

## 嵌入点
T1 计算后端注册表：quimb/TensorNetwork/ITensor/tenpy/Cotengra（调研中 research/TN-toolchain.md）
T2 量子启发优化：Ising/退火/QAOA 模拟——对接 Quafu 线（quafu-poller 已在跑）与 QLV-VAULT
T3 语义计算：DisCoCat/lambeq 借范（张量语义）
T4 形式化接合：TN 性质的 SMT/LEAN 表达（与 ATP-lab、fourlang-01 E5 交汇）
T5 IPGSA/相变几何化：量子求解预研（开放研究，讨论室议题）

## 冒烟序列（未来 CI）
S1 pip 装 quimb，3 站点 MPS 缩并
S2 小 Ising 模型基态能量 vs 穷举对拍
S3 tn_residual 两快照场 → 非零残差触发 FINDING 落链

## 纪律
- CPU-only 优先，GPU 量子硬件走 Quafu 专线
- 大结果留私域 artifact，公域只载哈希+摘要
