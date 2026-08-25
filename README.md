# Anki decks

Flashcard decks maintained in a live Anki collection and published
here, one folder per deck. Each folder holds the deck two ways: an
`.apkg` you import into Anki with File, then Import, and a `.csv` with
plain front and back columns, which is the file to read without Anki
and the file git diffs when cards change.

Every deck is written from documentation and daily use, and each card
is checked for current truth before it is published, with the check
date in the deck's section below.

| Deck | Cards | Scope |
|---|---|---|
| [powershell](powershell/) | 133 | PowerShell from the basics through scripting, checked current for PowerShell 7 in August 2026 |
| [python](python/) | 125 | Python fundamentals with a security slant, written from a PowerShell background, checked current in August 2026 |
| [kql](kql/) | 118 | Kusto Query Language for logs and hunting, from operators through time series, checked current in August 2026 |
| [bicep](bicep/) | 50 | Bicep from the language through pipelines and deployment stacks, with the Terraform contrasts, checked current in August 2026 |
| [cybersecurity](cybersecurity/) | 184 | Security fundamentals across network, cloud, application, and governance, backup and recovery included, checked current in August 2026 |
| [aws-scs-c03](aws-scs-c03/) | 426 | AWS Certified Security Specialty (SCS-C03), service facts through the C03 additions, checked current in August 2026 |

More subjects land here one at a time.

## PowerShell

The pipeline and its objects, variables, arrays and hashtables,
functions and advanced functions, error handling, modules, remoting
over WinRM and SSH, jobs and runspaces, parallelism in PowerShell 7,
and script security. Where Windows PowerShell 5.1 differs from
PowerShell 7, the card says so.

## Python

The language from types through comprehensions, functions, exceptions,
files, and the standard library a security engineer leans on: hashlib,
ipaddress, subprocess and its shell gotcha, logging, json, re. Most
cards carry a parenthetical mapping the concept to its PowerShell
equivalent, because the deck was written while crossing from one
language to the other, and that bridge is the fastest way over for
anyone making the same crossing.

## KQL

The query language behind Azure Monitor, Log Analytics, and Microsoft
Sentinel: the core operators, joins and their hints, dynamic data and
JSON parsing, time series with make-series, and the query shapes
security work leans on, failed logons, spikes, correlation across
tables. Cards state what exists in the language and name what does
not, because half of writing good KQL is knowing which SQL habit has
no equivalent here.

## Bicep

The language itself, parameters through modules and decorators, then
the operational half most decks skip: .bicepparam files, deployment
scopes, what-if against live Azure, the BicepDeploy pipeline task,
and deployment stacks with deny settings as the successor to
Blueprints. Cards contrast with Terraform where the models genuinely
differ, state above all.

## Cybersecurity

The broad fundamentals deck: the CIA triad through zero trust, network
controls and their attacks, web vulnerabilities and their defenses,
cloud posture, identity models, incident response, governance and the
major compliance frameworks, and a backup and recovery section from
the 3-2-1 rule through immutability and restore testing.

## AWS Security Specialty (SCS-C03)

The deep deck: logging and monitoring internals (CloudTrail event
types, CloudWatch, Athena, VPC Flow Logs and what they miss), network
security (endpoints, PrivateLink, Transit Gateway, NACL and security
group behavior), edge protection (CloudFront, WAF, Shield), identity
(policies, boundaries, STS, Identity Center, Cognito), encryption
(KMS, envelope encryption, the SSE variants, CloudHSM), incident
response, and the SCS-C03 additions: Verified Access, Security Lake
and OCSF, resource control policies, and declarative policies. Facts
only, no practice questions; the exam names appear because the deck
tracks that exam's scope.

## Updating

Decks are exported from the collection with
[scripts/export.py](scripts/export.py). Corrections are welcome: open
an issue naming the deck, the card front, and what is wrong with the
back.

## If these help

Thanks for reading this far. If a deck saves you study time, the
other repositories on [my profile](https://github.com/tltaylor1) may
be worth a look too, and a star on the ones you use helps other
people find them.

## License

[CC BY 4.0](LICENSE). Use it, adapt it, credit it.
