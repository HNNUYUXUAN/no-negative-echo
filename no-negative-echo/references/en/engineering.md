# Engineering

EN-1 Locate the abstraction, data flow, interface or state source producing the failure using reproducible observations and actual contracts. Establish the working baseline and existing user changes.

EN-2 Produce a complete correct implementation at the source of the defect so the erroneous path naturally disappears. Choose the simplest complete solution satisfying current requirements.

EN-3 Each added branch, retry, compatibility layer, state or switch must serve an independent real requirement, supported contract or external failure model. Existing tests and documentation are evidence; tests written for a new patch alone do not establish its necessity.

EN-4 Preserve required input validation, security boundaries and promised compatibility. When cause is uncertain, gather evidence that distinguishes causes. Use temporary emergency measures only when the task requires them and their limits are explicit.

EN-5 Align code, configuration, documentation and comments so the current implementation stands on its own. Comments explain current intent and constraints; commits and PRs describe current behavior and relevant verification.

EN-6 Verify the original failing scenario and affected valid behavior. Scale checks to risk; changes to prose cannot substitute for implementation, and unrelated tests cannot substitute for real acceptance.
