# Contributing

Help make the course clearer, more correct and more reproducible. Useful contributions include a repaired walkthrough, a more precise explanation, a meaningful failure test or an additional original lesson.

Before opening a pull request, describe the user problem and the resulting behavior. For runnable changes include the commands and observations. For prose, check terminology against primary sources and verify local links. Keep examples fictional and public. Do not include private screenshots, credentials, copied course materials, unsupported ranking claims or invented test results.

Run:

```sh
python3 06-tools/01-audit.py
python3 06-tools/05-check-all.py
python3 06-tools/04-walkthrough.py
```

Use [the lesson template](08-templates/06-lesson.md). New lessons need prerequisites, a clear model, a follow-along exercise, expected observations, acceptance criteria, a failure drill, worked reasoning, a knowledge check and primary references. Update `02-course-catalog.json`, the numbered phase index and the course map. Update displayed counts if the catalog changes.

A test should demonstrate a meaningful behavior or boundary, not merely repeat a function’s implementation. Optional integrations need versioned execution evidence or a clear unverified label. Avoid adding dependencies to the core path without explaining the learner benefit.

By contributing, you agree to distribute your original code/assets under the repository’s MIT license and your original prose under CC BY 4.0. Identify any third-party material and its compatible terms. Do not contribute material you are not authorized to share.
