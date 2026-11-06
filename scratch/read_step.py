import json

with open(r'C:\Users\Sam John\.gemini\antigravity\brain\97ac1437-e779-4b26-90c3-baf1652636f8\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if '"step_index":522' in line or '"step_index": 522' in line:
            obj = json.loads(line)
            calls = obj.get('tool_calls', [])
            for c in calls:
                print(c['name'], c['args'].get('Path', ''), str(c['args'].get('CommandLine', ''))[:100])
            break
