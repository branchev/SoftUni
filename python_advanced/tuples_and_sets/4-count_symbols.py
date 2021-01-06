from collections import defaultdict

symbol_dict = defaultdict(int)

line = input()
for s in line:
    symbol_dict[s] += 1

srt_symbols = {k: v for k, v in sorted(symbol_dict.items(), key=lambda item: item[0])}

for sym, occs in srt_symbols.items():
    print(f"{sym}: {occs} time/s")