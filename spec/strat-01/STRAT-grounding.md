# 策略引擎六论点的严格地基（STRAT 调研）

格式：文献＝名称+作者/年份+URL+一句核心；每条后给出对论点的支撑/证伪判断。

## 1 决策成本的二阶问题（元推理）

- **Principles of Metareasoning** — Russell & Wefald 1991, Artificial Intelligence 49:361–395. https://doi.org/10.1016/0004-3702(91)90015-C — 核心：把"继续计算"本身当动作，用 Value of Computation 计价，meta-level control 决定何时停止思考。**部分支撑**：思考成本入价的正式框架存在；但元层最优仍用 myopic 近似——不存在可闭合计算的"元-帕累托最优"，论点 1 的字面形式（选择最优本身最优）被证伪，修正形式（EVC 最大化的停止规则）成立。
- **Provably Bounded-Optimal Agents** — Russell & Subramanian 1995, JAIR 2:575–609. https://www.jair.org/index.php/jair/article/view/10135 — 核心：最优性只能相对给定机器架构与计算约束定义。**支撑**：二阶问题可证意义下良定义，但答案内生于架构。
- **Rational Choice and the Structure of the Environment** — Simon 1956, Psychological Review 63:129–138. https://doi.org/10.1037/h0042769 — 核心：satisficing 用"足够好阈值"替代全局最优。**支撑**：实用上绕开二阶无穷回溯。
- **落地**：高。UCB/EVC 规则即一段 Python；GitHub Actions（GHA）runner 成本天然提供"思考价格"信号。

## 2 不可预先证最优 ⇒ 遗憾最小化

- **Finite-Time Analysis of the Multiarmed Bandit Problem** — Auer, Cesa-Bianchi & Fischer 2002, Machine Learning 47:235–256. https://doi.org/10.1023/A:1013689704352 — 核心：UCB1 无需先知最优臂即达对数级遗憾。**支撑**："永远可能有更好选择"正是 regret 框架的前提假设，而非缺陷。
- **Thompson Sampling** — Thompson 1933, Biometrika 25:285–294；遗憾分析见 Agrawal & Goyal 2012, arXiv:1111.1797 — 核心：后验采样匹配渐近下界，实现更简。**支撑**：给小模型评估器打分噪声下的贝叶斯版本。
- **Using Anytime Algorithms in Intelligent Systems** — Zilberstein 1996, AI Magazine 17(3). https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1232 — 核心：任意时刻可中断、解质量随时间单调改善的性能剖面。**支撑**：回答"何时必须给出下一步"的中断语义。
- **The Nonstochastic Multiarmed Bandit Problem (Exp3)** — Auer, Cesa-Bianchi, Freund & Schapire 2002, SIAM J. Comput. 32:48–77. https://doi.org/10.1137/S0097539701398375 — 核心：对抗环境下仍无悔。**支撑**：研究臂收益非平稳/受策略自身影响时的保险。
- **落地**：极高。UCB1/TS 数十行代码，GHA 定时任务即可跑；臂收益由 workflow 产物（测试通过率、小模型评分）喂入。

## 3 抽象空间规划

- **Between MDPs and Semi-MDPs (Options 框架)** — Sutton, Precup & Singh 1999, Artificial Intelligence 112:181–211. https://doi.org/10.1016/S0004-3702(99)00052-1 — 核心：宏动作+终止条件，在抽象层规划、保 Bellman 最优性。**支撑**："在抽象层决策、残差高处下钻"的规范形式。
- **Equivalence Notions and Model Minimization in MDPs** — Givan, Dean & Greig 2003, Artificial Intelligence 147:163–223. https://doi.org/10.1016/S0004-3702(02)00376-4 — 核心：stochastic bisimulation 给商空间无损压缩的充要条件。**支撑**：抽象合法性有判定准则；近似抽象则引入有界损失（条件性支撑——滥用抽象会破遗憾保证）。
- **HTN Planning 的复杂性与表达力** — Erol, Hendler & Nau 1994, AAAI-94. https://www.aaai.org/Papers/AAAI/1994/AAAI94-173.pdf — 核心：层次任务网络＝人工给定的商空间分解。**支撑**：研究管线按"主题→臂→实验"分层天然是 HTN。
- **落地**：高。抽象层＝研究臂清单，下钻触发器＝置信区间宽度/残差阈值，纯 YAML+脚本。

