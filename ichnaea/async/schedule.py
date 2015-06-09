from datetime import timedelta

from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {

    # Monitoring tasks

    'monitor-queue-length': {
        'task': 'ichnaea.monitor.tasks.monitor_queue_length',
        'schedule': timedelta(seconds=60),
        'options': {'expires': 57},
    },
    'monitor-ocid-import': {
        'task': 'ichnaea.monitor.tasks.monitor_ocid_import',
        'schedule': timedelta(seconds=600),
        'options': {'expires': 570},
    },
    'monitor-api-key-limits': {
        'task': 'ichnaea.monitor.tasks.monitor_api_key_limits',
        'schedule': timedelta(seconds=600),
        'options': {'expires': 570},
    },

    # BBB: Continuous location update tasks

    'monitor-observations': {
        'task': 'ichnaea.monitor.tasks.monitor_measures',
        'schedule': timedelta(seconds=900),
        'options': {'expires': 990},
    },

    'location-update-cell-1': {
        'task': 'ichnaea.data.tasks.location_update_cell',
        'schedule': timedelta(seconds=29),
        'args': (1, 1000000, 1000),
        'options': {'expires': 25},
    },
    'location-update-wifi-1': {
        'task': 'ichnaea.data.tasks.location_update_wifi',
        'schedule': timedelta(seconds=31),
        'args': (1, 1000000, 1000),
        'options': {'expires': 25},
    },

    # BBB: Daily backup tasks

    's3-schedule-cellobservation-archival': {
        'task': 'ichnaea.backup.tasks.schedule_cellmeasure_archival',
        'args': (1000, 100000),
        'schedule': crontab(hour=1, minute=7),
        'options': {'expires': 43200},
    },
    's3-write-cellbackups': {
        'task': 'ichnaea.backup.tasks.write_cellmeasure_s3_backups',
        'args': (1000, 10000, 60),
        'schedule': crontab(hour=2, minute=7),
        'options': {'expires': 43200},
    },
    's3-schedule-wifiobservations-archival': {
        'task': 'ichnaea.backup.tasks.schedule_wifimeasure_archival',
        'args': (1000, 100000),
        'schedule': crontab(hour=1, minute=17),
        'options': {'expires': 43200},
    },
    's3-write-wifibackups': {
        'task': 'ichnaea.backup.tasks.write_wifimeasure_s3_backups',
        'args': (1000, 10000, 60),
        'schedule': crontab(hour=2, minute=17),
        'options': {'expires': 43200},
    },
    's3-delete-wifiobservations': {
        'task': 'ichnaea.backup.tasks.delete_wifimeasure_records',
        'args': (1000, 1, 120, 1000),
        'schedule': crontab(hour=3, minute=17),
        'options': {'expires': 43200},
    },
    's3-delete-cellobservations': {
        'task': 'ichnaea.backup.tasks.delete_cellmeasure_records',
        'args': (1000, 1, 120, 1000),
        'schedule': crontab(hour=3, minute=27),
        'options': {'expires': 43200},
    },

    # Hourly

    'update-statcounter': {
        'task': 'ichnaea.data.tasks.update_statcounter',
        'args': (1, ),
        'schedule': crontab(minute=3),
    },
    'ocid-hourly-cell-delta-import': {
        'task': 'ichnaea.export.tasks.import_latest_ocid_cells',
        'args': (True, ),
        'schedule': crontab(minute=52),
        'options': {'expires': 2700},
    },
    's3-hourly-cell-delta-export': {
        'task': 'ichnaea.export.tasks.export_modified_cells',
        'args': (True, ),
        'schedule': crontab(minute=3),
        'options': {'expires': 2700},
    },
    's3-daily-cell-full-export': {
        'task': 'ichnaea.export.tasks.export_modified_cells',
        'args': (False, ),
        'schedule': crontab(hour=0, minute=13),
        'options': {'expires': 39600},
    },

    # Couple minutes

    'continuous-cell-scan-areas': {
        'task': 'ichnaea.data.tasks.scan_areas',
        'schedule': timedelta(seconds=121),
        'args': (500, ),
        'options': {'expires': 110},
    },

    # (less than) one minute

    'update-cell': {
        'task': 'ichnaea.data.tasks.update_cell',
        'schedule': timedelta(seconds=7),
        'args': (1000, ),
        'options': {'expires': 10},
    },
    'update-mapstat': {
        'task': 'ichnaea.data.tasks.update_mapstat',
        'args': (1000, ),
        'schedule': timedelta(seconds=61),
        'options': {'expires': 57},
    },
    'update-score': {
        'task': 'ichnaea.data.tasks.update_score',
        'args': (1000, ),
        'schedule': timedelta(seconds=63),
        'options': {'expires': 57},
    },
    'update-wifi': {
        'task': 'ichnaea.data.tasks.update_wifi',
        'schedule': timedelta(seconds=6),
        'args': (1000, ),
        'options': {'expires': 10},
    },

    'schedule-export-reports': {
        'task': 'ichnaea.data.tasks.schedule_export_reports',
        'schedule': timedelta(seconds=60),
        'options': {'expires': 57},
    },

}
