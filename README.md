# POLYVERSE — Python Edition

A beginner-friendly, Python-powered educational website that connects everyday objects to polymers. It includes Pico, eight polymer profiles, an everyday-object finder, random facts and interactive 3D molecular sketches.

## Features

- **Pico guide:** a friendly SVG mascot introduces each section.
- **Polymer explorer:** Kevlar, Polyaniline (PANI), PLA, PTFE, PET, PVC, Nylon 6,6 and Polyethylene.
- **Polymer selector:** enter a numbered product requirement (1–5) and receive a polymer recommendation with a one-sentence scientific justification; invalid entries prompt the user to choose again. Includes peer-testing examples.
- **Everyday finder:** choose an object and see a possible polymer match, the supporting property and practical caveats.
- **3D molecule lab:** interactive Plotly molecular sketches that can be rotated and zoomed.
- **Random facts:** discover short facts about polymers and material science.
- **Responsive layout:** custom CSS theme for desktop and mobile-sized screens.

## Run on macOS

1. Extract the ZIP file.
2. Open the `polyverse_python` folder in VS Code.
3. Open the VS Code terminal in that folder.
4. (Recommended) Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install the packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Start the website:

   ```bash
   python -m streamlit run app.py
   ```

7. Streamlit will show a local address, usually `http://localhost:8501`. Open it in your browser.

## Notes

- The website is implemented in Python using Streamlit. Plotly supplies the interactive 3D charts; you do not need to write JavaScript yourself.
- The 3D views are **simplified educational sketches** of representative repeat-unit connectivity. They are not crystallographic, measured or scale-accurate structures. Actual polymer chains can contain many repeat units and may have complex conformations.
- The polymer-to-object matches are examples, not universal claims. A product may use a different material depending on grade, design, manufacturer and local requirements.
- PLA is not guaranteed to biodegrade in ordinary soil, water or home compost. Suitable industrial composting conditions and an accepted collection route may be required.
- Polyaniline conductivity depends on oxidation state and doping. A label saying “polyaniline” alone does not guarantee high conductivity.

## Deploying

The project files are `app.py`, `polymers.py`, `molecules.py`, `pico.py`, `styles.py`, `selector.py`, and `requirements.txt`.

This project runs as a Streamlit app, not as a static GitHub Pages website. To publish it, use a Python-capable Streamlit hosting service or another host that supports running Streamlit applications. The app does not need FastAPI or a database.
