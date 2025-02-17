# Copyright (c) 2021 Tulir Asokan
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from __future__ import annotations

import functools

import magic

try:
    _from_buffer = functools.partial(magic.from_buffer, mime=True)
    _from_filename = functools.partial(magic.from_file, mime=True)
except AttributeError:
    _from_buffer = lambda data: magic.detect_from_content(data).mime_type
    _from_filename = lambda file: magic.detect_from_filename(file).mime_type


def mimetype(data: bytes | str) -> str:
    """
    Uses magic to determine the mimetype of a file on disk or in memory.

    Supports both libmagic's Python bindings and the python-magic package.

    Args:
        data: The file data, either as in-memory bytes or a path to the file as a string.

    Returns:
        The mime type as a string.
    """
    if isinstance(data, str):
        return _from_filename(data)
    return _from_buffer(data)


__all__ = ["mimetype"]
