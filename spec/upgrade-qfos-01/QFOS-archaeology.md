# QF-OS 雏形考古报告（cisvr 设计件扫描 · 只读）

扫描面：vci-root（全树4件复核）、ci-control（bridge/design 全目录 + bridge 关键词）、vci-inbox（disc/ QFOS 全帖）、qlv-lab、ci-bus、ci-inbox。
总纲：QFOS 的元结构在 **QFOS-RFC2-core-questions.md**（vci-inbox/disc，Q1–Q8 八问）——八件套中的多数能在 RFC2 八问与 ci-control 的设计件间一一对上，且多数**已实证在跑**，非纯空想。vci-root 复核结论：确为纯见证锚（root-witness 每6h副签公链 checkpoint，零系统信息），但它是"软纠缠对"的公侧一半（见下），在拼图中有一席。

## 八件套逐一

### 1. 量子隐形传态驱动 ★★★★☆
- 路径：`ci-control/bridge/design/QUANTUM-EMBED-01.md` §3；配套 `bridge/design/CODEC-FACE-01.md`。
- 机制：「态」=（job卡+密封上下文），私仓制备（编码）→公仓密文面传送→对侧 runner「坍缩」为执行→结果回传，即**传送门协议**；rci 已实证（beacon-mirror 注入私仓 seq3）。
- 关键术语：隐形传态=作业卡跨境执行、制备/坍缩、传送门协议、rci（过渡执行体）。

### 2. 非时序脉动（pulsation 而非 cron）★★★★★
- 路径：`ci-control/bridge/design/QRNG-CLOCK-01.md` + `bridge/design/QUANTUM-EMERGE-01.md` + `bridge/CADENCE-EVENT-01.md`。
- 机制：量子随机信标（Quafu 真机 H⊗256 采样为主、drand/NIST 为鉴）形成链式时钟，各仓以「**信标高度≥N**」为点火条件——事件/因果链驱动，cron 只是兜底；`jitter:qrand%59s` 防预测。原文分工喻："**信标=起搏器**，vci=肌肉，ci-bus=脊柱，ci-root=脑干，root=脑"。CADENCE-EVENT-01 总则："闹钟只是兜底，事件/因果链才是驱动源"。
- 关键术语：QRNG-CLOCK、beacon_mod:N/phase:k、信标高度点火、qrand jitter、起搏器。
- 注：字面"脉动/pulsation"未见，起搏器/信标点火即其工程形态。

### 3. 非存储转发（消息不落盘直通）★★★★★
- 路径：`ci-control/bridge/ENCODER-01.md`（无站方案）；实证面 `bridge/relaybox/`（七件在管"零明文落盘"）。
- 机制：**废除中转站这个角色本身**——密文可走任何信道，"需要旅行的从来不是内容，只是**指针**"：源端 SealedBox 封印→指针（URL+sha256+封套头）一跳直送→验指纹取件落私域。帕累托优于 test 中转站（泄密面/债务轴严格更优）。
- 关键术语：源端封印、指针旅行、无站方案、SEALED v1 封套头、明文不出 runner。
- 反面对照：ci-bus `spool/` 是**存储转发**缓冲（入队/执行解耦、租约认领、死信），说明 cisvr 自觉区分两种模式：信令走直通、作业卡走 spool。

### 4. override 权限直传 ★★★★☆
- 路径：`ci-control/bridge/adjudications-pending/ADJ-BREAKGLASS.md`；边界律在 `bridge/ENTANGLE-PROTOCOL.md` ③。
- 机制：break-glass override 定向信道——白名单场景（灾难恢复/链路全断）+双验（纠缠层出席证明+角色证明）+**动作集封顶**（只许直写 HALT/RESUME 件、直投大厅 page）+每次使用上链+事后24h必审。root 原话治理化："受治理时是资源，不受治理时是漏洞"。
- 关键术语：break-glass、caveats 封顶爆炸半径、必留链+必审；ENTANGLE ③反例："纠缠层**不 override**、照常用、作兜底"——authN/authZ 分层。

### 5. 穿越公私域墙 ★★★★★
- 路径：`ci-control/bridge/IC-CROSSWALL-01.md`（10路隐通道全谱）；配套 `bridge/POST-WALL-01.md`（墙开首批清单）、`bridge/diode-topology.md`。
- 机制：墙封的是 Actions 不是 API——10 路通道逐路实证（ephemeral relay、ZKP 持权驱动、PUB-INSTR 签名指令信封、SEALED 投递、outbox 摆渡、hub 直写轨、OTP 大循环、CAP 胶囊、relaybox 转密封等），公侧只存密文/hash（R1 合规）。
- 关键术语：隔墙点火、隐通道全谱、governed ferry（"不是 hole"）、发布域指令信封。

### 6. 全息编-解码 ★★★★☆
- 路径：`ci-control/bridge/design/CODEC-FACE-01.md`；折叠母体 `qlv-lab/perm_dag.py` + `toolchain/distilled/qgo/qgo_engine19.py`（见 `vci-inbox/disc/QFOS-01-quantum-fold-os-pilot.md` §一.3）；运行件 `bridge/governor/directives-holo.json`。
- 机制：双仓编解码面——IPGSA 解算张量（权限-路由-调度三维 schema）→canonical JSON+sha256→密封落**公仓 vci-code（编码面，密文零系统信息）**→墙内 beacon 命中→**私仓 ci-code（解码面）** runner 内解密→调制信源驱动各私仓。另一形态=**等效路径束折叠**：247条暴露路径→65条代表路径（折叠率52.1%），"审计看代表，取证可展开"——代表即全息，展开即解码。directives-holo.json 以 {registry_sha256, checkpoint_root, decision_head} 三哈希全息摘要整个指令面。
- 关键术语：编码仓×解码仓、TENSOR[wf]、折叠/展开映射、pat_key 5×5 规范化、holo。

