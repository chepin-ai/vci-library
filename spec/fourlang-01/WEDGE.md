# WEDGE · 四语链跨域计算工具链（fourlang-01）· 桩 v0.1
2026-08-24 usrm 打桩 · 未来嵌入/关联点 · 接口先行，实现后补

## 层定义
L0 NL 自然语言 ｜ L1 LEAN 形式语言 ｜ L2 代码 ｜ L3 链/哈希

## 接口契约（每条互译边一个函数型）
trans(src: Li, dst: Lj, payload, ctx) -> {artifact, proof, residual}
- proof：互译正确性证据（roundtrip 一致 / 机判 / Merkle 见证）
- residual：失配残差 —— **残差即 FINDING**（Δ-Base），非零即入研究队列

## 既有桩基
- 链/哈希锚定：usrm-outbox chain（prev/hash/hmac）——L3 已运行
- L1⇔L2 机判：ATP-lab（Z3/cvc5/Prover9/Mace4 @ vci-playground）——已运行
- 诊断-恢复模式目录：research/N1-fourlang.md P1-P12
- 借范调研：research/FL-toolchain.md（在研）

## 嵌入点（未来挂接）
E1 NL→LEAN：autoformalization 服务（供推者=P-B 会话端/P-A2 中心）
E2 LEAN→NL：LaTeX/证书渲染（leanblueprint 借范）
E3 代码→链：SLSA/in-toto 式来源证明，commit 即 CID
E4 链→NL：审计证书人类可读投影
E5 残差总线：各层 residual → FDI 式故障隔离矩阵（n1a 节点）

## 纪律
- 每条边的实现必须先过冒烟（CI 可跑）再接入 DAG
- 跨层信息不过公/私边界：L3 只载哈希，原文留私域
