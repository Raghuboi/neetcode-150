# NeetCode 150 — Rust + TypeScript

Google interview DSA practice. Both languages, same problem.

## Rules

1. Every problem gets `.rs` and `.ts` side by side in the topic folder.
2. No `src/`, no `tests/`, no boilerplate noise. Files live directly in topic folders.
3. Function-only solutions. No IO scaffolding unless the problem requires it.
4. Name files kebab-case: `two-sum.rs`, `two-sum.ts`.
5. Add `[[bin]]` to Cargo.toml only for problems you want `cargo run` on.

## Structure

```
arrays-strings/     sliding window, two pointers, prefix sum
trees-graphs/       bfs/dfs, trie, union-find, topo sort
dynamic-programming/ 1d, 2d grid, string dp, knapsack
heaps-design/       priority queue, lru/lfu cache, autocomplete
backtracking-misc/  permutations, combinations, word search
```

## Run

Rust: `cargo run --bin <name>` or `rustc --edition 2021 -O <file>.rs && ./<file>`
TypeScript: `bun <file>.ts`

## Roadmap

Follow `~/GOOGLE-DSA-ROADMAP.md` for problem priority and Google-specific tips.
