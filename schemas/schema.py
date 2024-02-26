def individual_forex_serial(obj) -> dict:
    return {
        'id': str(obj['_id']),
        'base_currency': obj['base_currency'],
        'target_currency': obj['target_currency'],
        'rate': obj['rate'],
        'date': obj['date']
    }


def list_forex_serial(objs) -> list:
    return [individual_forex_serial(obj) for obj in objs]
