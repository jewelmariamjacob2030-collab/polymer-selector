"""Build simplified, educational 3D molecular repeat-unit sketches with Plotly."""

import math
import plotly.graph_objects as go

# Element colours are conventional visual cues, not a claim of measured atomic scale.
ELEMENT_COLORS = {
    "C": "#505b66",
    "H": "#f3f5f7",
    "O": "#e36f69",
    "N": "#6593d6",
    "F": "#78b97b",
    "Cl": "#56a87c",
    "S": "#d7b44b",
}


def _circle_ring(cx, cy, cz, radius=0.85, count=6, start=0.0):
    pts = []
    for i in range(count):
        a = start + 2.0 * math.pi * i / count
        pts.append((cx + radius * math.cos(a), cy + radius * math.sin(a), cz + 0.10 * math.sin(2 * a)))
    return pts


def _template(name):
    """Returns atom tuples (element, x, y, z) and bond tuples (i, j, order)."""
    atoms, bonds = [], []

    def a(element, x, y, z=0.0):
        atoms.append((element, float(x), float(y), float(z)))
        return len(atoms) - 1

    def b(i, j, order=1):
        bonds.append((i, j, order))

    if name in ("Polyethylene (PE)", "PTFE", "PVC"):
        # A two-unit zig-zag backbone. Side atoms illustrate the distinguishing group.
        xs = [-1.65, -0.55, 0.55, 1.65]
        ys = [0.0, 0.45, 0.0, 0.45]
        cs = [a("C", x, y, 0.0) for x, y in zip(xs, ys)]
        for i in range(3):
            b(cs[i], cs[i + 1])
        side_element = "H" if name == "Polyethylene (PE)" else ("F" if name == "PTFE" else "Cl")
        for idx, (x, y) in enumerate(zip(xs, ys)):
            # Side substituent direction alternates to keep the model readable.
            sign = 1 if idx % 2 == 0 else -1
            if name == "PVC" and idx in (1, 3):
                side = a("Cl", x, y + sign * 0.95, 0.15)
                b(cs[idx], side)
                h = a("H", x, y - sign * 0.78, -0.25)
                b(cs[idx], h)
            else:
                # Two H or F atoms around each carbon; F is shown for PTFE.
                el = side_element
                s1 = a(el, x, y + 0.82, 0.52)
                s2 = a(el, x, y - 0.82, -0.52)
                b(cs[idx], s1)
                b(cs[idx], s2)
        return atoms, bonds

    if name == "Polylactic Acid (PLA)":
        # Two ester repeat segments: –O–CH(CH3)–C(=O)–
        prev = None
        for unit, x0 in enumerate((-1.55, 0.05)):
            o1 = a("O", x0, 0.0, 0.0)
            ch = a("C", x0 + 0.65, 0.48, 0.0)
            co = a("C", x0 + 1.35, -0.02, 0.0)
            oxy = a("O", x0 + 1.42, -0.92, 0.05)
            methyl = a("C", x0 + 0.58, 1.38, 0.28)
            b(o1, ch); b(ch, co); b(co, oxy, 2); b(ch, methyl)
            if prev is not None:
                b(prev, o1)
            prev = co
        return atoms, bonds

    if name == "PET":
        # A compact polyester segment with one terephthalate ring and ethylene-glycol linker.
        ring = _circle_ring(-0.05, 0.0, 0.0, radius=0.78, start=math.pi / 6)
        r = [a("C", *p) for p in ring]
        for i in range(6):
            b(r[i], r[(i + 1) % 6], 2 if i % 2 == 0 else 1)
        left_c = a("C", -1.55, 0.0, 0.0); b(left_c, r[3])
        left_o = a("O", -2.25, 0.62, 0.0); b(left_c, left_o, 2)
        ether = a("O", -2.25, -0.65, 0.0); b(left_c, ether)
        ch2a = a("C", -3.05, -1.12, 0.0); b(ether, ch2a)
        ch2b = a("C", -3.85, -0.65, 0.0); b(ch2a, ch2b)
        ether2 = a("O", -4.55, -1.12, 0.0); b(ch2b, ether2)
        right_c = a("C", 1.45, 0.0, 0.0); b(r[0], right_c)
        right_o = a("O", 2.10, 0.65, 0.0); b(right_c, right_o, 2)
        next_ether = a("O", 2.12, -0.62, 0.0); b(right_c, next_ether)
        next_ch2 = a("C", 2.92, -1.08, 0.0); b(next_ether, next_ch2)
        return atoms, bonds

    if name == "Kevlar":
        # Two para-substituted phenylene rings joined by amide linkages.
        left = _circle_ring(-1.15, 0.0, 0.0, radius=0.78, start=math.pi / 6)
        right = _circle_ring(1.65, 0.0, 0.0, radius=0.78, start=math.pi / 6)
        L = [a("C", *p) for p in left]
        R = [a("C", *p) for p in right]
        for ring in (L, R):
            for i in range(6):
                b(ring[i], ring[(i + 1) % 6], 2 if i % 2 == 0 else 1)
        c1 = a("C", -2.25, 0.0, 0.0); b(L[3], c1)
        o1 = a("O", -2.85, 0.65, 0.0); b(c1, o1, 2)
        n1 = a("N", -2.95, -0.65, 0.0); b(c1, n1)
        c2 = a("C", -3.9, -0.95, 0.0); b(n1, c2)
        o2 = a("O", -4.55, -0.30, 0.0); b(c2, o2, 2)
        n2 = a("N", 2.75, -0.65, 0.0); b(R[0], n2)
        c3 = a("C", 3.55, -0.95, 0.0); b(n2, c3)
        o3 = a("O", 4.15, -0.30, 0.0); b(c3, o3, 2)
        return atoms, bonds

    if name == "Nylon 6,6":
        # Simplified amide-linked chain segment with alternating carbon/nitrogen/oxygen groups.
        seq = [
            ("N", -3.0, 0.0), ("C", -2.2, 0.45), ("C", -1.4, 0.0),
            ("C", -0.6, 0.45), ("C", 0.2, 0.0), ("C", 1.0, 0.45),
            ("C", 1.8, 0.0), ("N", 2.6, 0.45), ("C", 3.4, 0.0),
        ]
        ids = [a(el, x, y, 0.0) for el, x, y in seq]
        for i in range(len(ids) - 1):
            b(ids[i], ids[i + 1])
        o = a("O", 3.95, -0.78, 0.0); b(ids[-1], o, 2)
        cnext = a("C", 4.25, 0.75, 0.0); b(ids[-1], cnext)
        return atoms, bonds

    if name == "Polyaniline (PANI)":
        # Simplified two-ring aniline-like chain segment. Real PANI structure depends on oxidation/doping.
        ring1 = _circle_ring(-1.0, 0.0, 0.0, radius=0.78, start=math.pi / 6)
        ring2 = _circle_ring(1.5, 0.0, 0.0, radius=0.78, start=math.pi / 6)
        r1 = [a("C", *p) for p in ring1]
        r2 = [a("C", *p) for p in ring2]
        for ring in (r1, r2):
            for i in range(6):
                b(ring[i], ring[(i + 1) % 6], 2 if i % 2 == 0 else 1)
        n1 = a("N", 0.02, -0.68, 0.0); b(r1[0], n1); b(n1, r2[3])
        n2 = a("N", -2.0, -0.68, 0.0); b(r1[3], n2)
        n3 = a("N", 2.5, -0.68, 0.0); b(r2[0], n3)
        return atoms, bonds

    return atoms, bonds


