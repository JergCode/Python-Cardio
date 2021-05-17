KM_TO_MILE_FACTOR = 1.609344
MILE_TO_YARD_FACTOR = 1760


def convert(value, option):
    conversions = dict({
        'mi_to_km': value * KM_TO_MILE_FACTOR,
        'mi_to_m': value * KM_TO_MILE_FACTOR * 1000,
        'mi_to_cm': value * KM_TO_MILE_FACTOR * 1_000_000,
        'mi_to_yd': value * MILE_TO_YARD_FACTOR,
        'mi_to_ft': value * MILE_TO_YARD_FACTOR * 3,
        'mi_to_in': value * MILE_TO_YARD_FACTOR * 3 * 3,
        'km_to_mi': value / KM_TO_MILE_FACTOR,
        'km_to_yd': value / KM_TO_MILE_FACTOR * MILE_TO_YARD_FACTOR,
        'km_to_ft': value / KM_TO_MILE_FACTOR * MILE_TO_YARD_FACTOR * 3,
        'km_to_in': value / KM_TO_MILE_FACTOR * MILE_TO_YARD_FACTOR * 3 * 3,
        'km_to_m': value * 1000,
        'km_to_cm': value * 1_000_000,
    })
    return conversions.get(option)
