import { basename } from 'node:path';
import { hash } from './core.js';

type AssistantReview = { path: string; outputSha256: string; writerInputHash: string };

// A review follows identical text and inputs for the same model/task/condition,
// even when the collector copies that artifact into a later run directory.
export function hasAssistantReview(reviews: AssistantReview[], id: string, text: string, inputHash: string): boolean {
  const outputHash = hash(text);
  return reviews.some(review => basename(review.path) === `${id}.md`
    && review.outputSha256 === outputHash
    && review.writerInputHash === inputHash);
}

export function hasCompleteDraft(record: { text?: string; finishReason?: string }): boolean {
  return Boolean(record.text?.trim()) && record.finishReason !== 'length';
}
