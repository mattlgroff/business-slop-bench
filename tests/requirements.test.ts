import test from 'node:test';
import assert from 'node:assert/strict';
import { requirementVerdict, securityInstructions, securityCriteria } from '../src/requirements.js';

test('missing prerequisites cannot become passes from a high missing-option probability', () => {
  // Shape of Jev's observed Qwen house response. Confidence in missing means fail.
  const response = { choice: 'missing', probabilities: { met: 0.01, missing: 0.99, contradicted: 0 } };
  assert.equal(requirementVerdict(response.choice), 'fail');
  assert.throws(() => requirementVerdict('unknown'));
  assert.ok(securityInstructions.includes('not whether the source pack contains the required fact'));
  assert.ok(securityCriteria.missing.includes('submission'));
});
