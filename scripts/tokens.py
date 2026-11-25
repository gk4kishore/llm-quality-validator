from llmqv.client import generate

prompts = [
        " Hi, Software testing is the process of evaluating a program to find defects before users do Good tests are repeatable, fast, and check one behavior at a time, so failures point straight to the cause.",
    "def add(a, b):\n    return a + b",
    "నేను ప్రతిరోజూ కొత్త విషయాలు నేర్చుకుంటాను.",
]

for p in prompts:
    r = generate(p)
    print(r["prompt_eval_count"], r["eval_count"], p[:40])
#   prompt_eval_count, eval_count, and prompt[:40]
