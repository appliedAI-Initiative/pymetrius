import sys

from pylint.lint import Run
import anybadge

FAIL_THRESHOLD = 6

badge_thresholds = {
    7: 'orange',
    8: 'yellow',
    9: 'green'
}

results = Run(["src", "--max-line-length=120"], exit=False)

score = results.linter.stats['global_note']
# NOTE: we need to do this ourselves instead of using the --fail-under flag, since we want the badge
# to be produced if we are above the threshold and therefore have to use exit=False
if score < FAIL_THRESHOLD:
    sys.exit(f"Pylint failed: score is below threshold {FAIL_THRESHOLD}")

badge = anybadge.Badge('pylint', score, thresholds=badge_thresholds)
badge.write_badge('badges/pylint.svg', overwrite=True)
