# SPEC-STRAT-02 · 放蜂触发形式化 + 动态最优/不动点自指 + 新可能性进场策略（v1.0）

2026-08-24 · usrm 立论 · root 四问 · 承接 STRAT-01（六论）与 PARETO-01（决策规则）

## 1. 何时放蜂：触发器形式化

蜂 = 探索仪器（深研/广搜/借范/碰撞的具现）。放蜂不是节奏问题，是**触发逻辑**。定义四类触发谓词（全部代码判定，无量纲阈值入参数表）：

$$\textbf{T1 新臂无知：}\quad \mathsf{enter}(a) \wedge \mathrm{prior}\text{-}\sigma(a) > \theta_1 \Rightarrow \mathsf{release}(\text{广搜蜂})$$
新节点入 frontier 且先验不确定度超阈 → 放广搜蜂建立基线（对应"新可能性进场"的首次响应）

$$\textbf{T2 高残差方差：}\quad \sigma(a) > \theta_2 \Rightarrow \mathsf{release}(\text{锦标赛蜂群}\times k)$$
臂内分歧=发现信号（STRAT-01 多智能体唯一触发器的蜂化）；k∈[3,5]（R2：宽度实证区间）

$$\textbf{T3 新颖性残差：}\quad \mathsf{capsule}(x) \wedge \mathrm{sim}(x,\mathsf{KB}) < \theta_3 \Rightarrow \mathsf{release}(\text{深研蜂沿残差})$$
胶囊与知识库语义距离大（r≠0 ⇒ FINDING，Δ-Base）→ 残差方向放深研蜂

$$\textbf{T4 预算盈余：}\quad \forall a\in A_{\text{active}}:\ \Delta u(a) < \varepsilon \wedge B_{\text{free}} > \theta_4 \Rightarrow \mathsf{release}(\text{借范蜂})$$
全体现役臂收益递减（饱和）且有闲预算 → 放借范蜂开新维度（防原地打转，Nature 2024 崩塌警示的主动版）

**不放蜂条件（负触发）**：N1 预算紧绷（B(t)<θ₅）只供推不放蜂；N2 同臂已有在飞蜂（去重，蜂号入链）；N3 human-gate 存在时冻蜂。

## 2. 帕累托均衡 → 动态最优

静态：ω* ∈ 前沿流形上一点。动态：把状态 s=（各臂 score/σ/历史、预算、知识库哈希）纳入，策略 π(s) 满足**前沿约束 Bellman 方程**：
$$V(s)=\max_{a}\;[\,r(s,a)+\gamma V(\delta(s,a))\,]\quad \text{s.t.}\quad a\in\mathrm{Frontier}(s)$$
**影子价格 πᵢ 的严格正名 = Whittle index**（restless bandits，Whittle 1988）：每臂的"激活价格"，预算约束下选指数最高臂——我们 v0 的 π 公式正是 Whittle 指数的可计算启发式。这把 SPEC-PARETO-01 §2 从启发升级为有经典理论地位的策略。

## 3. 帕累托递归 → 不动点（自指的严格化）

引擎用自身产出调自身权重：策略映射 $\mathcal{F}:\Pi\to\Pi$。**自指的不动点存在性需要收缩性**：
$$\|\mathcal{F}(\pi)-\mathcal{F}(\pi')\| \le \rho\|\pi-\pi'\|,\ \rho<1 \;\Rightarrow\; \exists!\ \pi^*=\mathcal{F}(\pi^*)\ (\text{Banach})$$
- 收缩从哪来：折扣 γ<1 + 权重更新步长衰减（η_t∝1/t）+ 回放评估的平滑（EMA）。**无折扣/大步长 ⇒ 不收缩 ⇒ 自指失稳**（策略震荡/漂移）。
- 警示接线（STRAT-01 论题3）：无约束自指信任递推是公开难题（MIRI tiling）⇒ 引擎只允许**参数级自修改**（β,γ,ε,θ 数值），**结构级自修改（改代码/改目标）必须 human-gate**。不动点只在参数流形上求。
- 工程判据：相邻 epoch 参数变化 <ε_param 且遗憾界曲线斜率下降 ⇒ 宣称"临不动点"（可观测、可检验，M5/M6）。

## 4. 新可能性不断进场的策略（正式回答）

臂到达是**流**不是**集**。策略四件套：

**S-a 常驻探索预算**：γ·B(t) 永久保留给新臂（root 令第 4 条的制度化）——永不归零，防止"全 exploit 锁死"。

**S-b 试用池（廉价探针）**：新臂不直接进现役集，先入试用池，分配**最小探测预算**（一次快模型评分 或 一只蜂的基线广搜）→ 得到先验 π̂。依据：infinitely-many-armed bandits（Berry & Fristedt 1979-85）：无限臂流下仍可有界遗憾，前提是探测成本受控。

**S-c 帕累托门禁（支配剪枝）**：试用臂与现役臂做支配检验——被严格支配（全目标皆劣）者**不入现役**，归档入发现卡片库（Voyager 式，情境变化可召回）；非支配者入现役。现役集大小 |A_active| ≤ K_max 硬顶——否则每 tick 评估成本无界增长，直接违反论题 0（元成本爆炸）。

**S-d 退役与复活**：现役臂连续 n 轮 Δu<ε → 退役归档（非删除）；环境漂移（新胶囊/新 O）使归档臂的 π̂ 重估超阈 → 复活回试用池。

```
臂生命周期： 进场 → 试用池(廉价探针) → 支配门禁 → 现役(Whittle指数排序)
              ↑________________________________↓
                 退役归档 ⇄ 漂移复活（卡片库召回）
```

**与论题 1 的一致性**：臂流模型下遗憾界依然可界（Berry-Fristedt + mortal/restless bandits 文献）——"永远可能有更好选择进场"不再破坏策略，而是**被预算结构和门禁吸收**。

## 5. 落地映射
- n7 实现规格更新：pareto_tick.py（ure_tick.py 已归档）增加 触发器 T1-T4 判定 + Whittle 式排序 + 试用池/门禁状态（roadmap.json 增加 `probation`/`retired` 两池字段）
- 放蜂的执行通道 = DIAL 胶囊（cap=explore，供推者 P-B 会话端优先）
- 参数表（β,γ,ε,θ₁..₅,K_max）入 `roadmap.json.params`，epoch 回放自调（§3 收缩条件内）

## 6. 开放项
Q4 Whittle 指数在本臂型（可检索、可放蜂、有胶囊回执）下的精确可计算性——restless 且带外部信息注入，文献位置待考（候选 n8 姊妹节点）
Q5 试用池探针的最小成本界：多便宜才算"廉价"（与论题 0 停思规则耦合）
