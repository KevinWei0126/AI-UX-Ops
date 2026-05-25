# personas/

> 全盈+PAY 的使用者輪廓資料庫。

## 這裡放什麼？

- 每一份 `.md` 是一個 persona 的完整描述
- Persona 必須**有研究依據**，不是憑空假想（依據要寫在 frontmatter 的 `source_research`）

## 命名規則

- `p{流水號}-{名稱}.md`
- 例如：`p001-小資族行動支付者.md`、`p002-中高齡支付使用者.md`

## 新增流程

1. 複製 `../_meta/templates/persona.template.md`
2. 取下一個流水號（看 INDEX.md 或 file_map.md）
3. 填完 frontmatter（特別注意 `status` 預設 `draft`，被研究驗證後才升 `validated`）
4. 在 `CHANGELOG.md` 加 Added 一筆
5. 在 `../_meta/INDEX.md` 對應表格加一列
6. 執行 `bash ../scripts/generate_file_map.sh`

## 維護原則

- 一份 persona 只描述**一種**使用者類型，不要把多種類型塞進同一份
- 痛點與目標要具體（避免「希望好用」這種空話）
- 每次根據新研究更新時，務必更新 `last_updated` 並在 changelog 記 Changed
