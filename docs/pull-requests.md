# Pull requests and team workflow

Repository: https://github.com/mordecai12-cool/campusflow2

Integration branch: `feat/engineer-b-integration-and-checks`, authored under
Michael's account with explicit AI-assistance attribution. Original Mordecai
commits are preserved. A pull request will link this branch to main; its URL
will be recorded below after creation.

## Create a pull request yourself

1. Make your code and matching test changes on a feature branch.
2. Run the tests and inspect git diff.
3. Commit and push the branch under your own GitHub account.
4. Open the repository on GitHub and click **Compare & pull request**.
5. Set **base** to `main` and **compare** to your feature branch.
6. Describe the problem, resulting behavior, actual test results and AI assistance.
7. Click **Create pull request** and ask your partner to review it.
8. Fix review findings on the same branch; pushing updates the PR automatically.
9. Merge after genuine approval and successful checks.

For this branch, the comparison page is:
https://github.com/mordecai12-cool/campusflow2/compare/main...feat/engineer-b-integration-and-checks

To contribute a later change from a clean local clone:

```sh
git switch main
git pull --ff-only
git switch -c feat/your-change
# Implement application code and matching tests yourself.
python3 -m unittest discover -s tests -v
git diff --check
git add <the-files-you-changed>
git commit -m "Describe your actual change"
git push -u origin feat/your-change
```

## Real review and contribution evidence

Partner approval and cross-review are pending. Do not paste invented findings
or approvals. Record each person's actual PR, meaningful changes, tests and
learning evidence. An AI-generated commit is not proof of independent work.
