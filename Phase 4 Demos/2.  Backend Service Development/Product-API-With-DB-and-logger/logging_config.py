"""Side-by-side standard logging and structlog console demonstration.

INFO records normal operations, WARNING records rejected requests, ERROR
records failures with tracebacks, and DEBUG records diagnostic details.
Each record includes its timestamp, level, module, and source line.

Standard logging interpolates values into a readable message. Structlog keeps
values as JSON fields in the message, using the same standard-library backend.
Every application event intentionally emits both formats for comparison.
Change the configured level to DEBUG to see initialization and session events.
"""

import logging

import structlog


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s:%(lineno)d | %(message)s",
    )
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.CallsiteParameterAdder(
                [structlog.processors.CallsiteParameter.LINENO]
            ),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
