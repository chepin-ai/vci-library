# N3 · N-Must / M-Code / Δ-Base 形式化公式集 v0.1

2026-08-24 · usrm 起草 · 规则必形式（机器 LEAN ⇔ 人类 LaTeX 双层）

## 0. 符号与语义基座

设系统迹 $\tau = e_0 e_1 e_2\dots$（事件流），$S$ 为状态集，$\square$=恒有（always），$\lozenge$=终将（eventually），$\xrightarrow{\mathsf{lead}}$=领先于（A 发生则 B 必在后发生），$\mathcal{H}(x)$=x 的哈希锚定（L3 层）。

事件类（小写谓词）：$\mathsf{report}$（首报）· $\mathsf{track}$（跟进）· $\mathsf{close}$（闭环）· $\mathsf{build}$（建立）· $\mathsf{enable}$（启用）· $\mathsf{order}$（指令）· $\mathsf{respond}$（响应）· $\mathsf{iterate}$（迭代）· $\mathsf{verify}$（验效）· $\mathsf{feedback}$（反馈）· $\mathsf{silent}_a$（主体 a 静默）· $\mathsf{hook}$（勾稽/挂钩）· $\mathsf{conflict}$（冲缺）· $\mathsf{decide}$（决断）

## 1. N-Must（八必 · 时序链式公理）

$$\textbf{N1 首报必跟进：}\quad \square\big(\mathsf{report}(x) \xrightarrow{\mathsf{lead}} \mathsf{track}(x)\big)$$
$$\textbf{N2 跟进必闭环：}\quad \square\big(\mathsf{track}(x) \xrightarrow{\mathsf{lead}} \mathsf{close}(x) \vee \mathsf{escalate}(x)\big)$$
$$\textbf{N3 建立必启用：}\quad \square\big(\mathsf{build}(m) \xrightarrow{\mathsf{lead}} \mathsf{enable}(m)\big)\ \wedge\ \neg\mathsf{enable}(m) \Rightarrow \mathsf{retire}(m)$$
$$\textbf{N4 指令必响应：}\quad \square\big(\mathsf{order}(c) \xrightarrow{\mathsf{lead}} \mathsf{respond}(c)\big)$$
$$\textbf{N5 响应必迭代：}\quad \square\big(\mathsf{respond}(c) \wedge \neg\mathsf{done}(c) \xrightarrow{\mathsf{lead}} \mathsf{iterate}(c)\big)$$
$$\textbf{N6 迭代必验效：}\quad \square\big(\mathsf{iterate}(c) \xrightarrow{\mathsf{lead}} \mathsf{verify}(c)\big)$$
$$\textbf{N7 行动必反馈：}\quad \square\big(\mathsf{act}(c) \xrightarrow{\mathsf{lead}} \mathsf{feedback}(c)\big)$$
$$\textbf{N8 链式传递（元规则）：}\quad \text{N1..N7 构成 } \mathsf{report}\to\mathsf{track}\to\mathsf{close}\text{ 与 }\mathsf{order}\to\mathsf{respond}\to\mathsf{iterate}\to\mathsf{verify}\to\mathsf{feedback} \text{ 两条不可断链}$$

> 推论（缘起文档 §65）：认领必交付 $\mathsf{claim}(x)\to\lozenge\mathsf{deliver}(x)$ 可吸收 N1/N2/N4-N7 为单条强式。

## 2. M-Code（七原则 · 状态/迁移公理）

