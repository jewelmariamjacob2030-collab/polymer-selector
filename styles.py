"""Custom visual theme for Polyverse."""

CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root {
  --ink: #183b32; --muted: #6e8178; --green: #285b49; --green2: #477b64;
  --cream: #f7f7ef; --paper: #fffef9; --lime: #ddecaa; --gold: #efbd57;
}
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: radial-gradient(circle at 86% 8%, rgba(222,236,170,.26), transparent 25%), #f7f7ef; color: var(--ink); }
.block-container { padding-top: 1.55rem; padding-bottom: 3rem; max-width: 1320px; }
[data-testid="stSidebar"] { background: #183d34; border-right: 1px solid rgba(255,255,255,.08); }
[data-testid="stSidebar"] * { color: #eff5e9 !important; }
[data-testid="stSidebar"] [data-testid="stRadio"] label { padding: .48rem .65rem; border-radius: 12px; }
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover { background: rgba(255,255,255,.09); }
[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,.17); }
[data-testid="stSidebar"] .stCaption { color: #b9cfc2 !important; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: #eaf3e8; }
.stButton > button { border: 1px solid #cbd9ce; border-radius: 999px; background: #fffef9; color: #214c3d; font-weight: 700; padding: .62rem 1.15rem; transition: all .18s ease; }
.stButton > button:hover { border-color: #285b49; background: #eaf2df; color: #183b32; transform: translateY(-1px); }
.stSelectbox > div > div, .stTextInput > div > div { border-radius: 14px; background: #fffef9; }
div[data-testid="stMetric"] { background: #fffef9; border: 1px solid #e4e9de; padding: 1rem 1.1rem; border-radius: 18px; }
hr { border-color: #e4e9de; }
.poly-logo { display:flex; align-items:center; gap:10px; margin: .2rem 0 1.2rem; }
.poly-logo-mark { width:34px; height:34px; display:grid; place-items:center; border-radius:12px; background:#ddecaa; color:#1d493a; font-size:20px; }
.poly-logo-name { font-family:Manrope,sans-serif; font-size:1.25rem; font-weight:800; letter-spacing:.08em; color:#f4f8ed; }
.poly-logo-sub { color:#b9cfc2; font-size:.68rem; letter-spacing:.15em; text-transform:uppercase; }
.kicker { color:#6e8977; font:500 .72rem 'DM Mono',monospace; letter-spacing:.15em; text-transform:uppercase; margin-bottom:.55rem; }
.hero { background:linear-gradient(122deg,#183d34 0%,#285b49 58%,#477b64 100%); border-radius:30px; padding:2.5rem 2.6rem; color:#f7faef; position:relative; overflow:hidden; min-height:280px; }
.hero:after { content:''; position:absolute; width:350px; height:350px; border:1px solid rgba(255,255,255,.10); border-radius:50%; right:-90px; top:-120px; box-shadow:0 0 0 32px rgba(255,255,255,.025),0 0 0 72px rgba(255,255,255,.025); }
.hero h1 { font:800 clamp(2.6rem,5.4vw,4.6rem)/1.0 Manrope,sans-serif; letter-spacing:-.06em; color:#f7faef; margin:.2rem 0 1rem; max-width:730px; }
.hero p { color:#dce9da; font-size:1.06rem; max-width:640px; line-height:1.65; }
.hero-chip { display:inline-block; border:1px solid rgba(239,245,233,.35); border-radius:999px; padding:.42rem .8rem; font:500 .68rem 'DM Mono',monospace; letter-spacing:.12em; color:#e8f2df; }
.hero-art { position:absolute; right:5%; bottom:-8px; width:210px; z-index:1; filter:drop-shadow(0 12px 18px rgba(0,0,0,.16)); }
.section-title { font:800 1.65rem Manrope,sans-serif; color:#183b32; letter-spacing:-.035em; margin:.35rem 0 .3rem; }
.section-sub { color:#718178; line-height:1.55; margin-bottom:1.1rem; }
.pico-message { display:flex; align-items:center; gap:14px; background:#eef3e5; border:1px solid #dfe9d4; border-radius:22px; padding:13px 18px 13px 12px; margin:.8rem 0 1.35rem; }
.pico-avatar { flex:0 0 68px; width:68px; height:68px; display:grid; place-items:center; background:#dcebbf; border-radius:20px; overflow:hidden; }
.pico-avatar svg { width:68px; height:68px; }
.pico-eyebrow { color:#6c886f; font:500 .64rem 'DM Mono',monospace; letter-spacing:.12em; margin-bottom:4px; }
.pico-copy { color:#23483a; font-weight:600; line-height:1.5; }
.feature-card { background:#fffef9; border:1px solid #e7eade; border-radius:22px; padding:1.25rem 1.3rem; min-height:164px; box-shadow:0 8px 22px rgba(42,70,50,.035); }
.feature-card .emoji { font-size:1.6rem; margin-bottom:.55rem; }
.feature-card h3 { font:700 1.05rem Manrope,sans-serif; margin:0 0 .4rem; color:#244638; }
.feature-card p { color:#718178; font-size:.9rem; line-height:1.5; margin:0; }
.poly-card { background:#fffef9; border:1px solid #e5e9df; border-radius:20px; padding:1.1rem; min-height:180px; }
.poly-card .poly-dot { width:10px; height:10px; border-radius:50%; display:inline-block; margin-right:7px; }
.poly-card h3 { font:700 1.06rem Manrope,sans-serif; color:#234638; margin:.6rem 0 .35rem; }
.poly-card p { color:#748278; font-size:.88rem; line-height:1.48; }
.poly-meta { color:#789082; font:500 .62rem 'DM Mono',monospace; letter-spacing:.09em; text-transform:uppercase; }
.info-panel { background:#fffef9; border:1px solid #e5e9df; border-radius:22px; padding:1.35rem 1.5rem; }
.info-panel h3 { font:700 1.05rem Manrope,sans-serif; color:#234638; margin:.1rem 0 .65rem; }
.info-panel p, .info-panel li { color:#63766c; line-height:1.6; }
.fact-panel { background:linear-gradient(135deg,#e8f0d9,#f9f2d8); border:1px solid #dfe8cc; border-radius:26px; padding:1.6rem; }
.fact-panel .fact-word { color:#81966c; font:500 .68rem 'DM Mono',monospace; letter-spacing:.14em; text-transform:uppercase; }
.fact-panel .fact-copy { color:#244638; font:700 1.35rem/1.5 Manrope,sans-serif; margin-top:.65rem; }
.molecule-note { background:#edf2e8; border-radius:14px; padding:.75rem 1rem; color:#64766a; font-size:.82rem; line-height:1.5; }
.selector-options-title { color:#6e8977; font:500 .72rem 'DM Mono',monospace; letter-spacing:.15em; margin:.8rem 0 .7rem; }
.selector-option { background:#fffef9; border:1px solid #e5e9df; border-radius:19px; padding:1rem 1.1rem; min-height:160px; margin-bottom:.75rem; box-shadow:0 7px 18px rgba(42,70,50,.035); }
.selector-option-top { display:flex; justify-content:space-between; align-items:center; gap:.5rem; }
.selector-number { display:grid; place-items:center; width:30px; height:30px; border-radius:10px; background:#e8f0d9; color:#285b49; font:700 .9rem Manrope,sans-serif; }
.selector-tag { color:#789082; font:500 .6rem 'DM Mono',monospace; letter-spacing:.08em; text-transform:uppercase; text-align:right; }
.selector-option-icon { font-size:1.45rem; margin:.65rem 0 .2rem; }
.selector-option h3 { color:#234638; font:700 .98rem/1.35 Manrope,sans-serif; margin:.2rem 0 0; }
.selector-result { background:linear-gradient(125deg,#183d34 0%,#285b49 68%,#477b64 100%); border:1px solid rgba(24,61,52,.12); border-radius:25px; padding:1.5rem 1.7rem; margin:1.25rem 0 1rem; box-shadow:0 14px 30px rgba(32,68,50,.12); }
.selector-result-kicker { color:#ddecaa; font:500 .68rem 'DM Mono',monospace; letter-spacing:.14em; }
.selector-result-row { display:flex; align-items:center; gap:1rem; margin:1rem 0 1.2rem; }
.selector-result-icon { display:grid; place-items:center; flex:0 0 54px; height:54px; border-radius:17px; background:rgba(255,255,255,.14); font-size:1.8rem; }
.selector-result-label, .selector-reason-label { color:#c7d9c5; font:500 .62rem 'DM Mono',monospace; letter-spacing:.12em; }
.selector-result-name { color:#f8faef; font:800 clamp(1.5rem,3vw,2.15rem)/1.15 Manrope,sans-serif; letter-spacing:-.04em; margin-top:.15rem; }
.selector-reason { color:#f0f5e9; font-size:1rem; line-height:1.6; margin:.35rem 0 0; max-width:850px; }
.mono { font-family:'DM Mono',monospace; }
.small-muted { color:#87958c; font-size:.8rem; }
.footer { border-top:1px solid #e4e9de; padding-top:1rem; color:#849188; font-size:.78rem; margin-top:2.5rem; }
@media (max-width: 700px) { .hero { padding:1.7rem; min-height:320px; } .hero-art { width:130px; right:3%; opacity:.9; } .hero h1 { font-size:2.7rem; } .pico-message { align-items:flex-start; } }
</style>
"""
