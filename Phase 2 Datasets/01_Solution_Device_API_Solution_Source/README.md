# M2S2 Device API — Reference Solution (instructor only)

Practice is from scratch: do NOT provide this folder to learners before they submit their work.

## Start
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000/docs and use Try it out → Execute.

On Windows, activate with `.venv\Scripts\activate`.

## Test
In a second terminal, after activating the venv:
```bash
python validate_m2s2_solution.py
```
Expected: 11 checks passed.

Data is in memory; restarting Uvicorn resets to two initial devices. The validation uses an in-process client and does not change the running server state.
