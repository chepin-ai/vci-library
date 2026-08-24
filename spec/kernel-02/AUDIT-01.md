# AUDIT-01 · chepin-ai 联邦 URE 体系只读审计（2026-08-24）

范围：vci-library(spec/kit)、vci-usrm(ure/scripts/workflows/inbox/outbox)、vci-playground(atp/tn/kaggle/workflows)。三仓均公开（匿名 raw=200 实测）。证据经本地验算（链哈希逐条复算）与 API 实测（issue 看板）。

## A. 矛盾 / 冲突

| # | 位置 | 双方 | 严重度 |
|---|---|---|---|
| A1 | vci-usrm/scripts/ure_tick.py:126-132 vs pareto_tick.py:89-99；ure/chain.jsonl:1-5 vs 6-7 | 同一条链两种算法：旧式 hash=sha256(canon(entry))+hmac；新式 hash=sha256(prev+canon(entry)) 且无 hmac/state/action 字段。已复算：seq1-5 仅旧式可验、seq6-7 仅新式可验——单一验证器无法验全链 | 高 |
| A2 | vci-library STRAT-02:60、DUAL-01:52、LOOP-01:49、CONV-01:53,59 四处规定参数入 `ure/params.json` | 实现为 roadmap.json:289-299 `params` + pareto_tick.py:51-53 DEFAULT_PARAMS；ure/params.json 不存在；CONV-01 C4"params.json 静态校验"无机判对象 | 高 |
| A3 | PARETO-01:24（收益递减→π 衰减让位）vs STRAT-02:47 S-d（退役归档）vs pareto_tick.py:277-288（连续 2 轮 Δ<ε 即 retired） | 三处语义互斥；CONV-01 定理1 的 H1 停机证明依赖"退役"，PARETO-01 的"衰减"不满足其前提 | 中高 |
| A4 | pareto_tick.py:280 写 state="retired" vs 同文件:41 与 ure_tick.py:41 STATES 无 retired | set_issue_labels:208 对 retired 直接跳过 → 看板无 retired 泳道，退役节点投影丢失 | 中 |
| A5 | roadmap.json:201-207 frontier={n1,n2,n3,n5,n6} vs :146-150 n7 state=running | running 的 n7 不在 frontier/不在 prices(:307-313)，永不进臂集被调度（pareto_tick.py:258-264 仅以 frontier 为臂集）；queued 的 n2/n6 反占臂位。CONV-01 C3 的 |A_active| 口径与现实脱节 | 高 |
| A6 | roadmap n7=running vs GitHub issue #18 label=agent/queued（API 实测） | 看板投影失同步（n7/n8 的 issue #18/#19 今日已建，此前"无 issue"已过时，但标签未跟进） | 中 |
| A7 | PARETO-01:40、STRAT-02:58、RANDMIP-01:42 均写"ure_tick.py 实现/入规格" | 实际新建 pareto_tick.py，ure_tick.py 成死代码（ure-sweeper.yml:75-77 仅注释保留）；规格集体指向死文件 | 中 |
| A8 | roadmap budget.tick_score_delta=0.1(:7) vs chain seq3-5 n1 增量 0.3、手工分 n2/n6=0.25、n5=0.65（非 0.1 整数倍、无链条目） | score 双账：roadmap.score 由人工/证据改写，pareto_tick.py:153-155 的 u_i 只读链差分 → Whittle 统计系统性失真 | 中 |
| A9 | outbox/usrm-outbox.json(seq70-76) vs ure/chain.jsonl vs outbox/backfill/LOCAL-SEQ71-74.json | 双链三算法（outbox_append.py:34 为第三种 hash 式）；LOCAL 包与主链 seq71-74 同号不同文（平行双轨）；entry seq76 in_reply_to="seq84" 前向悬空 | 高 |
| A10 | vci-usrm/README.md:8 "零密钥…只持 GITHUB_TOKEN" + DIAL-01:6 "公仓不应绑 LLM key" | 实际 secrets：URE_APP_*/ATP_APP_*/CMD_AUTH/OTP_PHONE/AI_FULL_PAT/API_DEEPSEEK_KEY_1/Kaggle×2；agent-duty.yml:22 持 LLM key | 高 |
| A11 | sim/out.json pi_star=(β0, γ0.05)、PROOF-GUESS-01:28 vs roadmap.params β=0.5,γ=0.3 | 元递归自调（PARETO-01 §3）只活在 --simulate；live 参数静态不回灌 | 中 |
| A12 | STRAT-01:3 "research/STRAT-grounding.md"；fourlang WEDGE:15-16 research/N1-fourlang.md、FL-toolchain.md；tensor-net WEDGE:14 research/TN-toolchain.md | research/ 目录在仓中不存在（STRAT-grounding 实在 spec/strat-01/），四处路径断裂 | 低 |
| A13 | LOOP-01:52、KERNEL-01:73、REVP-01:53 三处"待 n9" | roadmap 无 n9 节点，悬空引用 | 低 |
| A14 | tensor-net WEDGE:21 "3 站点 MPS" vs tn-smoke.yml S1 n_sites=5 | 规格与冒烟参数不符 | 低 |
| A15 | 三仓 weave/status.json last_pulse=20260819 vs 各 pulse.log 尾 20260822 | status 内部字段自相矛盾（F2 愈合重建后未刷新 last_pulse） | 低 |

