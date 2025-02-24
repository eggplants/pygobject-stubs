
from typing import Optional

from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject


PIXBUF_MAJOR: int = ...
PIXBUF_MICRO: int = ...
PIXBUF_MINOR: int = ...
PIXBUF_VERSION: str = ...


def pixbuf_error_quark(*args, **kwargs): ...


class Pixbuf(Gio.Icon, Gio.LoadableIcon, GObject.Object):
    def add_alpha(*args, **kwargs): ...
    def apply_embedded_orientation(self) -> Optional[Pixbuf]: ...
    def calculate_rowstride(*args, **kwargs): ...
    def composite(*args, **kwargs): ...
    def composite_color(*args, **kwargs): ...
    def composite_color_simple(*args, **kwargs): ...
    def copy(self) -> Optional[Pixbuf]: ...
    def copy_area(*args, **kwargs): ...
    def copy_options(*args, **kwargs): ...
    def fill(self, pixel: int) -> None: ...
    def flip(*args, **kwargs): ...
    def get_bits_per_sample(*args, **kwargs): ...
    def get_byte_length(*args, **kwargs): ...
    def get_colorspace(*args, **kwargs): ...
    def get_file_info(*args, **kwargs): ...
    def get_file_info_async(*args, **kwargs): ...
    def get_file_info_finish(*args, **kwargs): ...
    @classmethod
    def get_formats(cls) -> list[PixbufFormat]: ...
    def get_has_alpha(self) -> bool: ...
    def get_height(self) -> int: ...
    def get_n_channels(*args, **kwargs): ...
    def get_option(*args, **kwargs): ...
    def get_options(*args, **kwargs): ...
    def get_pixels(*args, **kwargs): ...
    def get_rowstride(*args, **kwargs): ...
    def get_width(self) -> int: ...
    def init_modules(*args, **kwargs): ...
    @classmethod
    def new(cls, colorspace: Colorspace, has_alpha: bool, bis_per_sample: int, width: int, height: int) -> Optional[Pixbuf]: ...
    @classmethod
    def new_from_bytes(cls, data: GLib.Bytes, colorspace: Colorspace, has_alpha: bool, bits_per_sample: int, width: int, height: int, rowstride: int) -> Pixbuf: ...
    @classmethod
    def new_from_file(cls, filename: str) -> Pixbuf: ...
    @classmethod
    def new_from_file_at_scale(cls, filename: str, width: int, height: int, preserve_aspect_ratio: bool) -> Pixbuf: ...
    @classmethod
    def new_from_file_at_size(cls, filename: str, width: int, height: int) -> Pixbuf: ...
    def new_from_inline(*args, **kwargs): ...
    def new_from_resource(*args, **kwargs): ...
    def new_from_resource_at_scale(*args, **kwargs): ...
    def new_from_stream(*args, **kwargs): ...
    def new_from_stream_async(*args, **kwargs): ...
    def new_from_stream_at_scale(*args, **kwargs): ...
    def new_from_stream_at_scale_async(*args, **kwargs): ...
    def new_from_stream_finish(*args, **kwargs): ...
    def new_from_xpm_data(*args, **kwargs): ...
    def new_subpixbuf(self, src_x: int, src_y: int, width: int, height: int) -> Pixbuf: ...
    def read_pixel_bytes(*args, **kwargs): ...
    def read_pixels(*args, **kwargs): ...
    def remove_option(*args, **kwargs): ...
    def rotate_simple(*args, **kwargs): ...
    def saturate_and_pixelate(*args, **kwargs): ...
    def save_to_bufferv(self, type: str, option_keys: list[str], option_values: list[str]) -> tuple[bool, bytes]: ...
    def save_to_callbackv(*args, **kwargs): ...
    def save_to_stream_finish(*args, **kwargs): ...
    def save_to_streamv(*args, **kwargs): ...
    def save_to_streamv_async(*args, **kwargs): ...
    def savev(self, filename: str, type: str, option_keys: list[str, None], option_values: list[str]) -> bool: ...
    def scale(self, dest: Pixbuf, dest_x: int, dest_y: int, dest_width: int, dest_height: int, offset_x: float, offset_y: float, scale_x: float, scale_y: float, interp_type: InterpType) -> None: ...
    def scale_simple(self, dest_width: int, dest_height: int, interp_type: InterpType) -> Optional[Pixbuf]: ...
    def set_option(*args, **kwargs): ...
    
    def new_from_data(self, *args, **kwargs): ...
    