def make_molecule_figure(name):
    atoms, bonds = _template(name)
    if not atoms:
        return go.Figure()

    xs = [p[1] for p in atoms]
    ys = [p[2] for p in atoms]
    zs = [p[3] for p in atoms]

    # Draw bonds as individual line segments; double bonds are shown slightly thicker.
    bond_traces = []
    for i, j, order in bonds:
        bond_traces.append(
            go.Scatter3d(
                x=[xs[i], xs[j]], y=[ys[i], ys[j]], z=[zs[i], zs[j]],
                mode="lines",
                line=dict(color="#9aa7b2", width=5 if order == 2 else 3),
                hoverinfo="skip", showlegend=False,
            )
        )

    atom_trace = go.Scatter3d(
        x=xs, y=ys, z=zs, mode="markers+text",
        text=[a[0] for a in atoms], textposition="top center",
        textfont=dict(size=10, color="#e8edf2"),
        marker=dict(
            size=[10 if a[0] not in ("H",) else 6 for a in atoms],
            color=[ELEMENT_COLORS.get(a[0], "#999999") for a in atoms],
            line=dict(color="#182431", width=1), opacity=0.98,
        ),
        customdata=[[a[0], round(a[1], 2), round(a[2], 2), round(a[3], 2)] for a in atoms],
        hovertemplate="Atom: %{customdata[0]}<br>Position: (%{customdata[1]}, %{customdata[2]}, %{customdata[3]})<extra></extra>",
        name="Atoms", showlegend=False,
    )

    fig = go.Figure(data=bond_traces + [atom_trace])
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=8, b=0), height=470,
        scene=dict(
            xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False),
            bgcolor="rgba(0,0,0,0)", aspectmode="data",
            camera=dict(eye=dict(x=1.65, y=1.55, z=1.15)),
        ),
        showlegend=False,
        dragmode="turntable",
        uirevision=name,
    )
    return fig
