# Repository Sense

## Place in the identity architecture

Tecnocrat is the digital entity; Jesus is its human origin; AIOS is part of its
body. The authenticated repository catalog is the first sensory cell: it gives
Tecnocrat a current, structured view of the repositories it owns. Its complete
output stays inside the private AIOS repository.

This sensor reports observable GitHub facts. It does not infer identity, quality,
or activity beyond the fields returned by GitHub.

## Daily signal path

1. `scripts/vps/repository_sense.sh` is prepared for a daily 17:17 UTC VPS cron
   run. The script and crontab entry still need deployment to the VPS.
2. `ai/cells/repository_sense` verifies the GitHub account and reads every page
   of its owned-repository inventory with an authenticated token.
3. The complete catalog is atomically written to
   `.aios/senses/repository_catalog.json` in the private AIOS repository.
4. Once installed, the VPS job commits each new observation to the private AIOS
   repository.
5. The API exposes a public-only projection at `/api/repositories`, cached for
   one hour. Its Vercel Cron request is configured for 03:17 UTC and becomes
   active with the production deployment.

## Signal boundary

The private AIOS catalog contains public and private repositories owned by
`Tecnocrat`, including forks. It records repository identity, description,
visibility, language, topics, timestamps, activity counts, archive/fork state,
and license metadata. Its output is kept in a private repository.

The API response contains only public repositories. Private repositories are
filtered before the response is returned, so the public face can describe the
visible portfolio without exposing private repository names or metadata.

This boundary keeps the complete sensory record separate from its public
projection. Any later surface consuming the private catalog must apply an
explicit exposure policy before publishing data.

## Consumers and growth

The catalog is a stable JSON input for the profile README, portfolio, and later
identity summaries. Those consumers can be built from the same refreshed signal
instead of maintaining separate hand-written repository lists.

Future sensory cells can add distinct signals, such as repository source
structure, releases, or current work. Each should keep source, observation time,
scope, and exposure level alongside its data.
