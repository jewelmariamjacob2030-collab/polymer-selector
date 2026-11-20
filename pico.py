"""Pico mascot snippets used around the Polyverse interface."""

PICO_SVG = """
<svg viewBox="0 0 160 160" role="img" aria-label="Pico, the Polyverse guide" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="picoBody" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f9fff0"/><stop offset="1" stop-color="#d7edce"/>
    </linearGradient>
    <linearGradient id="picoScreen" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#234e43"/><stop offset="1" stop-color="#102d2a"/>
    </linearGradient>
  </defs>
  <ellipse cx="80" cy="145" rx="42" ry="8" fill="#143c33" opacity=".12"/>
  <path d="M80 17v14" stroke="#477b64" stroke-width="5" stroke-linecap="round"/>
  <circle cx="80" cy="12" r="8" fill="#efb64e" stroke="#fff5db" stroke-width="3"/>
  <rect x="29" y="31" width="102" height="92" rx="29" fill="url(#picoBody)" stroke="#477b64" stroke-width="5"/>
  <rect x="42" y="46" width="76" height="51" rx="19" fill="url(#picoScreen)"/>
  <ellipse cx="64" cy="69" rx="6" ry="8" fill="#b9f5cf"/>
  <ellipse cx="96" cy="69" rx="6" ry="8" fill="#b9f5cf"/>
  <path d="M67 84q13 11 26 0" fill="none" stroke="#b9f5cf" stroke-width="4" stroke-linecap="round"/>
  <path d="M29 73H16M131 73h13" stroke="#477b64" stroke-width="7" stroke-linecap="round"/>
  <circle cx="14" cy="73" r="7" fill="#efb64e"/><circle cx="146" cy="73" r="7" fill="#efb64e"/>
  <rect x="48" y="121" width="25" height="17" rx="8" fill="#477b64"/>
  <rect x="87" y="121" width="25" height="17" rx="8" fill="#477b64"/>
  <path d="M39 108q-10 13-3 22M121 108q10 13 3 22" fill="none" stroke="#477b64" stroke-width="6" stroke-linecap="round"/>
  <circle cx="80" cy="112" r="4" fill="#e6b54f"/>
</svg>
"""


def pico_message(message, eyebrow="PICO · YOUR POLYVERSE GUIDE"):
    return """
    <div class="pico-message">
      <div class="pico-avatar">{svg}</div>
      <div class="pico-bubble">
        <div class="pico-eyebrow">{eyebrow}</div>
        <div class="pico-copy">{message}</div>
      </div>
    </div>
    """.format(svg=PICO_SVG, eyebrow=eyebrow, message=message)
