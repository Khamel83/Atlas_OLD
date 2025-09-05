#!/usr/bin/env python3
# Calculate actual processing costs

# Model specs
cost_per_1m_tokens = 0.05  # $0.05 per 1M tokens
cost_per_1k_tokens = cost_per_1m_tokens / 1000  # $0.00005 per 1K tokens

print('=== COST ANALYSIS ===')
print(f'Model: Gemini 2.5 Flash Lite - ${cost_per_1m_tokens}/1M tokens')
print(f'100 items processed with 5 workloads each = 500 operations')

# Workload token averages from README
workloads = {
    'tags': 60,
    'summary': 150, 
    'socratic': 250,
    'patterns': 250,
    'recommendations': 250
}

total_tokens_per_item = sum(workloads.values())
print(f'\nAverage tokens per item (all 5 workloads): {total_tokens_per_item}')

# 100 items actually processed
total_tokens_100_items = total_tokens_per_item * 100
cost_100_items = (total_tokens_100_items / 1000) * cost_per_1k_tokens
print(f'Total tokens for 100 items: {total_tokens_100_items:,}')
print(f'Total cost for 100 items: ${cost_100_items:.6f}')

# Full database projection
total_items = 5475
total_tokens_all = total_tokens_per_item * total_items
cost_all = (total_tokens_all / 1000) * cost_per_1k_tokens
print(f'\n=== FULL DATABASE PROJECTION ===')
print(f'Total items in database: {total_items:,}')
print(f'Total tokens needed: {total_tokens_all:,}')
print(f'Total cost estimate: ${cost_all:.2f}')
print(f'Processing time estimate: {total_items/6.9:.1f} minutes ({total_items/6.9/60:.1f} hours)')