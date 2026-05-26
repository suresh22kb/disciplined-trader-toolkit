# The Survivor's Toolkit

Public download page for the three free Indian F&O trading spreadsheets that anchor the Disciplined Trader brand's Day 6 launch.

Deployed on Streamlit Community Cloud.

## What's here

- `streamlit_app.py` — the single-page Streamlit app (download UI)
- `toolkit/` — the three `.xlsx` files served by the app
  - `position-sizer.xlsx` — lite of Risk Management Supervisor (₹2,999)
  - `risk-of-ruin-calculator.xlsx` — lite of Smart Portfolio Stats Generator (₹699)
  - `trade-review.xlsx` — lite of Smart Portfolio Stats Generator (₹699)
- `requirements.txt` — `streamlit` only

## Local preview

```bash
pip install streamlit
streamlit run streamlit_app.py
```

Opens on `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Sign in to streamlit.io with GitHub
2. Click "Deploy app"
3. Repo: `suresh22kb/disciplined-trader-toolkit`
4. Branch: `main`
5. Main file: `streamlit_app.py`
6. Click Deploy. Public URL appears in 1-2 min.

## Update the sheets

Edit / regenerate the `.xlsx` files in `toolkit/`, then:

```bash
git add toolkit/
git commit -m "Update toolkit sheets"
git push
```

Streamlit Cloud auto-redeploys on push.
