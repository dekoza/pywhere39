"""Main module."""
from fractions import Fraction as frac

from .wordlist import words as _words

TILE_SIZES = (frac(45, 8), frac(1, 8), frac(1, 360), frac(1, 16200), frac(1, 324000))
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


def to_words(lat, lng, count=4):
    count = 5 if count > 5 else count
    lat += 90
    lng = (lng - 180) % 360

    words = []

    for i in range(count):
        tile_size = TILE_SIZES[i]
        lat_idx = lat // tile_size
        lng_idx = lng // tile_size

        lat -= lat_idx * tile_size
        lng -= lng_idx * tile_size

        word_idx = int(lat_idx * RASTER_SIZE[i][1] + lng_idx)
        words.append(_words[word_idx])

    return words
