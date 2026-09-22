import test from 'node:test';
import assert from 'node:assert/strict';
import { styleDecision } from '../src/style-judge.js';

test('editorial disagreements do not become confident passes or failures', () => {
  const text = 'A paragraph under review.';
  assert.equal(styleDecision(text, 'defect', 'none').verdict, 'review');
  assert.equal(styleDecision(text, 'clean', 'P1').verdict, 'review');
  assert.equal(styleDecision(text, 'unclear', 'none').verdict, 'review');
  assert.throws(() => styleDecision(text, 'defect', 'P100'));
});
