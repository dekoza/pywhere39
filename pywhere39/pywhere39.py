"""Main module."""
from .wordlist import words as _words

TILE_SIZES = (5.625, 0.125, 0.00277777777, 0.00006172839, 0.00000308642)
RASTER_SIZE = ((32, 64), (45, 45), (45, 45), (45, 45), (20, 20))


def to_coords(words):
    assert len(set(words) & set(_words)) == len(words)
    lat, lng = -90, -180
    for i, word in enumerate(words):
        index_limit = RASTER_SIZE[i][0] * RASTER_SIZE[i][1]
        word_idx = _words.index(word)
        assert word_idx <= index_limit
        lat += word_idx // RASTER_SIZE[i][1] * TILE_SIZES[i]
        lng += word_idx % RASTER_SIZE[i][1] * TILE_SIZES[i]

    return lat, lng


# ["slush", "battle", "damage", "dentist"]
# 51.02561728383 13.723333332970014


def to_words(lat, lng, count=4):
    count = 5 if count > 5 else count
    lat += 90
    lng = (lng - 180) % 360 + 360
    lng += 180

    words = []

    for i in range(count):
        lat_idx = lat // TILE_SIZES[i]
        lng_idx = lat // TILE_SIZES[i]

        lat -= lat_idx * TILE_SIZES[i]
        lng -= lng_idx * TILE_SIZES[i]

        word_idx = int(lat_idx * RASTER_SIZE[i][1] + lng_idx)
        words.append(_words[word_idx])

    return words