## B. 冗余 / 重复 / 混淆

| # | 位置 | 内容 |
|---|---|---|
| B1 | scripts/ure_tick.py（214 行全量死代码）vs pareto_tick.py | 新旧调度器并存，规格指向旧件（见 A7） |
| B2 | otp_gate_worker.py 三份异版：vci-usrm/scripts/（v3 issue-loop）、vci-usrm/workers/（T171 push 旧版）、vci-library/kit/usrm-01/（md5 三者互异） | 工蜂三源漂移，修复无法收敛 |
| B3 | 凭证四套：URE_APP_* 与 ATP_APP_* 互为 fallback（ure-sweeper.yml:36-54）、CI_OPS_APP_*（watchdog）、CI_OPS_HUB_KEY（bench-qlv）；铸 token 三种实现（手写 JWT×2、create-github-app-token@v1、@v2） | 密钥面×4、同功能代码×3 |
| B4 | outbox-publish.yml（GITHUB_TOKEN 直推、未 persist-credentials:false、未摘 extraheader）vs ure-sweeper.yml:90-93（App token+显式摘除） | 同仓两种 push 安全姿势 |
| B5 | line-producer.yml 三仓逐字节复刻（同 cron '11 */6'）；shadow-pulse/watchdog 三仓复制仅错峰分钟不同 | 模板未抽象，改动需三处同步 |
| B6 | chain 双键名 node/arm，pareto_tick.py:127 兼容读取 | 同一语义两个字段名，下游皆须兼容 |
| B7 | vci-usrm/zkp-pat-check.yml | 无 permissions 块；echo 引号未转义产出非法 JSON；"report to chain file" 实际只传 artifact 不回仓，名不符实 |
| B8 | OTP_PHONE 双处存放：secrets（各 otp workflow）+ repo Variables（kit/usrm-01/PATHS-ATLAS.md:15 自称"API 可读=自助收割"） | 同一 PII 两套口径 |
| B9 | N3-rules-formal.md:42-56 内嵌 LEAN 与 Rules.lean 逐字重复；Rules.lean:1 声称"sorry 待回灌"但全文无 sorry，:13 dagFrontier 未定义（不可编译）；Ev 枚举缺 escalate/retire/silent/hook/conflict/done（N3:9 已使用） | 双源漂移 + 骨架不可编译 + 词汇表不齐 |

## C. 缺口 / 缺陷 / 瓶颈

| # | 位置 | 内容 | 严重度 |
|---|---|---|---|
| C1 | STRAT-02 §1 T1-T4 放蜂触发器 | pareto_tick.py 全文无 release/蜂 判定——规格核心机制未实现 | 高 |
| C2 | STRAT-02 S-c/S-d 支配门禁 | probation 池只进不出（pareto_tick.py:291-301 仅 append）：无支配检验、无复活、无探针预算；今日已堆 12 条无消化路径 | 高 |
| C3 | roadmap deps 字段（n4←n3、n8←n3+n4、n1a←n1、n6←n1） | 两脚本均不读 deps：ure_tick.py:175 取 first queued、pareto_tick.py:262 只看 frontier → DAG 依赖约束形同虚设 | 高 |
| C4 | ure_tick.py:172 first-running 恒为 n1；pareto 臂集限 frontier → n7 饿死 | 新旧两路各自饥饿（与 A5 同源） | 中高 |
| C5 | pareto_tick.py:338-353 cascade 计数器 | try 块内仅浮点加法永不抛异常 → LOOP-01 §3 级联机构空转，cascade/cascade_log 恒空；CASCADE_K=2(:55) 硬编码而 LOOP-01:52 自承"k、θ_r 待 E7 标定" | 中 |
| C6 | vci-usrm/.github/workflows/watchdog.yml 监控名单 | 只盯 agent-duty/line-producer/shadow-pulse 三件旧 workflow；今日新建 ure-sweeper/ure-pareto/otp-gate/otp-issue-trigger/outbox-publish/quafu-poller 全在看门狗之外，跑红无报警 | 高 |
| C7 | 三仓 pulse.log 尾 20260822-04:xx，cron 声称 */6h | shadow-pulse 静默 ~48h 无人察觉；vci-library 连续 3 脉冲 "line not registered" 仍 verdict=ok（软失败掩盖） | 中高 |
| C8 | cron 撞车：ure-sweeper "23 */4" × atp-smoke "23 4 * * *" × bench-qlv "23 */6" 同刻叠加 GitHub 高载漂移 | 调度不确定性与分钟浪费 | 低 |
| C9 | otp-gate.yml artifact kimi-session retention 1 天 vs 同一 .kimi_session.json 被 git 提交永久留存 | 保留策略被自有提交通道绕行 | 中 |
| C10 | PROOF-GUESS-01:31 证据锚 "out.json @ commit 3b0e7702" | 以 commit 非内容哈希为锚，弱证据 | 低 |
| C11 | outbox_append.py:37 dtag 幂等仅查内存 entries，不含 backfill/chain_anchor 历史 | 42-69 区段存在重放窗口 | 低 |
| C12 | kaggle/mc-convergence/kernel-metadata.json:2 "chepin163net/..." | 163 邮箱前缀式个人标识入公仓 | 低 |

