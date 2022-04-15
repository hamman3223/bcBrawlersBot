LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default_formatter": {
            "format": '[%(levelname)s:%(actime)s] %(message)s'
        },

    },

    "handlers": {
        "stream_handler": {
            "class": "logging.StreamHandler",
            'formatter': "default_formatter",
        },
    },

    "loggers": {
        "my_logger": {
            "handler": ["stream_handler"],
            "level": "DEBUG",
            "propagate": True,
        }

    }
}

        # "info": {
        #     "handler": ["stream_handler"],
        #     "level": "INFO",
        #     "propagate": True,
        # },

        # "error": {
        #     "handler": ["stream_handler"],
        #     "level": "ERROR",
        #     "propagate": True,
        # }