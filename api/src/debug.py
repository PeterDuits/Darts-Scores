import logging
import os


def trace():
    import pydevd
    try:
        pydevd.settrace(
            os.getenv('PYTHON_DEBUG_HOST', 'host.docker.internal'),
            stdoutToServer=True,
            stderrToServer=True,
            port=int(os.getenv('PYTHON_DEBUG_PORT', 5678)),
            patch_multiprocessing=True,
            trace_only_current_thread=True,
            suspend=False,
            overwrite_prev_trace=True
        )
    except ConnectionRefusedError:
        logging.warning("Connection with debugger refused")
