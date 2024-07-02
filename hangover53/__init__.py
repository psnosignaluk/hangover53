from .__version__ import __description__, __title__, __version__

try:
    from ._main import main
except ImportError:
    def main():
        import sys
        sys.exit(1)
