import sys
import subprocess
import importlib
import os
from IPython.display import display, Markdown, clear_output

knjiznice = {
    'matplotlib': 'matplotlib>=3.4.0',             # Risanje grafov
    'cartopy': 'cartopy>=0.20.0',                  # Kartografske projekcije
    'numpy': 'numpy>=1.21.0',                      # Numerične operacije
    'pandas': 'pandas>=1.3.0',                     
    'tqdm': 'tqdm>=4.62.0',                        # Progress bar
    'meteostat': 'meteostat>=1.6.0',               # Vremenski podatki
    'scipy': 'scipy>=1.7.0',                       # Statistika
    'IPython': 'IPython>=7.0.0',                   # Interactive Python
    'python-dateutil': 'python-dateutil',          # Datumi
}

def instalacija():
    """Preveri in namesti vse manjkajoče pakete"""
    missing = []
    
    # Preveri manjkajoče pakete
    for pkg, ver in knjiznice.items():
        try:
            importlib.import_module(pkg.split('>=')[0])
        except ImportError:
            missing.append(ver)
    
    if not missing:
        display(Markdown("Vsi potrebni paketi že nameščeni"))
        return False
    
    display(Markdown(f"{len(missing)} manjkajočih paketov"))
    
    with open(os.devnull, 'w') as devnull:
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install', *missing],
                stdout=devnull,
                stderr=devnull
            )
            clear_output()
            return True
        except subprocess.CalledProcessError:
            clear_output()
            display(Markdown("Napaka"))
            display(Markdown(f"```python\n!pip install {' '.join(missing)}\n```"))
            return False