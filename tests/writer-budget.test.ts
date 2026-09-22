import test from 'node:test';
import assert from 'node:assert/strict';
import { catalogOutputReservation, hash, prompt, writerInput, type Task } from '../src/core.js';

test('catalog spending reservation never adds a generation token cap; historical hashes remain reproducible', () => {
  const task: Task = { id: 'test', family: 'email', brief: 'Request approval.', facts: { fee: '$30,000' }, maxWords: 180, checks: [] };
  const input = writerInput(task, 'default', '', 'low');
  assert.equal(Object.hasOwn(input, 'maxOutputTokens'), false);
  assert.equal(catalogOutputReservation({ max_tokens: 512000 }), 512000);
  for (const max_tokens of [undefined, 0, -1, Infinity, 1.5]) {
    assert.throws(() => catalogOutputReservation({ max_tokens }));
  }
  assert.equal(hash(writerInput(task, 'default', '', 'low', 4096)),
    hash({ prompt: prompt(task, 'default', ''), reasoning: 'low', maxOutputTokens: 4096 }));
});
