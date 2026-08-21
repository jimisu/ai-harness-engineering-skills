# Delivery checklist

## Before checkpoint

- Correct repository, branch, and base identified.
- Worktree ownership resolved.
- Authorized paths listed exactly.
- Full diff reviewed.
- Tests and completion checks passed or blockers recorded.
- Protected and production paths compared.

## Before push

- Commit contains only authorized files.
- Feature branch is based on the intended base.
- No unrelated commits are included.
- Normal push is sufficient.
- Push authority is explicit.

## Before PR creation or update

- Existing matching PR searched.
- Base and head resolved exactly.
- Draft/ready state authorized.
- Body states purpose, scope, exclusions, tests, data impact, and known limitations.

## Final verification

- Local and remote head match.
- Tracking ahead/behind is expected.
- Changed-file list and commit count match scope.
- PR is open and has the intended draft state.
- Worktree is clean or preserved changes are reported.
- No merge, deployment, production write, force push, or history rewrite occurred unless authorized.
