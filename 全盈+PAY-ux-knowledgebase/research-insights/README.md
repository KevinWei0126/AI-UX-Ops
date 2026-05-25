# research-insights/

> 全盈+PAY 的研究洞察資料庫（訪談、問卷、Usability Test、數據分析）。

## 這裡放什麼？

- 每一份 `.md` 是一份**完整研究的關鍵發現摘要**（不是原始逐字稿）
- 原始材料（逐字稿、問卷檔）放在另外的雲端硬碟，這裡用連結指過去
- 一份 insight 檔可影響多份 persona、多份 design-spec

## 命名規則

- `r{年}-{月}-{流水號}-{主題}.md`
- 例如：`r2025-05-001-支付流程訪談.md`

## 新增流程

1. 複製 `../_meta/templates/insight.template.md`
2. id 用「研究**執行**月份」而非「整理完成月份」
3. 連結回對應的 personas、business-goals
4. 在 `CHANGELOG.md` 加 Added 一筆
5. 若此洞察推翻或更新了某 persona，務必同步更新 persona 並記 changelog
6. 執行 `bash ../scripts/generate_file_map.sh`

## 維護原則

- 每個 Finding 都要有「具體證據」——原文引言、行為觀察、數據
- 樣本量很小時要明示限制（避免被當成 N=1000 的鐵律）
- 與設計決策直接相關的洞察，請在 `design-system/` 的對應元件加 `related` 反向連結
