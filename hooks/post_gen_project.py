import os

import os

REMOVE_PATHS = [
    'screenshots/README.txt',
    'vuln/README.txt',
    'files/README.txt',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)

