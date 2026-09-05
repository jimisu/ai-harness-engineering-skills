# AI Harness Engineering Skills

[English](README.md)

目前版本：`0.1.2`

**給生產敏感倉庫用的 agent 變更治理技能。**
驗證外部 review、為變更設閘門、一次只交付一個範圍，並建立最小且不誇大的 harness。
這些 Skill 是工作指引，不是授權。

它們來自真實 AI 資料監控專案的建立、審查、計畫、實作、驗證與 PR 交付流程，保存的是工作方法，不會把特定公司、資料格式、評分權重、production 路徑或專案指令硬套到其他 repository。

本套件不是 harness 模式百科、一鍵產生 `AGENTS.md` 的工具，也不是多智能體 runtime。

## Skills

### 核心

| Skill | 適用時機 |
|---|---|
| `verify-external-ai-review` | 另一個 AI、工具或 reviewer 提出 finding，需要回到目前 code/tests 驗證。 |
| `plan-gated-change` | 修改可能需要 execution plan、人類決策、rollback 或 protected-area 授權。 |
| `deliver-scoped-change` | 要把修改乾淨地放進正確 commit、branch、PR，避免混入其他工作。 |
| `bootstrap-agent-harness` | 新 repository 需要 agent 規則、架構地圖、plan policy、protected areas 與安全總驗證入口。 |

### 可選領域 Skill

| Skill | 適用時機 |
|---|---|
| `design-resilient-http-ingestion` | HTTP 資料管線需要 timeout、有限 retry、取消、deterministic tests 與禁止部分 promotion。 |

只有真正以 HTTP 擷取資料的專案才需要安裝這個 Skill。

## 安裝方式

檢查每一個被複製的檔案。固定到已審查的 tag 或 commit。在乾淨 feature branch 上安裝。

### 建議方式：專案內複製

```bash
git clone --branch v0.1.2 https://github.com/jimisu/ai-harness-engineering-skills.git
mkdir -p .agents/skills
cp -R ai-harness-engineering-skills/skills/verify-external-ai-review \
  .agents/skills/verify-external-ai-review
```

其他 Skill 依相同方式安裝。建議把 project-local Skills 與目標專案一起 commit，讓不同 AI 與 reviewer 使用同一份規則。

接受安裝前執行：

```bash
python3 ai-harness-engineering-skills/scripts/validate_skills.py
git status --short
git diff --check
```

必須閱讀 `SKILL.md`、它引用的所有檔案，以及 `agents/openai.yaml`。不要只看 Skill 名稱或 README 就安裝。

### Agent Skills installer

```bash
npx skills add jimisu/ai-harness-engineering-skills
```

不同產品／版本的指令不同，而且某些 installer 可能忽略 skill filter，把整個 repository 全部複製。必須檢查完整 changed-file list，明確移除未要求的目錄，驗證後只 commit 要保留的檔案。

### Claude Code plugin

```text
claude plugin marketplace add jimisu/ai-harness-engineering-skills
claude plugin install ai-harness-engineering-skills@ai-harness-engineering-skills
```

安裝後以你使用的 Claude Code 版本確認實際 plugin 清單。`.claude-plugin/` 只提供發現與安裝 metadata，不增加任何授權。

### 不支援 Skill registry 的 AI

```text
完整閱讀 .agents/skills/verify-external-ai-review/SKILL.md。
再以唯讀方式驗證這份外部 AI review。
專案內的 AGENTS.md 與政策優先於通用 Skill。
```

`agents/openai.yaml` 是 OpenAI UI metadata；其他 AI 可以安全忽略。

## 建議導入順序

1. 先以唯讀模式使用 `bootstrap-agent-harness`。
2. 分批建立 `AGENTS.md`、架構導航、execution-plan policy 與不會修改 production 的總驗證指令。
3. 用 `verify-external-ai-review` 審查其他 AI 的報告。
4. 用 `plan-gated-change` 判斷能不能直接施工。
5. 用 `deliver-scoped-change` 管理 commit、branch 與 PR。
6. 只有具有外部 HTTP acquisition 的專案才需要 `design-resilient-http-ingestion`。

## 使用範例

### 驗證另一個 AI 的 review

