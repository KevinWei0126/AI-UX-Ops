# design-system/

> 全盈+PAY 的設計系統規範（元件、模式、token）。

## 這裡放什麼？

- **元件**：按鈕、輸入框、卡片等可重用的 UI 元件
- **模式**：跨元件的設計模式（例如表單驗證、錯誤處理、空狀態）
- **Token**：色彩、字級、間距、圓角等基礎設計變數
- 視覺檔（Figma）放在 Figma，這裡是**規範文字版**，補充使用情境與例外

## 命名規則

- `ds-{類別}-{元件名}.md`
- 例如：
  - `ds-button-primary.md`
  - `ds-input-text.md`
  - `ds-pattern-form-validation.md`
  - `ds-token-color.md`

## 新增流程

1. 複製 `../_meta/templates/design-spec.template.md`
2. 填 Figma 連結（必填）
3. 寫清楚 "When to use" 與 "When NOT to use"
4. 在 `CHANGELOG.md` 加 Added 一筆
5. 執行 `bash ../scripts/generate_file_map.sh`

## 維護原則

- **改規範前先看 changelog 演進**——理解為什麼前一版這樣定，再決定是否改
- 元件規範變動的版本管理透過 changelog 處理（不要在檔名加 v2）
- 已被新元件取代的舊規範，標 `status: deprecated` 並在內文註明替代者，**保留檔案**
- 規範與 Figma 不一致時，**規範文字優先**（Figma 是視覺呈現，這裡是決策依據）