class PixbufAnimation:
    parent_instance = ...
    
    def get_height(*args, **kwargs): ...
    def get_iter(*args, **kwargs): ...
    def get_static_image(*args, **kwargs): ...
    def get_width(*args, **kwargs): ...
    def is_static_image(*args, **kwargs): ...
    def new_from_file(*args, **kwargs): ...
    def new_from_resource(*args, **kwargs): ...
    def new_from_stream(*args, **kwargs): ...
    def new_from_stream_async(*args, **kwargs): ...
    def new_from_stream_finish(*args, **kwargs): ...
    
    def do_get_iter(self, *args, **kwargs): ...
    def do_get_size(self, *args, **kwargs): ...
    def do_get_static_image(self, *args, **kwargs): ...
    def do_is_static_image(self, *args, **kwargs): ...
    

class PixbufAnimationIter:
    parent_instance = ...
    
    def advance(*args, **kwargs): ...
    def get_delay_time(*args, **kwargs): ...
    def get_pixbuf(*args, **kwargs): ...
    def on_currently_loading_frame(*args, **kwargs): ...
    
    def do_advance(self, *args, **kwargs): ...
    def do_get_delay_time(self, *args, **kwargs): ...
    def do_get_pixbuf(self, *args, **kwargs): ...
    def do_on_currently_loading_frame(self, *args, **kwargs): ...
    

class PixbufFormat:
    description = ...
    disabled = ...
    domain = ...
    extensions = ...
    flags = ...
    license = ...
    mime_types = ...
    name = ...
    signature = ...

    def free(*args, **kwargs): ...
    def get_description(*args, **kwargs): ...
    def get_extensions(*args, **kwargs): ...
    def get_license(*args, **kwargs): ...
    def get_mime_types(self) -> list[str]: ...
    def get_name(*args, **kwargs): ...
    def is_disabled(*args, **kwargs): ...
    def is_save_option_supported(*args, **kwargs): ...
    def is_scalable(*args, **kwargs): ...
    def is_writable(*args, **kwargs): ...
    def set_disabled(*args, **kwargs): ...
    

class PixbufLoader:
    parent_instance = ...
    priv = ...
    
    def close(self) -> bool: ...
    def get_animation(*args, **kwargs): ...
    def get_format(*args, **kwargs): ...
    def get_pixbuf(self) -> Optional[Pixbuf]: ...
    def new(*args, **kwargs): ...
    def new_with_mime_type(*args, **kwargs): ...
    def new_with_type(*args, **kwargs): ...
    def set_size(*args, **kwargs): ...
    def write(self, buf: bytes) -> bool: ...
    def write_bytes(*args, **kwargs): ...
    
    def do_area_prepared(self, *args, **kwargs): ...
    def do_area_updated(self, *args, **kwargs): ...
    def do_closed(self, *args, **kwargs): ...
    def do_size_prepared(self, *args, **kwargs): ...
    

class PixbufModule:
    _reserved1 = ...
    _reserved2 = ...
    _reserved3 = ...
    _reserved4 = ...
    begin_load = ...
    info = ...
    is_save_option_supported = ...
    load = ...
    load_animation = ...
    load_increment = ...
    load_xpm_data = ...
    module = ...
    module_name = ...
    module_path = ...
    save = ...
    save_to_callback = ...
    stop_load = ...
    

class PixbufModulePattern:
    mask = ...
    prefix = ...
    relevance = ...
    

class PixbufNonAnim:
    def new(*args, **kwargs): ...
    

class PixbufSimpleAnim:
    def add_frame(*args, **kwargs): ...
    def get_loop(*args, **kwargs): ...
    def new(*args, **kwargs): ...
    def set_loop(*args, **kwargs): ...
    

class PixbufSimpleAnimIter: ...

class PixbufFormatFlags(GObject.GFlags):
    WRITABLE = ...
    SCALABLE = ...
    THREADSAFE = ...

class Colorspace(GObject.GEnum):
    RGB = ...

class InterpType(GObject.GEnum):
    NEAREST = ...
    TILES = ...
    BILINEAR = ...
    HYPER = ...

class PixbufAlphaMode(GObject.GEnum):
    BILEVEL = ...
    FULL = ...

class PixbufError(GObject.GEnum):
    CORRUPT_IMAGE = ...
    INSUFFICIENT_MEMORY = ...
    BAD_OPTION = ...
    UNKNOWN_TYPE = ...
    UNSUPPORTED_OPERATION = ...
    FAILED = ...
    INCOMPLETE_ANIMATION = ...
    quark = ...

class PixbufRotation(GObject.GEnum):
    NONE = ...
    COUNTERCLOCKWISE = ...
    UPSIDEDOWN = ...
    CLOCKWISE = ...