## D. 安全债务

1. **P0 手机号明文**：vci-usrm/inbox/otp_aftersend.png（公仓，1440×900 截图）清晰显示 +86 13902209204。违反自定立法"公面不含真人标识符"（BACKFILL #13 记录），且 kit/INDEX.md:7 告诫 F1 早已点名此通道"须限期整改"——预警未执行。通道=otp-issue-trigger.yml / otp-gate.yml 的 `git add -A inbox/ → push`（配合 otp_gate_worker.py:126"发码后必截图"）。
2. **P0 活凭证入公仓**：inbox/.kimi_session.json 含 Kimi 个人账号 refresh_token（JWT，exp≈2026-11）+ 全量 cookies/localStorage。任何人可匿名拉取并接管会话。与 D1 同通道；artifact 1 天保留形同虚设。
3. **P0 无授权闸的公仓触发面**：otp-issue-trigger.yml 对 `issues:opened` 无 author_association 过滤——任何 GitHub 用户开 "[SENDCODE]"/"[OTP] xxxxxx" 标题 issue 即可触发对 OTP_PHONE 的发码轰炸与登录尝试，并驱动 contents:write 推送。
4. **P1 公仓绑私钥违立法**：AI_FULL_PAT（classic PAT 满 scopes，PATHS-ATLAS A5 自述）、API_DEEPSEEK_KEY_1 存于公仓 secrets，直接违反 DIAL-01 §0 与 README 铁律；zkp-pat-check.yml 无 permissions 声明。
5. **P1 最小权限失守**：URE/ATP App installation 实测覆盖 21 仓，sweeper 单 token 可写全邦；ure-sweeper.yml:14-15 声明 `contents: read` 与 :92-93 实际 x-access-token 推送形成"声明-实际"两张皮。
6. **P2 凭证驻留**：outbox-publish.yml 未关 persist-credentials，GITHUB_TOKEN 留 .git/config；bench-qlv /tmp/hub.pem 有删除前窗口；kaggle legacy 模式 kaggle.json 落盘（runner 临时）。
7. **P2 时效债**：三仓脉冲静默 48h（C7）；60 天计划停用仅靠 vci-usrm ure/.keepalive 单点，library/playground 无独立 keepalive；zkp-result artifact 未设 retention；watchdog 用 @v1 旧 action。

## E. 修复优先级

**P0（阻断性）**：① D1/D2——从公仓历史清除手机号截图与 .kimi_session.json，吊销/轮换 Kimi 会话，inbox/ 改 .gitignore+artifacts-only（落实 F1）；② D3——issue 触发加 author 闸；③ A1——统一链算法、为 seq6-7 补 hmac 或显式分段标注；④ A5/A9——frontier 纳入口径修正（running 节点必入臂集）、双链 seq 命名空间拆分、悬空 seq84 对表。
**P1（一致性）**：A2（落 ure/params.json 或改四处规格）；A3/A4（retired 入状态机与看板）；A7/B1（规格改指 pareto_tick.py，删 ure_tick.py）；A10/D4（LLM key/满权 PAT 迁出公仓或修订铁律）；C1-C3（T1-T4 触发器、支配门禁消化 probation、deps 生效）；C6（watchdog 扩面至全部新 workflow）；D5（App 权限缩仓）。
**P2（整洁）**：A8 score 单账化；A11 sim→live 参数回灌；A12-A15/B9 路径断裂、n9 悬空、S1 站点数、status 刷新、Rules.lean 可编译化；B2 工蜂三源收敛；B3/B4 凭证与 push 姿势统一；B5 三仓模板抽象；C7 静默告警；C8 cron 错峰；C11 dtag 全史查重。

（只读审计，未改任何文件；证据：本地复算链哈希、匿名 raw 探测、issues API 实测。）
