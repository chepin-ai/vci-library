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
