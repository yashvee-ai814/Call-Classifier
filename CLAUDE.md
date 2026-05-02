## Git Identity & Commit Rules

- Commit author is always **Yashvee** `<yashvee814@gmail.com>`
- Before the very first commit in any repo run:
  ```bash
  git config user.name "Yashvee"
  git config user.email "yashvee814@gmail.com"
  ```
- **NEVER add `Co-Authored-By:` lines** to any commit message — not for Claude, not for anyone
- Use feature branches for all new features: `feature/<short-name>`
- Push feature branches to origin and open a GitHub PR to merge into `main`
- Initial commit on `main` should contain only backend + infra files
- Commit frontend files on a `feature/frontend` branch
- Commit backend files on a `feature/backend` branch
- Commit messages: one short subject line, blank line, then a brief body — no trailers

---