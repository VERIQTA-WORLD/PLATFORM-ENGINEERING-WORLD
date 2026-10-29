# Forking and teaching

Fork the repository and keep source attribution and license notices. Choose a path and assessment window before assigning work. Provide a Python 3.10+ environment for the core track. If learners lack container runtime access, keep the Kubernetes lab optional and assess the local model separately.

A useful session has three parts: explain the model, attempt the exercise before opening the worked reasoning, then compare evidence and failure behavior. Ask learners to predict a command result before running it. Pair review is effective when one learner runs the documented instructions in a fresh directory and the other records ambiguities.

For a four-session workshop, use discovery and the first local loop in session one; contracts, reconciliation and self-service in session two; policy, SLOs and restore in session three; a small capstone defense in session four. Longer cohorts can complete all phases and the advanced integration projects.

Assess artifacts using the capstone rubric. A correct explanation with fabricated execution evidence must not receive a pass. Accept a clearly labeled design when the lesson asks for design work. Do not require a production deployment to prove a local exercise. Teach the difference between a useful simulation and a verified production control.

For private classroom adaptation, replace only synthetic examples and keep real organizational data out of any public fork. Keep a changelog for modified contracts and templates. Re-run audit, tests and walkthrough after changes. Validate external integrations in the versions and environments you teach, since the Python CI does not execute those integrations.