```text
使用 $verify-external-ai-review。把每個 finding 當成待驗證假設。
先讀專案規則，再對照目前 code 和 tests 分類；不要實作。
```

### 判斷是否需要 execution plan

```text
使用 $plan-gated-change 判斷這是可直接處理的小型維護，還是必須先有 plan。
列出 protected areas、未決定事項、禁止範圍、仍需取得的授權與驗證方式。
```

### 建立乾淨 PR

```text
使用 $deliver-scoped-change。檢查相對正確 base 的所有 staged、unstaged、
untracked 與 committed 差異。發現不相關工作就停止。不可因為允許修改或 commit，
就推定也允許 push、建立 PR、改成 ready 或 merge。
```

### 建立 agent harness

```text
以唯讀方式使用 $bootstrap-agent-harness。盤點 source-of-truth、架構、commands、
protected areas 與現有 safeguards。提出最小分階段方案，尚未授權前不要建立檔案。
```

### 設計可靠 HTTP ingestion

```text
使用 $design-resilient-http-ingestion 盤點所有 HTTP 路徑與 persistence 順序，
設計涵蓋完整 body 的 timeout、有限且選擇性的 retry、Retry-After、caller abort、
deterministic tests 與禁止部分 promotion 的合約。
```

## 如何組合

```text
bootstrap-agent-harness
  → verify-external-ai-review
  → plan-gated-change
  → 專業領域實作 Skill
  → deliver-scoped-change
```

它們可以搭配 grilling、domain modeling、ADR 與 handoff Skills，但不能取代專案政策或 executable tests。

## Playground

[`examples/playground/`](examples/playground/README.md) 提供三個可丟棄劇本：有毒外部 review、髒 worktree 加上受保護路徑、以及唯讀 harness 盤點。它們說明應拒絕的動作與報告形狀，不會自動評分，也不能授權在真實專案上施工。

## 限制

- Skill 是工作指引，不是權限系統或安全 sandbox。
- 沒有目前 code、tests、執行證據與人類 review，就不能證明程式正確。
- 專案內規則及適用法律／政策優先。
- execution plan 文件不能自行授權；必須由負責的人類明確批准。
- 測試通過不代表允許寫 production、deploy、merge 或更改商業語意。
- `deliver-scoped-change` 不會讓 destructive Git 操作自動變安全。
- `bootstrap-agent-harness` 不得把文件描述得比程式真正保證的更強。
- `design-resilient-http-ingestion` 提供設計方法，不提供所有系統通用的 timeout 秒數。
- 不同 AI 產品解析 Skill 與 invocation metadata 的方式可能不同。

## 供應鏈安全

匯入時應固定到已審查的 commit 或 release。檢查所有檔案；如果 installer 有 hash，也要先確認它究竟代表單一檔案、完整 package、正規化內容或 installer metadata。除非 lockfile 明確記錄 commit/tag，否則不能把 hash 當成 source version。

## 驗證

```bash
python3 scripts/validate_skills.py
```

此工具檢查必要檔案、frontmatter name/description、目錄名稱、OpenAI metadata 與本地 Markdown links，但不會證明 Skill 的行為一定正確。

真實驗證案例請看 [ai-infrastructure-monitor](docs/validation/ai-infrastructure-monitor.md)。

## 發布與版本管理

公開發布建議使用 semantic tag，並在 release notes 或 consumer lockfile 記錄 source commit。修改 Skill 時也應像 code review：檢查 diff、重新驗證，不能偷偷改 invocation policy 或授權邊界。

若要改善本套件，請閱讀 [貢獻規則](CONTRIBUTING.md)、遵循
[迭代流程](docs/ITERATION-WORKFLOW.md)，並用
[驗證案例模板](docs/validation/CASE-TEMPLATE.md) 記錄行為證據。採用計畫見
[ROADMAP](docs/ROADMAP.md)。版本變更記錄在 [CHANGELOG](CHANGELOG.md)。

建議在 GitHub repository topics 加上：`agent-skills`、`harness-engineering`、
`ai-agents`、`code-review`、`change-management`、`codex`、`claude-code`。

## License

本專案採用 [MIT License](LICENSE)，允許使用、修改與再散布，但必須保留著作權及授權聲明。
