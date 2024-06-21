from bo import BO
from bs import BS

CLASSES = {
    'Python.BO': BO,
    'Python.BS': BS
}

PRODUCTIONS = [
    {
    "Python.Production": {
        "@Name": "Python.Production",
        "@LogGeneralTraceEvents": "false",
        "Description": "",
        "ActorPoolSize": "1",
        "Item": [
            {
                "@Name": "BS",
                "@ClassName": "Python.BS",
                "@PoolSize": "1",
                "@Enabled": "true",
            },
            {
                "@Name": "BO",
                "@ClassName": "Python.BO",
                "@PoolSize": "1",
                "@Enabled": "true",

            }
        ]
    }
}
]