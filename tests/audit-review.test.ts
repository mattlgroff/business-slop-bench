import test from 'node:test';
import assert from 'node:assert/strict';
import { hash } from '../src/core.js';
import { hasAssistantReview, hasCompleteDraft } from '../src/audit-review.js';

test('assistant review follows an identical imported artifact without crossing text, inputs or model identity', () => {
  const id = 'anthropic--claude-fable-5.1--pilot-client-email--house';
  const text = 'Please approve the scope and fee, subject to security clearance.';
  const inputHash = hash('frozen writer request');
  const reviews = [{ path: `runs/pilot-v11/${id}.md`, outputSha256: hash(text), writerInputHash: inputHash }];
  assert.equal(hasAssistantReview(reviews, id, text, inputHash), true);
  assert.equal(hasAssistantReview(reviews, id, text + ' Start tomorrow.', inputHash), false);
  assert.equal(hasAssistantReview(reviews, id, text, hash('changed writer request')), false);
  assert.equal(hasAssistantReview(reviews, id.replace('fable-5.1', 'opus-5'), text, inputHash), false);
  assert.equal(hasAssistantReview(reviews, id.replace('--house', '--default'), text, inputHash), false);
});

test('draft audit keeps empty and token-capped API successes out of completed drafts', () => {
  assert.equal(hasCompleteDraft({ text: '', finishReason: 'length' }), false);
  assert.equal(hasCompleteDraft({ text: 'Partial draft', finishReason: 'length' }), false);
  assert.equal(hasCompleteDraft({ text: '  ', finishReason: 'stop' }), false);
  assert.equal(hasCompleteDraft({ text: 'Finished draft.', finishReason: 'stop' }), true);
});
