import test from 'node:test';
import assert from 'node:assert/strict';
import { paragraphs, groundingDecision } from '../src/grounding.js';

test('evidence anchors point to original text even with repeated paragraphs and blank lines', () => {
  const text = '  A claim.\n\n A second claim.\n\nA claim.  ';
  const p = paragraphs(text);
  assert.equal(p.length, 3);
  for (const item of p) assert.equal(text.slice(item.offset, item.offset + item.text.length), item.text);
  assert.equal(p[2].line, 5); assert.notEqual(p[0].offset, p[2].offset);
});

test('a grounding allegation needs real evidence and inconsistent judgments stay unresolved', () => {
  assert.equal(groundingDecision('A claim.', 'unsupported', 'P1').verdict, 'fail');
  assert.equal(groundingDecision('A claim.', 'unsupported', 'none').verdict, 'review');
  assert.equal(groundingDecision('A claim.', 'grounded', 'P1').verdict, 'review');
  assert.throws(() => groundingDecision('A claim.', 'unsupported', 'P9'));
  assert.equal(groundingDecision('', 'grounded', 'none').verdict, 'pass');
});
