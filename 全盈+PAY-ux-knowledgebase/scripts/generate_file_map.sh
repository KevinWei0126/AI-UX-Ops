#!/usr/bin/env bash
# generate_file_map.sh
#
# 自動掃描 quanying-pay-ux 知識庫所有 md 檔，
# 解析每個檔案的 frontmatter（id / title / status / last_updated / tags），
# 產生 _meta/file_map.md。
#
# 使用方式（在 skill 根目錄執行）：
#   bash scripts/generate_file_map.sh
#
# 此腳本不依賴 Python，純 bash + 標準工具，可在 macOS / Linux 執行。

set -euo pipefail

# 找到 skill 根目錄（這個腳本的上一層）
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT="$ROOT_DIR/_meta/file_map.md"
NOW="$(date '+%Y-%m-%d %H:%M:%S')"

# 從 frontmatter 取單一欄位（取等號或冒號後的值，去掉前後空白）
extract_field() {
  local file="$1"
  local field="$2"
  # 只看前 30 行（frontmatter 應該都在這範圍內）
  awk -v key="$field" '
    /^---$/ { count++; if (count==2) exit; next }
    count==1 {
      # 比對 "key: value" 格式
      if ($0 ~ "^"key":") {
        sub("^"key":[[:space:]]*", "", $0)
        # 去除可能的引號
        gsub(/^["'"'"']|["'"'"']$/, "", $0)
        print $0
        exit
      }
    }
  ' "$file"
}

# 開始寫 file_map.md
{
  cat <<EOF
# 檔案地圖（File Map）· 自動產生

> ⚠️ **此檔案由 \`scripts/generate_file_map.sh\` 自動產生，請勿手動編輯。**
>
> 執行方式：
> \`\`\`bash
> bash scripts/generate_file_map.sh
> \`\`\`

**最後產生時間**：$NOW

---

## 用途

- 列出知識庫所有 md 檔的完整路徑、id、標題、狀態、最後更新時間
- 當 \`INDEX.md\` 沒涵蓋到、或你懷疑 \`INDEX.md\` 過期，來這查
- grep 此檔可以快速定位檔案位置：
  \`\`\`bash
  grep -n "支付" _meta/file_map.md
  \`\`\`

---

EOF

  # 依資料夾分組輸出
  for dir in personas research-insights design-system product-context business-goals; do
    if [ -d "$ROOT_DIR/$dir" ]; then
      echo ""
      echo "## 📁 \`$dir/\`"
      echo ""
      echo "| 檔案路徑 | ID | 標題 | 狀態 | 最後更新 | 標籤 |"
      echo "|---|---|---|---|---|---|"

      # 找出該資料夾下所有 md 檔（排除 CHANGELOG.md 與 README.md）
      found_any=0
      while IFS= read -r -d '' file; do
        basename_file="$(basename "$file")"
        # 跳過 CHANGELOG 與 README
        if [ "$basename_file" = "CHANGELOG.md" ] || [ "$basename_file" = "README.md" ]; then
          continue
        fi

        rel_path="${file#$ROOT_DIR/}"
        id="$(extract_field "$file" "id")"
        title="$(extract_field "$file" "title")"
        status="$(extract_field "$file" "status")"
        last_updated="$(extract_field "$file" "last_updated")"
        tags="$(extract_field "$file" "tags")"

        # 預設值
        [ -z "$id" ] && id="(無 id)"
        [ -z "$title" ] && title="(無標題)"
        [ -z "$status" ] && status="(無狀態)"
        [ -z "$last_updated" ] && last_updated="(無日期)"
        [ -z "$tags" ] && tags="-"

        echo "| \`$rel_path\` | $id | $title | $status | $last_updated | $tags |"
        found_any=1
      done < <(find "$ROOT_DIR/$dir" -maxdepth 1 -type f -name "*.md" -print0 | sort -z)

      if [ "$found_any" = "0" ]; then
        echo "| _(此分區尚未有檔案)_ | | | | | |"
      fi
    fi
  done

  # 額外區塊：列出所有 status=draft 與 status=deprecated 的檔案（需要關注的）
  echo ""
  echo "---"
  echo ""
  echo "## ⚠️ 需要關注的檔案"
  echo ""
  echo "### Status: \`draft\`（尚未驗證，引用時要小心）"
  echo ""
  draft_count=0
  while IFS= read -r file; do
    rel_path="${file#$ROOT_DIR/}"
    title="$(extract_field "$file" "title")"
    echo "- \`$rel_path\` — $title"
    draft_count=$((draft_count+1))
  done < <(grep -rln "^status: draft" "$ROOT_DIR" --include="*.md" --exclude-dir="_meta" --exclude-dir="scripts" 2>/dev/null || true)
  [ "$draft_count" = "0" ] && echo "_(無)_"

  echo ""
  echo "### Status: \`deprecated\`（已淘汰，保留歷史）"
  echo ""
  dep_count=0
  while IFS= read -r file; do
    rel_path="${file#$ROOT_DIR/}"
    title="$(extract_field "$file" "title")"
    echo "- \`$rel_path\` — $title"
    dep_count=$((dep_count+1))
  done < <(grep -rln "^status: deprecated" "$ROOT_DIR" --include="*.md" --exclude-dir="_meta" --exclude-dir="scripts" 2>/dev/null || true)
  [ "$dep_count" = "0" ] && echo "_(無)_"

  echo ""
  echo "### 超過 180 天未更新的檔案（建議 review）"
  echo ""
  stale_count=0
  cutoff_date=$(date -d "180 days ago" '+%Y-%m-%d' 2>/dev/null || date -v-180d '+%Y-%m-%d' 2>/dev/null || echo "1970-01-01")
  for dir in personas research-insights design-system product-context business-goals; do
    [ ! -d "$ROOT_DIR/$dir" ] && continue
    while IFS= read -r -d '' file; do
      basename_file="$(basename "$file")"
      [ "$basename_file" = "CHANGELOG.md" ] && continue
      [ "$basename_file" = "README.md" ] && continue
      last_updated="$(extract_field "$file" "last_updated")"
      [ -z "$last_updated" ] && continue
      # 字串比較即可，因為都是 YYYY-MM-DD 格式
      if [[ "$last_updated" < "$cutoff_date" ]]; then
        rel_path="${file#$ROOT_DIR/}"
        title="$(extract_field "$file" "title")"
        echo "- \`$rel_path\` — $title（last_updated: $last_updated）"
        stale_count=$((stale_count+1))
      fi
    done < <(find "$ROOT_DIR/$dir" -maxdepth 1 -type f -name "*.md" -print0 | sort -z)
  done
  [ "$stale_count" = "0" ] && echo "_(無)_"

} > "$OUTPUT"

echo "✅ file_map.md 已更新：$OUTPUT"
echo "   產生時間：$NOW"
