"""Run the static reconstruction at http://localhost:8000 (Python 3)."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=8000)
args = parser.parse_args()
root = Path(__file__).resolve().parent / 'site'
print(f'Open http://localhost:{args.port} — press Ctrl+C to stop.', flush=True)
try:
    ThreadingHTTPServer(('127.0.0.1', args.port), partial(SimpleHTTPRequestHandler, directory=str(root))).serve_forever()
except KeyboardInterrupt:
    pass