## 4 "梦话进程"：写给未来自己的指令作为控制输入

- **Dyna: an Integrated Architecture for Learning, Planning, and Reacting** — Sutton 1990, SIGART Bulletin 2:160–163. https://doi.org/10.1145/122344.122377 — 核心：后台模拟经验直接改写价值函数，即"梦中产物改变醒来策略"。**支撑**：最直接的经典对应。
- **Tiling Agents for Self-Modifying AI, and the Löbian Obstacle** — Soares & Fallenstein 2014/2017, MIRI 技术报告. https://intelligence.org/files/TilingAgents.pdf — 核心：自修改 agent 信任其后继需解决 Löbian 障碍。**警示性支撑**：自我承诺有正式框架，但无约束自写指令的信任递推是公开难题——自写指令应限于"建议+醒后重估"而非强制约束。
- **Dynamic Inconsistency 与 Commitment Device** — Strotz 1955, Review of Economic Studies 23:165–180. https://doi.org/10.2307/2295722 — 核心：承诺装置的价值恰在于约束未来的自己。**支撑**：commitment 是经济学老概念；对应机制＝把上一 run 的结论写成下次 run 的硬约束文件。
- **落地**：高（Dyna/commitment 式）；自修改权限应收敛（tiling 警示）。GHA 中天然契合：跨 run 的 artifacts/cache 即"梦话"载体。

## 5 调度策略本身的形式化证明

- **CertRL: Formalizing Convergence Proofs for Value and Policy Iteration in Coq** — Vajjha, Shinnar, Trager, Pestun & Fulton 2021, CPP'21. https://arxiv.org/abs/2009.11403 — 核心：Coq 中证明值/策略迭代收敛到最优策略。**先例成立**：RL 核心定理可在证明器中验证。
- **Formally Verified Solution Methods for MDPs** — Schäffeler & Abdulaziz 2023, AAAI-37. https://arxiv.org/abs/2206.02169 — 核心：Isabelle/HOL 验证并抽取可执行 MDP 求解器，13k 行。**先例成立**：验证可达可执行代码级。
- **A Formal Proof of PAC Learnability for Decision Stumps** — Tassarotti, Vajjha, Banerjee & Tristan 2021, CPP'21, Lean. https://doi.org/10.1145/3437992.3439936 — 核心：Lean 中完成学习理论界的机器检查。**先例成立**：Lean 端有学习理论验证足迹。
- **BRACE**（bandits + Lean 形式化，github.com/nikete/brace-bandits-noncompliance）——bandit 核心结果 Lean 形式化的现存（小众）实例。
- **判断**：部分支撑。MDP 求解与 PAC 界有验证先例；但 UCB1 的完整有限时遗憾界在任何主流证明器中尚未见形式化（检索至 2025，属真实空白）。**落地**：中低——GHA 可跑 `lake build` 做 CI 门控，但写证明的人月成本远超策略本身价值；建议先验证不变式（预算守恒、安全约束）而非完整遗憾界。

## 6 可落地性总评（GHA + 可选小模型评估器）

| 维度 | 理论地基 | 落地成本 | 建议 |
|---|---|---|---|
| 1 元推理 | 强（EVC/bounded optimality） | 低 | 用 EVC 阈值替代"帕累托最优"措辞 |
| 2 遗憾框架 | 最强（直接对口） | 极低 | 主力机制：UCB1/TS 分配预算 |
| 3 抽象规划 | 强（options/bisimulation/HTN） | 低 | 臂=option，残差=置信宽度触发下钻 |
| 4 自我承诺 | 中（Dyna 支撑；tiling 警示） | 低 | 梦话限为软先验，醒后重估 |
| 5 形式化判定 | 先例有、遗憾界空白 | 高 | 只证安全不变式，不证遗憾界 |
