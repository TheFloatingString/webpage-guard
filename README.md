## 🏆 Leaderboard 🏆

Score is success rate in accuracy of preventing a dox.

| Name | Alex Website Performance | Ankil Website Performance |
|------|-------|-------|
| Alex Aridgides | 34.0% | 62.0% |
| Danny | 32.0% | 50.0% |
| C-House (with lots of metadata) | 30.0% | 38.0% |
| C-House (with basic Guard) | 34.0% | 26.0% |
| C-House (with negation spans) | 32.0% | 24.0% |
| Baseline | 30.0% | 22.0% |


## Quickstart

```bash
uv run add_guard.py
uv run generate_qa.py
uv run main.py
```

## 📝 Notes 📝

- The `USE_GROQ` flag in `main.py` can be set to `True` to use Groq instead of OpenAI.
- The `VERBOSE` flag in `main.py` can be set to `True` to print the questions and answers.