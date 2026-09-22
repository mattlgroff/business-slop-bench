import test from 'node:test';
import assert from 'node:assert/strict';
import { generationId, repeatSample } from '../src/core.js';

test('repeats cannot overwrite the primary or another sample', () => {
  const task = { id: 'readout' };
  const primary = generationId('meta/muse', task.id, 'house');
  assert.equal(primary, 'meta--muse--readout--house');
  assert.equal(new Set([primary, generationId('meta/muse', task.id, 'house', 2), generationId('meta/muse', task.id, 'house', 3)]).size, 3);
  assert.equal(repeatSample('2'), 2);
  for (const bad of [undefined, '', '1', '0', '-1', '2.5', '02', '2junk', 'Infinity']) assert.throws(() => repeatSample(bad));
});
