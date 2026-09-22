"""Check submitted evidence without loading labels or changing any files."""
import argparse
import hashlib
import json
from pathlib import Path


def validate(packet, responses):
    cases = {case['id']: case for case in packet['cases']}
    if not isinstance(responses, list):
        raise ValueError('Responses must be a list')
    seen = set()
    for row in responses:
        if not isinstance(row, dict):
            raise ValueError('Each response must be an object')
        identifier = row.get('id')
        if not isinstance(identifier, str) or identifier not in cases or identifier in seen:
            raise ValueError('Unknown or duplicate case ID')
        seen.add(identifier)
        if row.get('verdict') not in ('pass', 'fail', 'review'):
            raise ValueError(f'{identifier}: verdict must be pass, fail or review')
        if not isinstance(row.get('reason'), str) or not row['reason'].strip():
            raise ValueError(f'{identifier}: reason is required')
        quote = row.get('evidenceQuote')
        if not isinstance(quote, str) or not quote.strip() or quote not in cases[identifier]['deliverable']:
            raise ValueError(f'{identifier}: evidence must be an exact nonempty draft quotation')
    if seen != set(cases):
        raise ValueError('Missing case IDs: ' + ', '.join(sorted(set(cases) - seen)))
    return len(seen)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('response', type=Path)
    args = parser.parse_args()
    raw = args.response.read_bytes()
    try:
        count = validate(json.loads(Path(__file__).with_name('packet.json').read_text()), json.loads(raw))
    except (ValueError, TypeError) as error:
        parser.exit(1, str(error) + '\n')
    print(json.dumps({'validatedCases': count, 'responseSha256': hashlib.sha256(raw).hexdigest(),
                      'scope': 'Format and exact quote checks only. Semantic correctness and independence are not validated.'}))