$$\textbf{M1 迁移必考：}\quad \mathsf{transition}(s,s') \Rightarrow \mathsf{examined}(s,s')\quad[\text{考=考古溯源+关联勾稽+前瞻推三步}]$$
$$\textbf{M2 静默必勾：}\quad \square\big(\mathsf{silent}(a) \Rightarrow \mathsf{guardian}(a)\ \mathsf{resident}\big)\ \wedge\ \mathsf{wakeable}(a)$$
$$\textbf{M3 未尽必钩：}\quad \mathsf{open}(x) \xrightarrow{\mathsf{lead}} \exists y:\ \mathsf{hook}(x,y)\ \mathsf{until}\ \mathsf{closed}(x)\vee\mathsf{transferred}(x)$$
$$\textbf{M4 冲缺必米田：}\quad \mathsf{conflict}(a,b) \Rightarrow \exists \mathcal{Y}:\ \mathcal{Y}(a)\cong\mathsf{Hom}(-,a)\ \text{且}\ \mathsf{embed}(\mathcal{Y}(a),\mathcal{Y}(b))\ \text{（米田嵌入归约至可共识）}$$
$$\textbf{M5 决断必检验：}\quad \square\big(\mathsf{decide}(d) \xrightarrow{\mathsf{lead}} \mathsf{test}(d)\big)$$
$$\textbf{M6 检验必反复：}\quad \mathsf{test}(d) \Rightarrow \mathsf{multimethod}(d)\quad[\text{圆心-半径法}\vee\text{包络线法}\vee\text{上下界两边夹}]$$
$$\textbf{M7 规则必形式：}\quad \forall r\in\mathsf{Rules}:\ \mathsf{formal}(r)_{\mathrm{LEAN}} \wedge \mathsf{render}(r)_{\mathrm{LaTeX}}$$

## 3. Δ-Base（三基操 · 残差动力学）

$$\textbf{Δ1 反逆找等价：}\quad \mathsf{inv}(f)\ \mathsf{seek}\ \cong:\quad f\circ f^{-1}\simeq\mathsf{id}\ \text{于某范畴}$$
$$\textbf{Δ2 等价必打破：}\quad a\cong b \Rightarrow \mathsf{break}:\ a\not\cong b\ \text{沿新维度}\ d\ \text{（对称破缺产新信息）}$$
$$\textbf{Δ3 残差即 FINDING：}\quad r = \mathsf{observed}-\mathsf{expected};\quad r\neq 0 \Rightarrow \mathsf{FINDING}(r)\ \mathsf{enters}\ \mathsf{DAG}$$

## 4. LEAN 4 骨架（机判层 · 双表达纪律 M7 自检）

```lean
-- spec/rules-formal-01/Rules.lean （骨架，sorry 待 ATP-lab 回灌）
inductive Ev | report | track | close | build | enable | order
  | respond | iterate | verify | feedback | act | decide | test
def Trace := List (Ev × Nat)          -- 事件 × 时刻
def LeadsTo (a b : Ev) (τ : Trace) : Prop :=
  ∀ i, (a, i) ∈ τ → ∃ j, (b, j) ∈ τ ∧ j > i
def Always (P : Trace → Prop) : Prop := ∀ τ, P τ

def N1 : Prop := Always fun τ => ∀ x, LeadsTo .report .track τ
def N4 : Prop := Always fun τ => ∀ c, LeadsTo .order .respond τ
def M5 : Prop := Always fun τ => ∀ d, LeadsTo .decide .test τ
-- Δ3：残差非零 → DAG 新增节点
def Delta3 (obs exp : Int) : Prop := obs - exp ≠ 0 → ∃ n, n ∈ dagFrontier
```

## 5. CI-OS 执行点映射（规则→机制，已运行处标 ✅）

| 公式 | 执行机制 | 状态 |
|---|---|---|
| N1-N2 | 链 append + issue 状态机（done 不可逆） | ✅ URE-U0 |
| N3 | wedge 冒烟准入制（不冒烟不接入） | ✅ fourlang/tensor-net |
| N4-N6 | OTP/QR/胶囊 全环实测惯例 | ✅ 本轮回合 |
| N7 | 首报必跟进 → 本报告制度 | ✅ |
| M2 | sweeper 即 guardian；keepalive 防 60 天停用 | ✅ |
| M5-M6 | ZKP 作业 / ATP-lab 四引擎对拍 / neal vs 穷举对拍 | ✅ |
| M7 | 本文档双层表达 + LEAN 骨架 | 🟡 骨架待回灌 |
| Δ3 | residual→FINDING→DAG（n1a 为首例） | ✅ |
| M1/M3/M4 | 迁移考古/未尽挂钩/米田归约 | 🟡 依赖 U2 递归层 |

## 6. 开放形式化问题（喂讨论室）
Q1 八必链的可满足性：是否存在迹 τ 使 N1-N8 全真而系统死锁？（ATP-lab 可机判有限模型）
Q2 M4 的米田嵌入在有限范畴上的可计算版本（小范畴 C-set，借 Catlab 思想但纯 Python）
Q3 Δ2"打破等价"的最小破缺度量：破缺量与信息增益的关系式