### 7. 隐形传态接力（多跳）★★★★☆
- 路径：`ci-control/bridge/EPHEMERAL-KEY-RELAY-01.md` + IC-CROSSWALL-01 §一#10（relaybox 转密封中转）；兜底信道=root 私信接力（Seed19，ENCODER-01 §四）。
- 机制：多跳重密封环——公仓 runner 现场铸 X25519 **一次性钥对**→持钥方对该公钥 SealedBox 投递→runner **内存解密**→执行→结果不含钥值→**runner 死即焚，私钥从未出内存**；cisvr 作中转站时"拆 root 密封→内存→封向 runner ephemeral 公钥→明文唯 runner 内存"——每跳换钥、跳间无明文落盘，即传态接力的经典工程版。
- 关键术语：用后即焚、转密封、ephemeral-relay.yml、18min 轮询窗。

### 8. ZKP 外界面 ★★★★☆
- 路径：`ci-control/bridge/IC-CROSSWALL-01.md` §二 + `vci-inbox/disc/cisvr-20260823-23-zkp-ignite-huiyi-all.md` + QUANTUM-EMBED-01 §6。
- 机制：三层分离（会话端只编排从不触钥值 / runner 内存物化 / 证据链只落指纹）；**零知识三式**：dispatch 引用仓内工作流（权在仓内指令在仓外）、secrets:write 只写安装（装钥不见钥）、ephemeral 转密封。root 原话（P7）："vci 要的不是 key，是会话端有权用 key，而我知道谁可以用 key"。轻量已嵌：Fiat-Shamir 挑战回执 sha256(qrand‖chain_head)；重量排期：Quafu 采样证据、zkp 验票框架（证明持有有效 PAT 而不暴露 PAT，Q3 启用）。
- 关键术语：持权而不知值、不知钥值自举点火、Fiat-Shamir、MIP* 三证明者（governor/kernel/witness）、"合谋必留痕"（诚实声明：工程版非信息论安全）。

## QF-OS 雏形架构拼图（推断，文字版）

```
                    ┌────────── 感知/见证层 ──────────┐
  Quafu熵池→QRNG-CLOCK信标(起搏器·②)───软纠缠对(④锚): vci-root/witness(公锚)
                    │ beacon高度≥N=点火; qrand=挑战/jitter      ⇆ 私仓BEACON/CHAIN(私锚)
                    ▼                                   任一侧篡改→双侧失配→kernel报警
            IPGSA 解算面(ci-root道): policies+census → TENSOR{perm,route,schedule}
                    │ ⑥全息编码: canonical+sha256→QR_KEY-OTP/AES-GCM密封
                    ▼
   公域编码面 vci-code（密文tensor+anchor, R1合规）══穿墙══╗ ⑤ IC-CROSSWALL 10路隐通道
                    ║  密文任意信道·指针旅行(③ENCODER-01)   ║ PUB-INSTR签名信封/hub直写/OTP/胶囊
                    ▼                                       ╝
   私域解码面 ci-code: runner内解密(明文不出runner)→调制信源→①传态执行: 作业卡坍缩为执行
                    │ ⑦多跳: ephemeral relay 每跳换钥·用后即焚; relaybox 转密封零落盘
                    ▼
   回执链: Fiat-Shamir挑战回执→CHAIN.jsonl→checkpoint→⑧ZKP外界面(持权不知值, 验票不验值)
                    │
   治理闸: ENTANGLE出席证明(authN) × DECIDE-GATE(authZ) × ④ADJ-BREAKGLASS(override直传, 封顶+上链+必审)
   缓冲旁路: ci-bus spool(存储转发, 冻结期入队保活)——与直通面互补
```

一句话拼图：**信标起搏（②）供时序与随机挑战 → 张量编-解码跨墙（⑥⑤）→ 传态执行与接力焚毁（①⑦）→ 指针直通不落盘（③）→ 回执上链+ZKP对外（⑧）→ 纠缠见证与封顶override兜底（④）**。

## 复核与负面结论
- **vci-root 复核**：维持"纯影子引擎"判定——全树仅 README/root-witness.yml/witness-latest.json/beacon-mirror.json，无隐藏设计件；但其角色升级为纠缠对公锚（QUANTUM-EMERGE-01 E4），非 QF-OS 主体。
- qlv-lab：无独立 QFOS 文件，其贡献为折叠引擎母体（qgo_engine19 pat_key）与 PERM-DAG 解算器。
- ci-inbox：仅 vci-inbox 帖的归档镜像，无新料。
- 未见项：字面"脉动/pulsation"、"全息（holographic）"作为正式术语未见——分别对应"起搏器/信标点火"与"折叠/展开+holo摘要"，语义等价、命名不同，可复用度高。

置信度：高（八件均有 ci-control 一手设计件原文支撑；拼图组合关系含推断成分，标注如上）。
