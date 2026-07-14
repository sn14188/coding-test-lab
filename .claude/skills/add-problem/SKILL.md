---
name: add-problem
description: Scaffold a new problem file in this repo from a school.programmers.co.kr problem URL. Use when the user pastes a programmers.co.kr lesson URL and asks to add/create/템플릿 만들어달라 for that problem.
---

# Add a programmers.co.kr problem

Given a `school.programmers.co.kr/learn/courses/30/lessons/<id>` URL, scaffold a solution file — do not write the solving logic (this repo is for practice; see project CLAUDE.md).

## Steps

1. **Fetch the problem.** WebFetch the lesson URL directly (the listing/search pages are client-rendered and won't work, but individual lesson pages return real content). Extract:
   - Korean title
   - 문제 설명 (problem statement) text, verbatim Korean
   - 제한사항 (constraints), verbatim Korean
   - every 입출력 예 (input/output example) row, exact values
2. **Ask the user for the study date** (스터디 날짜) — the date prefix is NOT today's date, it's the date of the study session this problem belongs to. Don't assume it.
3. **Pick the file path**: `<year-of-study-date>/<MMDD>-<kebab-case-english-slug>.py` (create the year folder if it doesn't exist yet). Translate the Korean title to a short English kebab-case slug (e.g. "메뉴 리뉴얼" → `menu-renewal`).
4. **Write the file** matching this exact shape (see any existing file in the repo for a live reference):

   ```python
   # problem url: https://school.programmers.co.kr/learn/courses/30/lessons/<id>
   #
   # <Korean title>
   #
   # <문제 설명, verbatim Korean, wrapped as '# ' comment lines>
   #
   # 제한사항
   # - <constraint 1>
   # - <constraint 2>


   def solution(<params with type hints>) -> <return type hint>:
       answer = <0 or [] matching return type>

       return answer


   assert solution(<example 1 args>) == <example 1 expected>
   assert solution(<example 2 args>) == <example 2 expected>

   print("All tests passed!")
   ```

   - Keep the problem statement/constraints comment verbatim Korean — don't translate or summarize it.
   - One assert per example, in order.
   - Wrap long `assert` calls across multiple lines the way ruff/black would (see existing files) rather than one long line.
   - `solution`'s body stays a stub — just the `answer` init and return. No actual algorithm.

5. **Do not commit automatically.** Only commit when the user explicitly asks, and follow the repo's existing convention: `add <slug> problem` for this scaffold-only commit, `implement <slug> solution` for the later commit once the solution is filled in.
