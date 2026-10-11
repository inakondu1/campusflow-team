# Pull requests and team workflow

Repository: https://github.com/mordecai12-cool/campusflow2

Integration branch: `feat/engineer-b-integration-and-checks`, authored under
Michael's account with explicit AI-assistance attribution. Original Mordecai
commits are preserved. Publication is currently blocked: GitHub returned 403, Resource not accessible
by integration, when creating this branch. The connected integration lists only
miikese's installation. No remote branch or PR has been created by this session.
The prepared title and body are in [pr-draft.md](pr-draft.md).

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

## Publish the finished local commits

On the computer containing this checkout, authenticate Git to GitHub using
your own account, then run:

```sh
cd /home/student/campusflow2
git switch feat/engineer-b-integration-and-checks
python3 -m unittest discover -s tests -v
git push -u origin feat/engineer-b-integration-and-checks
```

The shell checkout is separate from the original /home/student/campus project.
If using the portable Git bundle on another computer, clone campusflow2 first,
then fetch the feature branch from the bundle file:

```sh
git clone https://github.com/mordecai12-cool/campusflow2.git
cd campusflow2
git fetch /path/to/campusflow2-commits.bundle feat/engineer-b-integration-and-checks:feat/engineer-b-integration-and-checks
git switch feat/engineer-b-integration-and-checks
python3 -m unittest discover -s tests -v
git push -u origin feat/engineer-b-integration-and-checks
```

Replace /path/to with the actual download location. Once pushed, open the
comparison link above, click Create pull request, and use pr-draft.md.
The repository owner can alternatively enable the connected GitHub integration
for this repository and let the assistant complete publication and PR creation.
