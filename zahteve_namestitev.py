import sys
import subprocess
import importlib
import os
from IPython.display import display, Markdown, clear_output

required_packages = {
    'pandas': 'pandas>=1.3.0',
    'numpy': 'numpy>=1.21.0',
    'matplotlib': 'matplotlib>=3.4.0',
    'seaborn': 'seaborn>=0.11.0',
    'meteostat': 'meteostat>=1.6.0',
    'scipy': 'scipy>=1.7.0',
    'tqdm': 'tqdm>=4.62.0',
    'python-dateutil': 'python-dateutil',
    'pathlib': 'pathlib>=1.0.1',
    'glob2': 'glob2',
    'time': 'time',
    'warnings': 'warnings',
    'logging': 'logging'
}

def instalacija():
    """Preveri in namesti vse manjkajoče pakete"""
    missing = []
    
    # Preveri manjkajoče pakete
    for pkg, ver in required_packages.items():
        try:
            importlib.import_module(pkg.split('>=')[0])
        except ImportError:
            missing.append(ver)
    
    if not missing:
        display(Markdown("**Vsi potrebni paketi že nameščeni**"))
        return False
    
    display(Markdown(f"**{len(missing)} manjkajočih paketov**"))
    
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
            display(Markdown("**Napaka pri nameščanju**"))
            display(Markdown("Poskusite ročno namestiti"))
            display(Markdown(f"```python\n!pip install {' '.join(missing)}\n```"))
            return False

# Izvedemo namestitev
were_packages_installed = instalacija()

# Pokažemo navodila za ponovni zagon SAMO če je bilo nameščanje
if were_packages_installed:
    display(Markdown("**Kernel → Restart Kernel**"))